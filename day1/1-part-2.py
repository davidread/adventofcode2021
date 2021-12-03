from collections import deque 

depth_increase_count = 0

with open('1-input.txt', 'r') as f:
    window = deque([int(f.readline()), int(f.readline()), int(f.readline())])
    print(window, '-')

    for line in f:
        depth_leaving_window = window.popleft()
        depth_joining_window = int(line)
        window.append(depth_joining_window)
        if depth_joining_window > depth_leaving_window:
            depth_increase_count += 1
            print(depth_joining_window, 'increase')
        else:
            print(depth_joining_window, '-')

print('Depth increases:', depth_increase_count)
# runtime: O(n)
# memory: O(1)