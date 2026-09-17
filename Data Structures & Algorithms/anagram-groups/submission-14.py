class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        dict_all = {}
        
        for s in range(len(strs)):
            str_s = strs[s]
            list_s = sorted("".join(str_s))
            tup_s = tuple(list_s)
            if tup_s not in dict_all.keys(): dict_all[tup_s] = [s]
            else: dict_all[tup_s].append(s)
        
        for key in dict_all.keys():
            ret.append([strs[i] for i in dict_all[key]])
        return ret

                    
        
        
        