while True:
    user_input = input("Dez2Bin (DB); Bin2Dez (BD): ")
    if user_input == ("DB"):
        print("Dez to Bin: ")
        break
    if user_input == ("BD"):
        print("Bin to Dez: ")
        break
    if user_input != ("DB", "BD"):
        print("Type 'DB' or 'BD':")
    continue

if user_input == ("DB"):
    while True:
        input_dez = input("Decimal number: ")
        try:
            int(input_dez)
            break
        except ValueError:
            print("Please enter a valid decimal number: ")
            continue

if user_input == ("BD"):
    while True:
        input_dez = input("Binary number: ")
        try:
            int(input_dez)
            break
        except ValueError:
            print("Please enter a valid binary number: ")
            continue