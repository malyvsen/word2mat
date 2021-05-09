from typing import Tuple, FrozenSet
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from random import sample
from datasets import load_dataset
from word2mat.utils import get_nlp
from .phrase import Phrase


@dataclass(frozen=True)
class Dataset:
    phrases: Tuple[Phrase]

    @classmethod
    def from_file(cls, path: Path) -> "Dataset":
        with open(path, "r", encoding="utf8") as file:
            return cls(
                phrases=tuple(
                    [
                        Phrase.from_sentence(sentence)
                        for sentence in get_nlp()(file.read()).sents
                    ]
                )
            )

    @classmethod
    def from_huggingface(
        cls, dataset_name: str, config: str = None, split: str = "train"
    ) -> "Dataset":
        huggingface_dataset = load_dataset(dataset_name, config)[split]
        return cls(
            phrases=tuple(
                [
                    Phrase.from_sentece(sentence)
                    for data in huggingface_dataset
                    for sentence in get_nlp()(data["text"]).sents
                ]
            )
        )

    @property
    def clean(self) -> "Dataset":
        return type(self)(
            phrases=tuple(
                [
                    cleaned
                    for phrase in self.phrases
                    if not phrase.contains_rare_words
                    if len(cleaned := phrase.without_whitespace) > 0
                ]
            )
        )

    @cached_property
    def unique_words(self) -> FrozenSet[str]:
        return frozenset(word for phrase in self.phrases for word in phrase.words)

    @property
    def shuffled(self) -> "Dataset":
        return type(self)(phrases=tuple(sample(self.phrases, k=len(self.phrases))))

    def __len__(self) -> int:
        return len(self.phrases)

    def __iter__(self):
        return iter(self.phrases)
