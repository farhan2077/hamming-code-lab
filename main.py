"""
dw = data word or data code or message bit
p1, p2, p4, p8 = parity bit
gcw = generated code word
rcw = received code word
cwc = corrected code word
"""
import os

os.system('cls')

print("∎ Hamming code generation, error dectection & correction ∎")
print("⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅")
print("Choose any option form below ↓\n")
option = int(input(
    '[1] Generate hamming code\n[2] Find error in received code word\n\nEnter you option: '))
print("⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅")

if option == 1:
    dw = str(input("Enter the 7-bit data word: "))
    # dw = str(1110100)

    def generate_codeword(dw):
        # convert int number to a list
        dw_list = [x for x in dw]

        # generate parity bits
        p1 = int(dw_list[6]) ^ int(dw_list[5]) ^ int(
            dw_list[3]) ^ int(dw_list[2]) ^ int(dw_list[0])

        p2 = int(dw_list[6]) ^ int(dw_list[4]) ^ int(
            dw_list[3]) ^ int(dw_list[1]) ^ int(dw_list[0])

        p4 = int(dw_list[5]) ^ int(dw_list[4]) ^ int(dw_list[3])

        p8 = int(dw_list[2]) ^ int(dw_list[1]) ^ int(dw_list[0])

        # generate code word
        gcw = dw_list[0] + dw_list[1] + dw_list[2] + \
            str(p8) + dw_list[3] + dw_list[4] + dw_list[5] + \
            str(p4) + dw_list[6] + str(p2) + str(p1)
        return gcw

    gcw = generate_codeword(dw)
    print("\nComplete code word →", gcw,)
    print("⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅")

elif option == 2:
    rcw = str(input("Enter the the received code word: "))
    # rcw = str(11110101011)
    # rcw = str(10001101100)

    def check_error_index(rcw):
        rcw_list = [x for x in rcw]
        errors = "NO"
        error_pos = ""

        # generate parity bits
        p1 = int(rcw_list[10]) ^ int(rcw_list[8]) ^ int(
            rcw_list[6]) ^ int(rcw_list[4]) ^ int(rcw_list[2]) ^ int(rcw_list[0])

        p2 = int(rcw_list[9]) ^ int(rcw_list[8]) ^ int(
            rcw_list[5]) ^ int(rcw_list[4]) ^ int(rcw_list[1]) ^ int(rcw_list[0])

        p4 = int(rcw_list[7]) ^ int(rcw_list[6]) ^ int(
            rcw_list[5]) ^ int(rcw_list[4])

        p8 = int(rcw_list[3]) ^ int(rcw_list[2]) ^ int(
            rcw_list[1]) ^ int(rcw_list[0])

        parity = str(p8)+str(p4)+str(p2)+str(p1)

        if parity == "0000":
            error_index = 0  # error_pos = 0
        elif parity == "0001":
            error_index = 10  # error_pos = 1
        elif parity == "0010":
            error_index = 9  # error_pos = 2
        elif parity == "0011":
            error_index = 8  # error_pos = 3
        elif parity == "0100":
            error_index = 7  # error_pos = 4
        elif parity == "0101":
            error_index = 6  # error_pos = 5
        elif parity == "0110":
            error_index = 5  # error_pos = 6
        elif parity == "0111":
            error_index = 4  # error_pos = 7
        elif parity == "1000":
            error_index = 3  # error_pos = 8
        elif parity == "1001":
            error_index = 2  # error_pos = 9
        else:  # parity == 1010
            error_index = 1  # error_pos = 10

        return error_index

    error_index = check_error_index(rcw)

    def correct_error(rcw, error_index):
        if error_index == 0:
            print("\nNo Error in received codeword")
        else:
            print("\nError in", error_index+1, "position")

            first_part = rcw[slice(error_index)]
            middle_part = rcw[error_index]
            last_part = rcw[slice(error_index+1, len(rcw), 1)]

            if middle_part == "0":
                changed_bit = "1"
            else:
                changed_bit = "0"

            cwc = first_part+changed_bit+last_part
            return print("Corrected code word →", cwc)

    cwc = correct_error(rcw, error_index)
    print("⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅")

else:
    print("Your entered option doesn't exist. Try again.")
    print("⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅")
