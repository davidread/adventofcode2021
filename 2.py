horizontal_position = depth = 0
with open('2-input.txt', 'r') as f:
    for line in f:
        action, value = line.split()  # e.g. line = 'forward 5'
        value = int(value)
        if action == 'forward':
            horizontal_position += value
        elif action == 'up':
            depth -= value
        elif action == 'down':
            depth += value
        print(line, f'horizontal: {horizontal_position} depth: {depth}')
print(f'h * d = {horizontal_position * depth}')