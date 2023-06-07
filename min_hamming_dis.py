def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        print("The two strings must have the same length.")
        return
    return sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))

def minimum_hamming_distance(codewords):
    min_distance = float('inf')
    for i in range(len(codewords)):
        for j in range(i + 1, len(codewords)):
            distance = hamming_distance(codewords[i], codewords[j])
            if distance < min_distance:
                min_distance = distance
    return min_distance


# sample input 
# 110000,001100,000011,111111
array_input = input('Enter the numbers of codewords with comma separated: ')
codewords = array_input.split(',')
min_distance = minimum_hamming_distance(codewords)
print("Minimum Hamming distance:", min_distance)
