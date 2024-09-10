from collections import deque
from typing import Deque, List 

def execute(program: List[str]) -> Deque[int]: 
    #intialise a deque represeting a queue 
    queue = deque()
    for instruction in program: 
        if instruction == "peek": 
            #print out the first item in the queue if it is not empty 
            #print out a warning message if the queue is empty 
            print(queue[0]) if queue else print ("Queue is empty!")
        elif instruction == "pop": 
            #check if the queue is empty 
            if queue: 
               #pop the first item in queue 
               queue.popleft()
            else: 
               #print message if queue is empty
               print("Queue is empty!")
        else: 
            #get the data in the "push" instruction 
            data = int(instruction[5:])
            #push data to the end of the queue 
            queue.append(data)
        return queue
    if __name__ == '__main__':