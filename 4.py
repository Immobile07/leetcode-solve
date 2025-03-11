class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        lr=[]
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i]<=nums2[j]:
                lr.append(nums1[i])
                i+=1
            else:
                lr.append(nums2[j])
                j+=1
        while(i<len(nums1)):
            lr.append(nums1[i])
            i+=1
        while(j<len(nums2)):
            lr.append(nums2[j])
            j+=1
        if len(lr)%2==0:
            return (lr[len(lr)//2] + lr[(len(lr)//2)-1])/2
        else:
            return lr[len(lr)//2]