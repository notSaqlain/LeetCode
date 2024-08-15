# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()
        total = len(merged)

        if total % 2 == 1:
            return float(merged[total // 2])
        else:
            middle1 = merged[total // 2 - 1]
            middle2 = merged[total // 2]
            return (float(middle1) + float(middle2)) / 2.0
        
def main():
    map_sol= Solution()
    print(map_sol.findMedianSortedArrays([1,3], [2]))
    print(map_sol.findMedianSortedArrays([1,2], [3,4]))
    print(map_sol.findMedianSortedArrays([0,0], [0,0]))
    print(map_sol.findMedianSortedArrays([], [1]))
    print(map_sol.findMedianSortedArrays([2], []))

if __name__ == "__main__":
    main()