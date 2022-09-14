months=["january","february","march","april","may","june","july","august","september","october","november","december"]
print("list of months:",months)
print("input the name of month:")
month=str(input())
if (month.lower() in months):
    if(month== "january" or month=="march" or month=="may" or month=="july" or month=="august" or month=="october" or month=="december"):
        print(" No. of days: 31")
    elif (month==" february"):
        print(" No. of days: 28/29")
    else:
        print(" No. of days: 30")
else:
    print("such month does not exist")