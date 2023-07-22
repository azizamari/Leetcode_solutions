class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output=[]

        def recurse(i, cur_list, cur_sum):
            if cur_sum==target:
                output.append(cur_list.copy())
                return
            elif cur_sum>target or i>=len(candidates):
                return
            else:
                recurse(i,cur_list+[candidates[i]], cur_sum+candidates[i])
                recurse(i+1, cur_list,cur_sum)
        recurse(0,[],0)
        return output
