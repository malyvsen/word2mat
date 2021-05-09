from typing import Set
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import lzma
import numpy as np
from tqdm.auto import tqdm


@dataclass(frozen=True)
class Vectors:
    known_words: Set[str]  # TODO: load vectors as well (without eating up all the RAM)

    @classmethod
    def from_xz_file(cls, path: Path) -> "Vectors":
        known_words = set()
        with lzma.open(path) as file:
            iterator = map(
                lambda b: b.decode(errors="ignore") if isinstance(b, bytes) else b,
                iter(file),
            )
            line = next(iterator).split(" ")
            num_vectors = int(line[0])
            dimensionality = int(line[1])
            for line in tqdm(iterator, desc="Reading word vectors", total=num_vectors):
                split = line.strip().split(" ")
                # vector = [float(value) for value in split[1:]]
                # assert len(vector) == dimensionality
                # vectors[split[0].lower()] = vector
                known_words.add(split[0].lower())
        return cls(known_words=known_words)


@lru_cache
def get_word2vec():
    return Vectors.from_xz_file(Path(__file__).parent.parent / "data" / "word2vec.xz")
