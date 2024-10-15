def invert(number:int):
    answer=str(number)[::-1]
    if answer[-1]=='-':
        answer='-'+answer[:-1]
        if int(answer)<-pow(2,31):
            return 0
    elif int(answer)>1+pow(2,31):
        return 0
    return int(answer)
print (invert(123))