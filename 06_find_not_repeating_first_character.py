#다음과 같이 영어로 되어 있는 문자열이 있을 때,
# 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오.
# 만약 그런 문자가 없다면 _ 를 반환하시오. (응용)

input = "abadabac"

def find_not_repeating_character(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "x", "y", "z"]     # 각각의 배열을 설정

    min_occurrence = 1                             # 최소 occurrence를 비교할 1을 설정
    min_alphabet = alphabet_array[0]               # 각각 최소 공간을 담을 배열 설정

    for alphabet in alphabet_array:  #alphabet_array라는 배열 만큼 반복한다.
        occurrence = 0               #occurrence를 선언후 0으로 초기화 한후
        for char in string:          # 다시한번 문자열을 반복했을때
            if char == alphabet:     # char 그리고 alphabet이 서로 같다면
                occurrence += 1      # occurrence 에 1씩을 추가 해줘라
                                     # 이렇게 될시 해당되는 위치에 1씩 추가가 들어가게된다
                #<빈도수 비교>
                #<최소 빈도수 가져오기 >
        if occurrence == min_occurrence:  #최소의 경우 1만있는것을 가져와야하므로 1로지정해뒀던 min_occurrence를 비교
            min_alphabet = alphabet  # 조건문이 맞을시 해당 알파벳을 넣고
            min_occurrence = occurrence # 값또한 넣어준다

    return min_alphabet #필요한건 알파벳이므로 알파벳을 가져와






result = find_not_repeating_character(input)
print(result) #출력한다.