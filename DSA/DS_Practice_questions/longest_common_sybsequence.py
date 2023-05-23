class Solution():
	def longest_common_subsequence_recursive(self,seq1,seq2):
		if not seq1 or not seq2:
			return 0
		if seq1[0] == seq2[0]:
			return 1 + self.longest_common_subsequence_recursive(seq1[1:],seq2[1:])
		else:
			return max(self.longest_common_subsequence_recursive(seq1[1:],seq2),\
				self.longest_common_subsequence_recursive(seq1, seq2[1:]))
	def longest_common_subsequence_dynamic_programming(self,seq1,seq2):
		table = [[0 for _ in range(len(seq2)+1)] for _ in range(len(seq1)+1)]
		for i,x in enumerate(seq1):
			for j,y in enumerate(seq2):
				if x == y:
					table[i+1][j+1] = 1 + table[i][j]
				else:
					table[i+1][j+1] = max(table[i+1][j],table[i][j+1])
		result = ""
		i,j = len(seq1),len(seq2)
		while i > 0 and j > 0:
			if seq1[i-1] == seq2[j-1]:
				result = seq1[i-1] + result
				i,j = i-1,j-1
			elif table[i-1][j]>table[i][j-1]:
				i -= 1
			else:
				j -= 1
		return table[-1][-1], result

obj = Solution()
print(obj.longest_common_subsequence_recursive("abcd","bd"))
print(obj.longest_common_subsequence_dynamic_programming("abcd","bd"))