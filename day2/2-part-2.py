horizontal_position = depth = aim = 0
with open('2-input.txt', 'r') as f:
    for line in f:
        action, value = line.split()  # e.g. line = 'forward 5'
        value = int(value)

        if action == 'forward':
            horizontal_position += value
            depth += aim * value
        elif action == 'up':
            aim -= value
        elif action == 'down':
            aim += value
        print(line, f'horizontal: {horizontal_position} aim: {aim} depth: {depth}')

print(f'h * d = {horizontal_position * depth}')