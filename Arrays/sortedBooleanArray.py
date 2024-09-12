from typing import List 

def find_boundary(arr: List[bool]) -> int: 
    left = 0 #start of the search range 
    right = len(arr) - 1 #end of the search range 
    boundary_index = -1 #start with -1 to indicate we haven't dounf a 'true' yet 

    while left <= right: 
        mid = (left + right) //2 
        if arr[mid]: 
            boundary_index = mid 
            right = mid - 1
        else: 
            left = mid + 1 
        return boundary_index
    return 0 

if __name__ == '__main__': 
    arr = [x == "true" for x in input ().spilt()]
    res = find_boundary(arr)
    print(res)
