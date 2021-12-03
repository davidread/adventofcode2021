import numpy

def power(rows_str):
    # count 1s in each column
    cols = len(rows_str[0])
    column_totals = numpy.array([0] * cols)
    rows_array = [numpy.array([int(bit) for bit in row_str])
                  for row_str in rows_str]
    for row_array in rows_array:
        column_totals = \
            numpy.add(row_array, column_totals)
        print(row_array, column_totals)
    
    # work out the most common bit for each column
    rows = len(rows_str)
    half_nums = rows // 2  # rounds down
    print(f'{len(nums)} // 2 = {half_nums}')
    most_common = ''.join(['1' if total > half_nums else '0'
                           for total in column_totals])
    gamma = int(most_common, 2)
    print('gamma rate (most common):', most_common, gamma)

    # least common - get by inverting the most common, by xor with 11111
    ones = pow(2, cols) - 1  # 11111 = 31
    epsilon = numpy.bitwise_xor(ones, gamma)
    print('epsilon rate (least common):', format(epsilon, 'b'), epsilon)

    power = gamma * epsilon
    print(f'power consumption: {power}')

    # oxygen - search for the longest match for gamma
    longest_match_length = 0
    longest_match_row = None
    for row_str in rows_str:
        # row:   101001
        # gamma: 101100
        # xor:   000101
        # i.e. XOR shows the differences
        # So to find the first difference, find the first '1' in the XOR
        row_dec = int(row_str, 2)
        differences = numpy.bitwise_xor(row_dec, gamma)
        len_of_matching_prefix = format(differences, 'b').find('1')
        if len_of_matching_prefix > longest_match_length:
            longest_match_length = len_of_matching_prefix
            longest_match_row = row_dec
        

    return gamma, epsilon, power

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        nums = [line.strip() for line in f]
    power(nums)