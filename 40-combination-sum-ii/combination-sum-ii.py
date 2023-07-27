class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output=[]
        candidates.sort()

        def recurse(i, cur_list, cur_sum):
            if cur_sum==target:
                output.append(cur_list.copy())
                return
            elif cur_sum>target or i>=len(candidates):
                return
            else:
                recurse(i+1,cur_list+[candidates[i]], cur_sum+candidates[i])
                while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                    i += 1
                recurse(i+1, cur_list,cur_sum)
        recurse(0,[],0)
        return output