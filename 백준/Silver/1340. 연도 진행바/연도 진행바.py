import sys
import re

line = sys.stdin.readline().strip()

ss = re.split(r'[ ,:]+', line)

#print(ss)

month = {
    "January" : 1, 
    "February" : 2, 
    "March" : 3, 
    "April" : 4, 
    "May" : 5, 
    "June" : 6, 
    "July" : 7, 
    "August" : 8, 
    "September" : 9, 
    "October" : 10, 
    "November" : 11, 
    "December" : 12
}



if int(ss[2]) % 400 == 0:
    #윤년
    minute = 366 * 24 * 60
elif int(ss[2]) % 4 == 0 and int(ss[2]) % 100 != 0:
    minute = 366 * 24 * 60
    #윤년
else:
    minute = 365 * 24 * 60
    

day1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

myMinute = 0

if minute == 527040: #윤년
    for i in range(month[ss[0]] - 1):
        myMinute += day2[i] * 24 * 60
else:
    for i in range(month[ss[0]] - 1):
        myMinute += day1[i] * 24 * 60

for i in range(int(ss[1]) - 1):
    myMinute += 24 * 60

myMinute += int(ss[3]) * 60 + int(ss[4])

print(myMinute / minute * 100)