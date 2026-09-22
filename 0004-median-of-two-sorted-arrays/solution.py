class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # To achieve O(log(min(m, n))) time complexity, we always run binary search 
        # on the smaller array. Swap them if nums1 is larger than nums2.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        
        # Binary search pointers for the smaller array (nums1)
        left, right = 0, m
        
        while left <= right:
            # Partition index for nums1
            partition1 = (left + right) // 2
            # Partition index for nums2 (ensures left half has same or 1 more element than right half)
            partition2 = (m + n + 1) // 2 - partition1
            
            # Find the border values for the partitions.
            # Use negative infinity for out-of-bounds on the left, positive infinity on the right.
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we have found the correct valid partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                
                # If the combined array has an odd number of elements, 
                # the median is the largest element on the left side.
                if (m + n) % 2 != 0:
                    return float(max(maxLeft1, maxLeft2))
                
                # If the combined array has an even number of elements, 
                # the median is the average of the largest left and smallest right elements.
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            
            # If the largest element on the left of nums1 is greater than the 
            # smallest element on the right of nums2, our partition is too far right.
            elif maxLeft1 > minRight2:
                right = partition1 - 1
                
            # Otherwise, our partition is too far left.
            else:
                left = partition1 + 1
