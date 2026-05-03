def solution(answers):
    answer = []
    aa=0
    bb=0
    cc=0
    count=0
    person=1
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    for i in answers:
        if i==a[count%5]:
            aa+=1
        if i==b[count%8]:
            bb+=1
        if i==c[count%10]:
            cc+=1
        count= count+1
    max_stat=max(aa,bb,cc)
    for i in [aa,bb,cc]:
        if i == max_stat:
            answer.append(person)
        person+=1
    return sorted(answer)