class Solution:
	def reverseString(self, s: List[str]) -> None:
		
		def revStr(st, s, e):
			if s >= e:
				return
			st[s], st[e] = st[e], st[s]
			revStr(st, s+1, e-1)

		revStr(s, 0, len(s)-1)
