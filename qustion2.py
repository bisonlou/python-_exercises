def capitalise_input(sentence_list):
    capitalised_output = []
    for sentence in sentence_list:
        capitalised_output.append(sentence.upper())

    return capitalised_output

if __name__ == "__main__":
    input_count = int(input())
    sentence_list = []
    for i in range(input_count):
        sentence_list.append(str(input()))

    print('\n'.join(map(str,capitalise_input(sentence_list))))
