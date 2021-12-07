from collections import Counter


def day(fishes):
    # store *counts* of fishes at each timer value
    # (the alternative is to store a timer per fish, which doesn't scale)
    out = Counter()
    for timer, count in dict(fishes).items():
        if timer == 0:
            out.update({6: count, 8: count})
        else:
            out.update({timer - 1: count})

    # print(out)
    return out

def breeding(initial_fish_timer_counts, num_days):
    total_fish_at_end = 0
    for timer, fish_count in initial_fish_timer_counts:
        total_fish_at_end += 2 ** (num_doublings(timer, num_days) - 1)
    return total_fish_at_end

def num_doublings(timer, num_days):
    return (num_days - 6) // 8

def line_to_counts(line):
    return Counter(int(num) for num in line.split(','))


if __name__ == '__main__':
    input = '3,4,1,1,5,1,3,1,1,3,5,1,1,5,3,2,4,2,2,2,1,1,1,1,5,1,1,1,1,1,3,1,1,5,4,1,1,1,4,1,1,1,1,2,3,2,5,1,5,1,2,1,1,1,4,1,1,1,1,3,1,1,3,1,1,1,1,1,1,2,3,4,2,1,3,1,1,2,1,1,2,1,5,2,1,1,1,1,1,1,4,1,1,1,1,5,1,4,1,1,1,3,3,1,3,1,3,1,4,1,1,1,1,1,4,5,1,1,3,2,2,5,5,4,3,1,2,1,1,1,4,1,3,4,1,1,1,1,2,1,1,3,2,1,1,1,1,1,4,1,1,1,4,4,5,2,1,1,1,1,1,2,4,2,1,1,1,2,1,1,2,1,5,1,5,2,5,5,1,1,3,1,4,1,1,1,1,1,1,1,4,1,1,4,1,1,1,1,1,2,1,2,1,1,1,5,1,1,3,5,1,1,5,5,3,5,3,4,1,1,1,3,1,1,3,1,1,1,1,1,1,5,1,3,1,5,1,1,4,1,3,1,1,1,2,1,1,1,2,1,5,1,1,1,1,4,1,3,2,3,4,1,3,5,3,4,1,4,4,4,1,3,2,4,1,4,1,1,2,1,3,1,5,5,1,5,1,1,1,5,2,1,2,3,1,4,3,3,4,3'
    fishes = line_to_counts(input)
    for i in range(80):
        fishes = day(fishes)
    print('After 80 days: ', fishes.total())

    for i in range(256 - 80):
        fishes = day(fishes)
    print('After 256 days: ', fishes.total())
