from collections import deque

dial = deque(range(100)) # circular queue from 0 to 99
dial.rotate(50) # start at 50

def incr(steps): # move clockwise
    pos = dial[0] # current position

    t0 = (-pos)%100 # steps to next 0
    if t0 == 0:
        t0 = 100 # if already at 0, next 0 is in 100 steps
    hits = 0 if steps < t0 else 1 + (steps - t0)//100 # count hits using floor division

    dial.rotate(-steps) # move
    return dial[0], hits

def decr(steps): # move counter-clockwise
    pos = dial[0]

    t0 = pos%100
    if t0 == 0:
        t0 = 100
    hits = 0 if steps < t0 else 1 + (steps - t0)//100

    dial.rotate(steps)
    return dial[0], hits


count = 0 # count of zeros hit initialized to 0

with open('day1-input', 'r', encoding='utf-8') as f: # read input file
    for line in f:
        line = line.rstrip('\n') # strip newline
        if line.startswith('L'): # left L means counter-clockwise
            val, hits = decr(int(line[1:]))
            print(f"Current Val: {val}")
            print(f"Zero Hits: {hits}")            
            count += hits

        elif(line.startswith('R')): # right R means clockwise
            val, hits = incr(int(line[1:]))
            print(f"Current Val: {val}")
            print(f"Zero Hits: {hits}")
            count += hits

        else:
            continue

    
    print(f"Number of Zeros: {count}") # print total count of zeros hit which is the password