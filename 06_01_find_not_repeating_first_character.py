input = "abadabac"


def find_not_repeating_first_character(string):
    alphabet_occurrence_array = [0] * 26   #문자열을 입력받아 alphabet_occurrence_array 에 하나하나 추가해  나가는 과정
                                          # 0에는 a , 25번째에는 z의 빈도수로 지정해 저장해주는 배열
    for char in string:  # 문자 배열에 하나하나 돌면서
        if not char.isalpha(): #알파벳이 아니면 버리고
            continue
        arr_index = ord(char) - ord("a") #알파벳이면 ord를 통해 변환함
        alphabet_occurrence_array[arr_index] += 1 #그래서 하나씩 추가

    not_repeating_character_array = []  #반복되지 않는걸 찾기 위해 변수 선언
    for index in range(len(alphabet_occurrence_array)): #알파벳의 길이만큼 반복
        alphabet_occurrence = alphabet_occurrence_array[index] #array의 index의 값을 occurrence에 저장

        if alphabet_occurrence == 1: #만약 1일경우
            not_repeating_character_array.append(chr(index + ord("a"))) #해당 알파벳을 넣어줘라
    ##print(not_repeating_character_array) #<- 이렇게 선언할 경우 기존 순서가 아닌 배열에 저장된 abcd...이순에서 꺼내오기때문에 순서배열에
    # 영향을 주지 않는다.

    for char in string: #입력한 문자열을 대상으로 반복문을 다시 돌려야한다.
        if char in not_repeating_character_array: #현재 들어온 문자를 바로 반환해라
            return char


    return "_"


result = find_not_repeating_first_character(input)
print(result)

# 시간 복잡도는 얼마나 걸리나?

# O(n)만큼 걸린다.함수 구문 하나하나를 보지 않더라도, 1차 반복문이 나왔고,
# array 의 길이 만큼 반복한다? 그러면 O(N) 으로 봐도 무방하다.