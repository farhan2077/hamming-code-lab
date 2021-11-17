"""
dw = data word or data code or message bit
p1, p2, p4, p8 = parity bit
gcw = generated code word
rcw = received code word
"""
import os

os.system('cls')

print("Hamming code generation, error dectection & correction.\n")

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

    # print("Parity bits", p1, p2, p4, p8)

    # generate code word
    gcw = dw_list[0] + dw_list[1] + dw_list[2] + \
        str(p8) + dw_list[3] + dw_list[4] + dw_list[5] + \
        str(p4) + dw_list[6] + str(p2) + str(p1)
    return gcw


gcw = generate_codeword(dw)
print("Complete code word →", gcw, "\n")

rcw = str(input("Enter the the received code word: "))
# rcw = str(11110101011)


# calculate hamming distance
def check_error(gcw, rcw):
    errors = 0
    error_pos = []

    for i in range(len(rcw)):
        if rcw[i] != gcw[i]:
            errors += 1
            error_pos.append(i)
            error_pos = error_pos
    return errors, error_pos


errors, error_pos = check_error(gcw, rcw)
if errors > 0:
    print("Error at", error_pos[0]+1, "position")
else:
    print("No error in received codeword")

print("Corrected code word →", gcw)
