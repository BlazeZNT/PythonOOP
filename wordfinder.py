"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self,path):
        new = open(path)
        self.words = self.words_read(new)
        print(f"There are {len(self.words)} words")
        

    
    def words_read(self,new):
        # for word in self.new:
        #     self.new_list.append(word)
        return [i.strip() for i in new]
    
    def random(self):
        return(random.choice(self.words))
            
        
    
    
class SpecialWordFinder(WordFinder):
    def words_read(self,new):
        return [w.strip() for w in new if w.strip() and not w.startswith('#')]
            
            
    
    
        

# wf = WordFinder("words.txt")
# print(wf.random())
# print(wf.random())
# print(wf.random())

ws = SpecialWordFinder("complex.txt")
print(ws.random())
print(ws.random())
print(ws.random() in ["pear", "carrot", "kale"])
print(ws.random() in ["pear", "carrot", "kale"])
print(ws.random() in ["pear", "carrot", "kale"])