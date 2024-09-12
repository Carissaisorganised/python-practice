#A sorted array of unique inttegers was roatated at an unknown pivot. 
# Find the the index of the minium element in this array

def find_minimum_index(nums): 
    left, right = 0, len(nums) - 1 

    while left < right: 
        mid = left + (right - left) //2 

        if nums[mid] > nums[right]: 
            left = mid + 1 
        else: 
            right = mid 

            return left