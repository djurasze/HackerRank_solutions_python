def flippingBits(n):
    binary_16bit = format(n, '032b')
    binary_16bit = ''.join(['1' if el=='0' else '0' for el in binary_16bit])
    decimal_n = int(binary_16bit,2)
    return decimal_n

# def flippingBits(n):
#
#     # this number is (2**32)-1
#     # unsigned integers given which is 32
#     # 2**32 = 4294967296
#     # to flip is to just minus 1
#     THE_FLIPPING = 4294967295
#
#     # ^ = bitwise XOR
#     return n ^ THE_FLIPPING

if __name__ == '__main__':
    f = open("data.txt", "r")

    q = int(f.readline().strip())

    for q_itr in range(q):
        n = int(f.readline().strip())

        result = flippingBits(n)

        print(result)

    f.close()
