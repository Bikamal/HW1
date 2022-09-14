month_numb=int(input())
day=int(input())
if(day<1 or day>32):
    print("such day does not exist")

if(month_numb==1):
    month="January"
elif(month_numb==2):
    month="February"
elif(month_numb==3):
    month="March"
elif(month_numb==4):
    month="April"
elif(month_numb==5):
    month="May"
elif(month_numb==6):
    month="June"
elif(month_numb==7):
    month="July"
elif(month_numb==8):
    month="August"
elif(month_numb==9):
    month="September"
elif(month_numb==10):
    month="October"
elif(month_numb==11):
    month="November"
elif(month_numb==12):
    month="December"


if (month=="December" or month=="January" or month=="February" ):
    season="Winter"
elif(month=="March" or month=="April" or month=="May" ):
    season="Spring"
elif(month=="June" or month=="July" or month=="August" ):
    season="Summer"
else:
    season="Autumn"


print(month,',',day,'. Season is:', season)




