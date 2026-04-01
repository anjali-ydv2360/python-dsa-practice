a = int(input("Enter the number of days: "))
daymap={}
daymap["sunday"]=0
daymap["monday"]=6
daymap["tuesday"]=5
daymap["wednesday"]=4
daymap["thursday"]=3
daymap["friday"]=2
daymap["saturday"]=1
s=input("enter the day: ")
sun_count=0
if(a-daymap[s]>1):
    sun_count=1+(a-daymap[s])//7
print(sun_count)