class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hash map creation for each word and group together
        anagram = {}

        for word in strs:                
            ordered = "".join(sorted(word))
            if ordered in anagram:
                value = anagram[ordered]
                value.append(word)
                anagram[ordered] = value
            else:
                anagram[ordered] = [word]
        
        return list(anagram.values())
        
