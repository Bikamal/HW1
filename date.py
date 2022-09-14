year=int(input())
day=int(input())
month=int(input())
if (month!=2 and (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12)):
    if(day<31 and month <12):
        day=day +1 
    elif(day>=31 and month<12):
        day=1
        month=month+1
    elif(day>=31 and month>=12):
        day=1
        month=1
        year+=1
elif(month==2):
    if(day<28):
        day+=1
    elif(day>28):
        month+=1
elif(month==4 or month==6 or month==9 or month==11):
    if(day<30 and month <12):
        day=day +1 
    elif(day>=30 and month<12):
        day=1
        month=month+1
    elif(day>=30 and month>=12):
        day=1
        month=1
        year+=1
print("The next date is",year,'-',month,'-',day)
