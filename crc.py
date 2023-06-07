def calculate_crc(dataword, divisor):
    dividend = dataword + "0" * (len(divisor) - 1)
    remainder = ""
    while len(dividend) >= len(divisor):
        if dividend[0] == "1":
            dividend = "".join(str(int(dividend[i]) ^ int(divisor[i])) for i in range(len(divisor))) + dividend[len(divisor):]
            # print(dividend)
        else:
            dividend = dividend[1:]
    remainder = dividend
    codeword = dataword + remainder
    return codeword

def check_crc(codeword, divisor):
    dividend = codeword
    while len(dividend) >= len(divisor):
        if dividend[0] == "1":
            dividend = "".join(str(int(dividend[i]) ^ int(divisor[i])) for i in range(len(divisor))) + dividend[len(divisor):]
        else:
            dividend = dividend[1:]
    return dividend == "0"

# Example usage:
dataword = "1011101"
divisor = "1101"
codeword = calculate_crc(dataword, divisor)
print("CRC Codeword:", codeword)

corrupted_codeword = "101111100"
is_corrupted = check_crc(corrupted_codeword, divisor)
print("Is Codeword Corrupted?", is_corrupted)
