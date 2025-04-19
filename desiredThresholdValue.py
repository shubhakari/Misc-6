# Given a list of integers and desiredSum, find the threshold value such that if we replace all the values in the input list which are greater then threshold value with the threshold value then the sum of the list should be equal to the desired sum. Testcase 1 in = [2,1,5] desiredSum = 6 output = 3 Testcase 2 in = [2,1,5] desiredSum = 2 output = 0.67 Testcase 3 in = [2,1,5] desiredSum = 4 output = 1.5 Testcase 4 in = [2,1,5] desiredSum = 1 output = 0.33
class Solution:
    # TC : O(n log n)
    # SC : O(1)
    def findThreshold(self, nums: List[int], desiredSum: float) -> float:
        nums.sort()
        n = len(nums)
        desiredThreshold = desiredSum / n
        for i in range(n):
            if desiredThreshold > nums[i]:
                diff = desiredThreshold - nums[i]
                desiredThreshold += (diff/(n-i-1))
            else:
                break

        return desiredThreshold
                
                

# Example cases
solution = Solution()
print(solution.findThreshold([2,1,5], 6))  # Output: 3.00
print(solution.findThreshold([2,1,5], 2))  # Output: 0.67
print(solution.findThreshold([2,1,5], 4))  # Output: 1.50
print(solution.findThreshold([2,1,5], 1))  # Output: 0.33