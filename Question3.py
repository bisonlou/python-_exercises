def filter_multiles_of_five(binary_list):
    multiples_of_five = []
    for binary in binary_list:
        bin_to_int = int(binary,2)
        if(bin_to_int%5 == 0):
            multiples_of_five.append(bin_to_int)
    
    return multiples_of_five

if __name__ == "__main__":
    binary_list = input("Enter binaries separated by a comma").split(',')

    print(','.join(map(str,filter_multiles_of_five(binary_list))))
