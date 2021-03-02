"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """
    Find a random word from a given dictionary:
    >>> wf = WordFinder("test.txt")
    4 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'duck'

    >>> wf.random()
    'dog'

    """
    def __init__(self, path):
        """Open the file and report the number of words read """

        dictionary = open(path)
        self.words = self.parse(dictionary)
        print(f"{len(self.words)} words read")

    def parse(self, dictionary):
        """ Parse the dictionary file into a list of words"""

        return [word.strip() for word in dictionary]

    def random(self):
        """Return random word"""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """
    Refactor WordFinder so that it excludes comments:
    >>> special_w = SpecialWordFinder('test2.txt')
    4 words read
    >>> special_w.random()
    'kale'
    >>> special_w.random()
    'parsnip'
    >>> special_w.random()
    'kale'
    >>> special_w.random()
    'mango'
    """
    def parse(self, dictionary):
        """Parse the dictionary file into a list of words
        skipping the comments """

        return [word.strip() for word in dictionary
                if word.strip() and not word.startswith('#')]
