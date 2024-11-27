def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")
    return sum(bit1 != bit2 for bit1, bit2 in zip(str1, str2))


def detect_error(codeword, parity_bits):
    error_pos = 0
    for i, pos in enumerate(parity_bits):
        parity = 0
        for j in range(1, len(codeword) + 1):
            if (j & (1 << i)) and j != pos:
                parity ^= int(codeword[len(codeword) - j])
        if parity != int(codeword[len(codeword) - pos]):
            error_pos += pos
    return error_pos

def correct_error(codeword, error_pos):
    if error_pos == 0:
        return codeword
    corrected_codeword = list(codeword)
    corrected_codeword[len(codeword) - error_pos] = str(1 - int(codeword[len(codeword) - error_pos]))
    return ''.join(corrected_codeword)


if __name__ == "__main__":
    str1 = input("Enter first binary string: ")
    str2 = input("Enter second binary string: ")
    print("Hamming distance:", hamming_distance(str1, str2))

    codeword = input("Enter received codeword: ")
    parity_bits = [1, 2, 4]  # Can be adjusted as needed
    error_pos = detect_error(codeword, parity_bits)

    if error_pos:
        print("Error detected at position:", error_pos)
        print("Corrected codeword:", correct_error(codeword, error_pos))
    else:
        print("No error detected.")
