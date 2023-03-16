class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        #get the greatest element should array be bigger than 1
        if len(arr) > 1: greatest = max(arr[1:])

        for i in range(len(arr)):
            #if at final element change value to -1 and return array
            if i == len(arr) - 1:
                arr[i] = -1
                return arr
            
            #if the current value == greatest value, change the greatest value
            if arr[i] == greatest:
                greatest = max(arr[i+1:])
            
            #replace the current value with the greatest
            arr[i] = greatest
            