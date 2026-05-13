def solution(tickets):
    answer = ["ICN"]
    used=[False]*len(tickets)
    tickets.sort(key=lambda x : x[1])
    def DFS(current_airport, used):
        if len(answer) == len(tickets)+1:
            return True
        for i,(a,b) in enumerate(tickets):
            if a==current_airport and used[i]==False:
                answer.append(b)
                used[i]=True
                if DFS(b,used):
                    return True
                else:
                    answer.pop()
                    used[i]=False
    DFS("ICN",used)
    return answer