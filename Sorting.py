from typing import List

def sort_list(unsorted_list: List[int]) -> List [int]: 
    #Loop over the entire list 
    for i in range(1, len (unsorted_list)): 
        key = unsorted_list[i] #The current element to be inserted 
        j = i-1 
        #Move th eelements of unsorted_list [0..i-1], that are greater than 
        #to one position ahead of their current position 

    while j >=0 and key < unsorted_list[j] : 
        unsorted_list [j+1] = unsorted_list[j]
        j -= 1 
        unsorted_list[j+1] = key 
    return unsorted_list

if __name__ == '__main__': 
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(''.join(map(str,res)))