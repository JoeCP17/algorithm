def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for alphabet in string:
        if not alphabet.isalpha():
            continue
        arr_index = ord(alphabet) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        # index 0 -> alphabet_occurrence 3
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence
    print(max_alphabet_index)
    return chr(max_alphabet_index+ord("a"))


print(find_alphabet_occurrence_array("hello my name is sparta"))