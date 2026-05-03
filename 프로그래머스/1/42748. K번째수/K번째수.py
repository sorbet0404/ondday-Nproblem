def solution(array, commands):
    answer = []
    for i in commands:
        l=i[0]
        m=i[1]
        n=i[2]
        new_array=sorted(array[l-1:m])
        answer.append(new_array[n-1])
    return answer