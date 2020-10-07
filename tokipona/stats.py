from .words import words, word_forms
from .text import text



num_words_in_text = sum(len(sentence) for sentence in text)
form_frequency = {
    form: len([
        word
        for sentence in text
        for word in sentence
        if word == form
    ])
    for form in word_forms
}