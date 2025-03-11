class Solution:
    def applyOperations(self, arr: List[int]) -> List[int]:
        i=0
        j=i+1
        while(j<len(arr)):
            if arr[i]==arr[j]:
                arr[i]=arr[i]*2
                arr[j]=0
                i+=1
                j+=1
            else:
                i+=1
                j+=1
        for i in range(0,len(arr)):
            change=False
            for j in range(1,len(arr)):
                if arr[j-1]==0 and arr[j]!=0:
                    arr[j-1]=arr[j]
                    arr[j]=0
                    change=True
            if change==False:
                break
        return arr