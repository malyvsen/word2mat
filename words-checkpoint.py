import os
import json



with open(os.path.join(os.path.dirname(__file__), 'words.json'), 'r') as words_file:
    words = json.load(words_file)

word_forms = [
    form
    for word in words
    for form in word['forms']
]