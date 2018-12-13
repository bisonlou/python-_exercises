number_list = []
for number in range(2000,3201):
    if(number%7 == 0) and (number%5 == 1):
        number_list.append(number)
print(','.join(map(str,number_list)))
