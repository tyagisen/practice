''''
lets start with the str
'''
class Solution(object):
    def findMedianSortedArray(self,num1, num2):
        num1.extend(num2)
        num1.sort()
        print((len(num1)//2)-1)
        print(num1[9])
        # print(num1[6])
        if len(num1)%2==0:
            avg1= int(len(num1)//2)
            avg2= int(len(num1)//2)

            median = num1[avg2], num1[avg1] 
        else:
            avg1 = int(len(num1)//2)
            avg2 = int(len(num1)//2)

            median =avg1+avg2/2

        return median


arr1 = [1,1,2,3,5,8,13,21]
arr2 = [2,3,5,7,11,13,17,19]

sol = Solution()
print(sol.findMedianSortedArray(arr1,arr2))