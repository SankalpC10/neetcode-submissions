class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            base = ''.join(sorted(word))
            anagram_map[base].append(word)
        return list(anagram_map.values())
