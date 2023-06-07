def calculate_even_parity(dataword):
    parity_bit = 0
    for bit in dataword:
        parity_bit ^= int(bit)  # XOR operation to calculate parity bit
    # print('Parity bit is: ' + str(parity_bit))
    return dataword + str(parity_bit)

def check_codeword_parity(codeword):
    parity_bit = int(codeword[-1])  # Get the last bit (parity bit)
    dataword = codeword[:-1]  # Remove the parity bit
    expected_parity_bit = calculate_even_parity(dataword)[-1]  # Calculate the expected parity bit
    return parity_bit == int(expected_parity_bit)

# 11010
dataword = input('Enter the dataword: ')
codeword = calculate_even_parity(dataword)
print("Even Parity Codeword:", codeword)

corrupted_codeword = "110011"  # Adding an error by changing a bit
is_corrupted = check_codeword_parity(corrupted_codeword)
print("Is Codeword Corrupted?", is_corrupted)
