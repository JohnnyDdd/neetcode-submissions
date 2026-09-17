class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_all = {}
        
        for s in range(len(strs)):
            str_s = strs[s]
            list_s = sorted("".join(str_s))
            tup_s = tuple(list_s)
            if tup_s not in dict_all.keys(): dict_all[tup_s] = [str_s]
            else: dict_all[tup_s].append(str_s)
        
        return list(dict_all.values())


                    
        
        
        