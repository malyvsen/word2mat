# Word2Mat

Hoi! This is an NLP research project. We're trying to find an alterative way to represent word meanings in a computer - one which could elegantly be extended to produce meanings of phrases while taking word order into account.

## Instructions

### Data

There are two important classes: `Dataset` and `Phrase`. A `Dataset` is a collection of phrases, a `Phrase` is a collection of words.

Example usage:

```python
dataset = Dataset.from_file("path/to/file.txt")
len(dataset) # 30184
len(dataset.unique_words) # 2941
for phrase in dataset.clean.shuffled:
	print(phrase.without_punctuation.words) # ("mary", "had", "a", "little", "lamb"), ...
```

### Vectors

Half-ready :) Download word vectors from [here](https://kth.box.com/s/d8epqp9ipiyyteae35qr7j921rnowtaz) and put them under `data/word2vec.xz`. You'll be able to load them using `Vectors.from_xz_file`. Currently, this only lists the known words - we'll add loading the actual word2vec vectors later.
