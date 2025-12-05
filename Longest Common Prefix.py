class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        store = ""
        for i in range(len(strs[0])):
            store2 = strs[0][i]

            for j in strs:
                if j[i]!= store2:
                    return store
            store = store + store2
        return store
                
        



s = Solution()

print(s.longestCommonPrefix(["flower", "flow","flight"]))
