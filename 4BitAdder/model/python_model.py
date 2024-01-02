def Bit4Adder_python_model(A: int, B: int, Carry_in: int) -> tuple[int, int]:
    # Convert the integers to binary strings
    A = format(A, '04b')
    B = format(B, '04b')
    Carry_in = format(Carry_in, '01b')

    # Initializing
    Sum = ''
    Carry_out = 0

    # Loop through each bit and perform the addition
    for i in range(3, -1, -1):
        # Calculate the sum of the bits
        bit_sum = int(A[i]) + int(B[i]) + Carry_out

        # Calculate the carry out
        if bit_sum > 1:
            Carry_out = 1
        else:
            Carry_out = 0

        # Calculate the sum bit
        Sum = str(bit_sum % 2) + Sum

    # Convert the binary strings to integers
    Sum = int(Sum, 2)
    Carry_out = int(Carry_out)

    return Sum, Carry_out
