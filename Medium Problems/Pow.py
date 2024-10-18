def Pow(x,n):
    neg=1
    ans=1
    temp=0
    if x<0 and n%2:
        neg=-1
        x=-x
    if x==1:
        return x*neg
    for sub in range(n):
        ans=ans*x
        if ans<0.000005:
          return 0
    for sub in range(-n):
        if round(ans-temp,5)==0:
            break
        temp=ans
        ans=ans/x
    return round(ans*neg,5)
