"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be constructed from the magazines ; 
otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

class Solution():
	def __init__(self,ransom_note,magazine):
		self.ransom_note = ransom_note
		self.magazine = magazine
	
	def is_ransome_note(self):
		from collections import Counter
		magazine_hash_map = Counter(self.magazine)
		for char in self.ransom_note:
			if char in magazine_hash_map:
				magazine_hash_map[char] = magazine_hash_map.get(char) - 1
				if magazine_hash_map[char] < 0:
					return False
			else:
				return False
		return True

obj = Solution('a','b')
print(obj.is_ransome_note())
obj = Solution('aa','ab')
print(obj.is_ransome_note())
obj = Solution('aa','aab')
print(obj.is_ransome_note())