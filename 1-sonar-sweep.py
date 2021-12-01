with open('1-input.txt', 'r') as f:
    depth_increase_count = 0
    depth = int(f.readline())
    print(depth, '-')

    for line in f:
        prev_depth = depth
        depth = int(line)
        if depth > prev_depth:
            depth_increase_count += 1
            print(depth, 'increase')
        else:
            print(depth, '-')

print('Depth increases:', depth_increase_count)
