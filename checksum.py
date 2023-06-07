def calculate_checksum(numbers):
    binary_sum = binary_add(numbers)  # Perform binary addition on all numbers
    binay_sum_8_bit = format(int(binary_sum, 2), '08b')
    checksum = ones_complement(binay_sum_8_bit)
    return checksum

def check_checksum(numbers, checksum):
    binary_sum = binary_add(numbers)  # Perform binary addition on all numbers
    binay_sum_8_bit = format(int(binary_sum, 2), '08b')
    print(binay_sum_8_bit)
    pre_result = binary_add([binay_sum_8_bit, checksum])
    result = ones_complement(pre_result)
    return result == '00000000'

def binary_add(args):
    result = format(sum(int(num, 2) for num in args), 'b')
    if(len(result) > 8):
        sub1_res = result[:-8]
        sub2_res = result[-8:]
        return binary_add([sub1_res, sub2_res])
    return result

def ones_complement(binary):
    ones_comp = ''.join('1' if bit == '0' else '0' for bit in binary)
    return ones_comp

# Example usage:
numbers = ['01100101', '10101010', '11001100', '00110011', '01010101']
# numbers = [7, 11, 12, 0, 6]
checksum = calculate_checksum(numbers)
print("Checksum Codeword:", checksum)

corrupted_numbers = ['01100101', '10101010', '11001101', '00110011', '01010101']
isCorrupted = check_checksum(corrupted_numbers, checksum)
print("Is Codeword Corrupted?", not isCorrupted)


'''
01100101
10101010
11001100
00110011
01010101
------------
01100011
      10
------------
01100101
1's compliment
10011010
'''