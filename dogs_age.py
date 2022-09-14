print(" input a dog's age in human years:")
human_year=int(input())

if(human_year<=2):
    dogs_age=human_year * 10.5
else:
    dogs_age=21+(human_year-2)*4

print("The dog's age in dog's years is:" ,dogs_age)