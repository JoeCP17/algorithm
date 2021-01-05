##Q. 다음과 같이 0 혹은 양의 정수로만 이루어진 배열이 있을 때,
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 '✕' 혹은 '+' 연산자를
# 넣어 결과적으로 가장 큰 수를 구하는 프로그램을 작성하시오.

##단, '+' 보다 '✕' 를 먼저 계산하는 일반적인 방식과는 달리,
# 모든 연산은 왼쪽에서 순서대로 이루어진다.

#Facebook code test

input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    multiply_sum = 0 #변수선언 1회
    for num in array:  #input으로 들어온 array값을 하나하나 계산   #반복문 N
        if num <= 1 or multiply_sum <=1:  #<- multiply_sum <=1을 해주는 이유도 위 0으로 선언을했기때문에 이또한 생각을해야한다.
            #조건문 1회
            multiply_sum += num #대입 연산 1회
        else: #조건문 1회
            multiply_sum *= num #대입 연산 1회

    return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)

# Quiz 여기에 시간 복잡도는 얼마일까?
# 3N+1 즉 시간 복잡도는 O(N)