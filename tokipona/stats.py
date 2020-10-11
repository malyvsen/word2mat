from .words import words, word_forms
from .text import sentences



num_words_in_text = sum(len(sentence) for sentence in sentences)
form_frequency = {
    form: len([
        word
        for sentence in sentences
        for word in sentence
        if word == form
    ])
    for form in word_forms
}