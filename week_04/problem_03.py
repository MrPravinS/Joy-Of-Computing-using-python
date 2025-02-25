# What is the date of birth
#  Birthday paradox : Find your twin 
#  if person1 dd/mm == person2 dd/mm  they are twin

# if year % 400 == 0  and year % 4 === 0 => leap year
# else if year % 100 !== 0 => not leap year
#  else not leap year

#  psuedo code
'''
if month is feb and year is leap 
generate random from 1 to 29
if month feb and year is not leap 
        1 to 28
if month % 2 and month < 7 // april and june
      from 1 to 30
if month % 2 == 0 and month > 7 // aug oct, dec
 1 to 31
if month % 2 != 0 and month <= 7 // jan march may july
 1 to 31
if month % 2 != 0 and month < 7 // sep, nov
1 to 30
'''

def leapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year , " is Leap year")
    else:
        print(year , " is not leap year")
print(leapYear(2024))