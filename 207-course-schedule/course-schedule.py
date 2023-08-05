class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        seen = set()

        def dfs(crs):
            if crs in seen:
                return False
            if preMap[crs]==[]:
                return True
            seen.add(crs)
            for x in preMap[crs]:
                if not dfs(x):
                    return False
            preMap[crs]=[]
            seen.remove(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
