from typing import Tuple
from dataclasses import dataclass
from string import punctuation, whitespace
from word2mat.vectors import get_word2vec


@dataclass(frozen=True)
class Sentence:
    words: Tuple[str]

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
