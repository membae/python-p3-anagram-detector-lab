# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word=word.lower()
        self.sorted_word=sorted(self.word)

    def match(self,possible_anagrams):
        matches=[]

        for watu in possible_anagrams:
            if sorted(watu.lower())==self.sorted_word:
                matches.append(watu)

        return matches
    