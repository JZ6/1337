class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    
        total_len = len(nums1) + len(nums2)
        target_median = int(total_len/2)
        odd = total_len % 2
                                  
        i1= 0
        i2= 0
        last2 = (0, 0)
        
        while (i1 + i2) < (target_median + 1):
            
            increment1 = i2 > len(nums2) - 1
            increment2 = i1 > len(nums1) - 1 
                        
            if not (increment1 or increment2):
                increment1 = nums1[i1] < nums2[i2]
            
            if increment1: 
                last2 = (last2[1], nums1[i1])
                i1+=1
            else:
                last2 = (last2[1], nums2[i2])
                i2+=1
            
        return last2[1] if odd else sum(last2)/2
