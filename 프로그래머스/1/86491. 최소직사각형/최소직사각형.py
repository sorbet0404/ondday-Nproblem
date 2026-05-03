def solution(sizes):
    answer = 0
    new_sizes=[]
    max_w=0
    max_h=0
    for i in sizes:
        if i[0]>i[1]:
            new_sizes.append(i)
        else:
            new_sizes.append([i[1],i[0]])
    for j in new_sizes:
        if j[0]>=max_w:
            max_w=j[0]
        if j[1]>=max_h:
            max_h=j[1]
    return max_w*max_h