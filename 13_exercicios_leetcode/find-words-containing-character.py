# https://leetcode.com/problems/find-words-containing-character/

def findWordsContaining(words, letter):
    return [i for i, word in enumerate(words) if letter in word]

 def test():   
    # Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.
    assert findWordsContaining(words=["leet", "code"], letter="e") == [0, 1]
    
    # Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.
    assert findWordsContaining(words=["abc", "bcd", "aaaa", "cbc"], letter="a") == [0, 2]
    
    # Explanation: "z" does not occur in any of the words. Hence, we return an empty array.
    assert findWordsContaining(words=["abc", "bcd", "aaaa", "cbc"], letter="z") == []
