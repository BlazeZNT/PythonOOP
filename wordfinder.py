"""Word Finder: finds random words from a dictionary."""

import random




class WordFinder:
    '''
    >>> wf = WordFinder("/Users/student/words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    '''
    
    def __init__(self,path):
        file = open(path)
        self.words = self.parse(file)
        print(f"{len(self.words)} words read")
        
         
    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)

wf = WordFinder("words.txt")
print(wf.random())