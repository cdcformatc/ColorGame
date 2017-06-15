from __future__ import division
import random

MAX_PLAYERS = 10

class Wordlist():
    def __init__(self):
        self.nouns = [word.strip() for word in open("noun_list.txt","r")]
        self.words = []
        
    def random_noun(self):
        while True:
            word = random.choice(self.nouns)
            if word not in self.words:
                self.words.append(word)
                return word

class Name():
    def __init__(self):
        self.n = words.random_noun()
        self.s = 100
        
    def __str__(self):
        return self.n

class Category():
    def __init__(self, range, names):
        self.min = range[0]
        self.max = range[1]
        self.names = names
        self.preferred = self.names[-1]
        
    def is_in(self, i):
        return self.min <= i < self.max
        
    def __str__(self):
        return '{} {} {}'.format(self.min, self.max, ','.join(str(n) for n in self.names))

class Player():
    def __init__(self,name):
        self.name = name
        self.categories = [Category((0,360),[Name()])]
        
    def perceive(self,colors):
        h = colors[0]
        print 'Topic:',h
        rest = colors[1:]
        
        for cat in self.categories:
            if cat.is_in(h):
                topic_cat = cat
                break
        
        print topic_cat
        
        collisions = [obj for obj in rest if topic_cat.is_in(obj)]
        print 'Collision:', collisions
        
        if not collisions:
            print [str(cat) for cat in self.categories]
            return topic_cat
        
        a_list = [i for i in collisions if i < h]
        b_list = [i for i in collisions if i > h]
        a_list.append(-1)
        b_list.append(361)
        
        a = max(a_list)
        b = min(b_list)
        
        print a,b
        
        if a > b:
            a,b = b,a
            
        if a != -1 and b != 361:
            cat0 = (topic_cat.min,(a+h)/2)
            cat1 = ((a+h)/2,(b+h)/2)
            cat2 = ((b+h)/2,topic_cat.max)
        elif a == -1:
            cat0 = (topic_cat.min,(b+h)/2)
            cat1 = ((b+h)/2,topic_cat.max)
            cat2 = ()
        elif b == 361:
            cat0 = (topic_cat.min,(a+h)/2)
            cat1 = ((a+h)/2,topic_cat.max)
            cat2 = ()
            
        self.categories.remove(topic_cat)
        self.categories.append(Category(cat0,topic_cat.names+[Name()]))
        self.categories.append(Category(cat1,topic_cat.names+[Name()]))
        if cat2:
            self.categories.append(Category(cat2,topic_cat.names+[Name()]))
        
        print [str(cat) for cat in self.categories]
        raw_input()
        
words = Wordlist()
def game(iterations):
    num_players = random.randint(2,MAX_PLAYERS)
    print "Number of Players {}".format(num_players)
    players = [Player(str(i)) for i in range(num_players)]
    
    for t in range(iterations):
        s,h = random.sample(players,2)
        print "Speaker {} Hearer {}".format(s.name,h.name)
        
        M = 5
        items = range(360)
        random.shuffle(items)
        items = items[0:M]
        print "Scene {}".format(items)
        
        s.perceive(items)
        
    
if __name__== "__main__":
    game(100)
