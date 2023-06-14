n = int(input())

start_index = 1  # 인덱스 값
sum = 1
end_index = 1
count = 1  # 15인 경우의 수를 미리 넣어줌

while 1:
    if n == end_index:  # 인덱스가 15가 되면 끝 = while(end_index !=n)
        break

    elif sum == n:  # 합친 값이 15가 되면!
        count += 1  # 경우의 수 +1
        end_index += 1  # index인  경우의 수는 확인했으니 +1로 다음 인덱스 기준으로!
        sum += end_index  # 합친 값 초기화
    elif sum > n:  # 값을 넘어간 경우 -> 여기서 나올 수 있는 경우는 없음
        sum -= start_index
        start_index += 1
    elif sum < n:  # 목표값 되려면 아직 멀었음
        sum += end_index
        end_index += 1

print(count)
