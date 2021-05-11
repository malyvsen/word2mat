from typing import Tuple
from dataclasses import dataclass
from string import punctuation, whitespace
from word2mat.vectors import get_word2vec


@dataclass(frozen=True)
class Sentence:
    words: Tuple[str]

    @classmethod
    def from_string(cls, string: str) -> "Sentence":
        result = []
        for word in string.split():
            splits = [word]
            for character in set(punctuation) - set("'"):
                splits = [
                    subsplit
                    for split in splits
                    for subsplit in supersplit(split, character)
                ]
            for split in splits:
                apostrophe_split = supersplit(split, "'")
                if len(apostrophe_split) == 3:
                    result.append(apostrophe_split[0])
                    result.append("'" + apostrophe_split[2])
                else:
                    result += apostrophe_split
        return cls(words=tuple(word.lower() for word in result))

    @classmethod
    def from_spacy(cls, spacy_sentence) -> "Sentence":
        return cls(words=tuple([word.lower_ for word in spacy_sentence]))

    @property
    def contains_rare_words(self):
        return any(word not in get_word2vec().known_words for word in self.words)

    @property
    def without_whitespace(self) -> "Sentence":
        return self.without_characters(whitespace)

    @property
    def without_punctuation(self) -> "Sentence":
        return self.without_characters(punctuation)

    def without_characters(self, forbidden_characters: str) -> "Sentence":
        return type(self)(
            words=tuple(
                [word for word in self.words if word not in forbidden_characters]
            )
        )

    def __len__(self) -> int:
        return len(self.words)


def supersplit(string: str, delimiter: str):
    """Like str.split, but keeps delimiter and discards empty bits."""
    return [
        bit
        for split in string.split(delimiter)
        for bit in [delimiter, split]
        if len(bit) > 0
    ][1:]
