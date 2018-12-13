def squares():
    square_list = []
    for number in range(1,21):
        square_list.append(number**2)
    return square_list[:5]

if __name__ == "__main__":
    print(','.join(map(str,squares())))
