###################
#algorithm 1 complete digest
def complete_digest(listt):
    new_list=[]
    for i in range(1,len(listt),1):
        new_list.append(listt[i]-listt[i-1])
    return new_list

print(complete_digest([0,2,4,7,10]))
def partial_digest(listt):
    result=[]
    for i in range(len(listt)):
        for j in range(i+1,len(listt)):
            result.append(abs(listt[i]-listt[j]))
    return result

print(partial_digest([0,2,4,7,10]))
