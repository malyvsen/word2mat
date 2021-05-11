from typing import Tuple, FrozenSet
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from random import sample
from datasets import load_dataset
from tqdm.auto import tqdm
from word2mat.utils import get_nlp
from .sentence import Sentence


@dataclass(frozen=True)
class Dataset:
    sentences: Tuple[Sentence]

    @classmethod
    def from_file(cls, path: Path) -> "Dataset":
        with open(path, "r", encoding="utf8") as file:
            return cls(
                sentences=tuple(
                    [
                        Sentence.from_spacy(sentence)
                        for sentence in get_nlp()(file.read()).sents
                    ]
                )
            )

    @classmethod
    def from_huggingface(
        cls,
        dataset_name: str,
        config: str = None,
        split: str = "train",
        column: str = "text",
    ) -> "Dataset":
        huggingface_dataset = load_dataset(dataset_name, config)[split]
        return cls(
            sentences=tuple(
                [
                    Sentence.from_spacy(sentence)
                    for data in tqdm(huggingface_dataset, desc="Reading dataset")
                    for sentence in get_nlp()(data[column]).sents
                ]
            )
        )

    @property
    def clean(self) -> "Dataset":
        return type(self)(
            sentences=tuple(
                [
                    cleaned
                    for sentence in self.sentences
                    if not sentence.contains_rare_words
                    if len(cleaned := sentence.without_whitespace) > 0
                ]
            )
        )

    @cached_property
    def unique_words(self) -> FrozenSet[str]:
        return frozenset(word for sentence in self.sentences for word in sentence.words)

    @property
    def shuffled(self) -> "Dataset":
        return type(self)(
            sentences=tuple(sample(self.sentences, k=len(self.sentences)))
        )

    def __len__(self) -> int:
        return len(self.sentences)

    def __iter__(self):
        return iter(self.sentences)
