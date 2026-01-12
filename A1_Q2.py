def decimal_to_binary(num):
    if num == 0:
        print(f"You have entered number 0\nIts binary is 0")
        return
    bin_str = []
    bin_int_inverse = []
    while num > 0:
        a = num % 2
        num = num // 2
        bin_int_inverse.append(a)
        bin_str.insert(0, str(a))
    print (f"\nYou got binary number {''.join(bin_str)}")
    n = 0
    k = 0
    for j in bin_int_inverse:
        n += j * (2**k)
        k += 1
    print (f"From the decimal number {n}")

def decimal_to_hexadecimal(num):
    if num == 0:
        print(f"You have entered number 0\nIts hexadecimal is 0")
        return
    hex = []
    hex_num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    while num > 0:
        a = num % 16
        num = num // 16
        hex.insert(0, hex_num[a])
    print(f"\nYou got a hexadecimal number {''.join(hex)}")
    n = 0
    k = 0
    inv_hex = []
    for x in hex:
        inv_hex.insert(0, x)

    for j in inv_hex:
        l = hex_num.index(j)
        n += l * (16**k)
        k += 1
    print (f"From the decimal number {n}")


request = input ("What type of convertion do you need? (BIN - decimal to binary, HEX - deciaml to hexadecimal)?")
if request != "BIN" and request!= "HEX":
    request = input ("INPUT BIN OR HEX: ")
num = int(input("Input a positive integer: "))
if request == "BIN":
    decimal_to_binary(num)
else:
    decimal_to_hexadecimal(num)
