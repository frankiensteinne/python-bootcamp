def is_leap(year):
    if year % 4 == 0:
        if year % 100:
            if year % 400:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_index = month - 1
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year) and month_index == 1:
        return 29
    else:
        return month_days[month_index]



year = int(input("Input Year: "))
month = int(input("Input Month: "))
days = days_in_month(year, month)

print(days)