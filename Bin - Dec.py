import time

while True:                                                             #Run the conversion in a loop

    while True:                                                         #Check what to convert
        user_input = input("Convert Dec to Bin [DB], Convert Bin to Dec [BD], Exit [X]: ")
        if user_input == ("DB"):
            break
        if user_input == ("BD"):
            break
        if user_input == ("X"):
            break
        if user_input != ("DB", "BD", "X"):
            print("Type 'DB' or 'BD' ot 'X' !")
        continue

    if user_input == ("X"):                                             #Exit Timer
            print("Exit in 3 ...")
            time.sleep(0.5)
            print("Exit in 2 ...")
            time.sleep(0.5)
            print("Exit in 1 ...")
            time.sleep(0.5)
            print("Exeting ...")
            time.sleep(0.5)
            quit()

    if user_input == ("DB"):                                            #If DB, Check DB input_dec is an int, convert dec to bin
        while True:
            input_dec = int(input("Decimal number: "))
            try:
                int(input_dec)
                break
            except ValueError:
                print("Please enter a valid decimal number: ")
                continue
        

        def output_bin(input_dec):
            return bin(input_dec).replace("0b", "")
        if __name__ == '__main__':
            print("Decimal:", input_dec, "=", "Binary:", output_bin(input_dec))    

    if user_input == ("BD"):                                            #If BD, Check BD input_bin is an int, convert bin to dec
        bin_didget = {'0','1'}
        while True:
            input_bin = input("Binary number: ")        
            var_ib = set(input_bin)
            if bin_didget == var_ib or var_ib == {'0'} or var_ib == {'1'}:
                break
            else:
                print("Please enter a valuable Binary number")
                continue
        output_dec = int(input_bin, 2)
        print("Binary:", input_bin, "=", "Decimal:", output_dec)

    continue