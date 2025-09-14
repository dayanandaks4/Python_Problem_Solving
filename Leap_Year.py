# Take a year and check if it is a leap year.

def check_leap_year(year):
    if year % 400 == 0:
        print("Leap year")
    elif year % 4 == 0 and year % 100 !=0:
        print("Leap year")
    else:
        print("Not a Leap Year")
check_leap_year(2000)
check_leap_year(2004)
check_leap_year(2024)
check_leap_year(2001)
check_leap_year(2018)
check_leap_year(2020)
