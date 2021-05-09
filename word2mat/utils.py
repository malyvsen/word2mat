from functools import lru_cache
import spacy


@lru_cache
def get_nlp():
    return spacy.load("en_core_web_md")
