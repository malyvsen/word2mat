import os
from .words import word_forms



with open(os.path.join(os.path.dirname(__file__), 'text.txt'), 'r') as file:
    file_contents = file.read().strip()

def sanitize(paragraph):
    replace_with_spaces = '\n’\'":,;'
    for symbol in replace_with_spaces:
        paragraph = paragraph.replace(symbol, ' ')
    return paragraph

paragraphs = [
    sanitize(paragraph)
    for paragraph in file_contents.split('\n\n')
]

def split_sentences(paragraph):
    sentence_endings = '.!?()[]'
    for symbol in sentence_endings:
        paragraph = paragraph.replace(symbol, '.')
    return paragraph.split('.')


def split_words(sentence):
    return [
        word
        for word in sentence.split()
        if word in word_forms
    ]

sentences = [
    words
    for words in [
        split_words(sentence)
        for paragraph in paragraphs
        for sentence in split_sentences(paragraph)
    ]
    if words != []
]