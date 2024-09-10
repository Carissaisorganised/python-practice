#rotate left till zero 
from collections import deque
from typing import list 

def rotate_left_till_zero(nums: List[int]) -> List [int]: 
    #initalise a new deque out of nums 
    queue = deque(nums)
    #continue the loop till front of queue is 0 
    while queue[0] !=0: 
        # remove the front of the queue and add it to the end 
        queue.append(queue.popleft())
        return queue
if __name__ == '__main__': 