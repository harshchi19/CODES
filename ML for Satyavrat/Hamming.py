def calculate_parity_bits(data, parity_bits):
    """Calculate the parity bits for the given data."""
    n = len(data)
    codeword = list('0' * (n + len(parity_bits)))
    
    # Place data bits in codeword
    j = 0
    for i in range(1, len(codeword) + 1):
        if i not in parity_bits:
            codeword[-i] = data[-j - 1]
            j += 1
    
    # Calculate parity bits
    for i, pos in enumerate(parity_bits):
        parity = 0
        for j in range(1, len(codeword) + 1):
            if (j & pos) and j != pos:
                parity ^= int(codeword[-j])
        codeword[-pos] = str(parity)
    
    return ''.join(codeword)

def detect_error(codeword, parity_bits):
    """Detect if there is an error in the received codeword."""
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
    """Correct an error in the codeword if detected."""
    if error_pos == 0:
        return codeword
    corrected_codeword = list(codeword)
    corrected_codeword[len(codeword) - error_pos] = str(1 - int(codeword[len(codeword) - error_pos]))
    return ''.join(corrected_codeword)

if __name__ == "__main__":
    # User input for data
    data = input("Enter binary data to send: ")
    parity_positions = [1, 2, 4]  # Adjust based on the size of the data
    codeword = calculate_parity_bits(data, parity_positions)
    print("Generated codeword to send:", codeword)

    # Simulate receiving codeword (possibly with errors)
    received_codeword = input("Enter received codeword (simulate errors if any): ")
    error_pos = detect_error(received_codeword, parity_positions)

    if error_pos:
        print("Error detected at position:", error_pos)
        corrected_codeword = correct_error(received_codeword, error_pos)
        print("Corrected codeword:", corrected_codeword)
    else:
        print("No error detected. Codeword is correct.")
