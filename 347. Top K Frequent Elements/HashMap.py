from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            hmap[n] = 1 + hmap.get(n, 0)
        
        for i, j in hmap.items():
            freq[j].append(i)
        
        res=[]
        for k in range(len(freq)-1, 0, -1):
            for p in freq[k]:
                res.append(p)
                if len(res) == k:
                    return res
        
        return res

    
def main():
    map_sol= Solution()
    print(map_sol.topKFrequent([1,1,1,2,2,3], k=2))

if __name__ == "__main__":
    main()