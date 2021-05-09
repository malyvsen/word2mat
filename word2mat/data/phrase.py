from typing import Tuple
from dataclasses import dataclass
from string import punctuation, whitespace
from word2mat.vectors import get_word2vec


@dataclass(frozen=True)
class Phrase:
    words: Tuple[str]

    @classmethod
    def from_sentence(cls, sentence) -> "Phrase":
        return cls(words=tuple([word.lower_ for word in sentence]))

    @property
    def contains_rare_words(self):
        return any(word not in get_word2vec().known_words for word in self.words)

    @property
    def without_whitespace(self) -> "Phrase":
        return self.without_characters(whitespace)

    @property
    def without_punctuation(self) -> "Phrase":
        return self.without_characters(punctuation)

    def without_characters(self, forbidden_characters: str) -> "Phrase":
        return type(self)(
            word=tuple(
                [word for word in self.words if word not in forbidden_characters]
            )
        )
