## 다음과같은 숫자로 이루어진 배열이 있을때, 이배열 내에 특정 숫자가
## 존재한다면 True , 존재하지 않는다면 False를 반환해라.

input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for element in array:    #array의 길이만큼 아래 연산 실행
        if number == element: # 비교연산 1번 실행
            return True  # N * 1 정도의 시간 복잡도 사용
    return False


result = is_number_exist(3, input)
print(result)

# 알고리즘은 입력값에 따라 입력값의 분포에 따라 성능이 변화할수 있다.
# 예를 들어 지금의 경우 3이 맨앞이라 한번에 찾았지만 만약 맨뒤였을 경우에는
# for문을 다 돌아야 찾을수 있기 때문에

