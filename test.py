TRIANGLE PROBLEM
def is_triangle(a, b, c):
    return 1 <= a <= 20 and 1 <= b <= 20 and 1 <= c <= 20

def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral triangle"
    elif a != b and a != c and b != c:
        return "Scalene triangle"
    else:
        return "Isosceles triangle"

while True:
    try:
        a, b, c = map(int, input("\nEnter 3 integers which are sides of a triangle: ").split())
    except ValueError:
        print("Invalid input. Please enter integers.")
        continue

    if is_triangle(a, b, c):
        print(triangle_type(a, b, c))
        break
    else:
        print("Triangle sides should be integers between 1 and 20. Please try again.")

----------------------------------------------------------------------------------------------------------------------------

COMMISION PROBELM
def calculate_commission(sales):
    if sales > 1800:
        return 0.10 * 1000 + 0.15 * 800 + 0.20 * (sales - 1800)
    elif sales > 1000:
        return 0.10 * 1000 + 0.15 * (sales - 1000)
    else:
        return 0.10 * sales

locks_price, stocks_price, barrels_price = 45.0, 30.0, 25.0
total_locks, total_stocks, total_barrels = 0, 0, 0

while True:
    try:
        locks = int(input("\nEnter the number of locks (Enter -1 to exit): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    if locks == -1:
        break

    stocks = int(input("Enter the number of stocks: "))
    barrels = int(input("Enter the number of barrels: "))

    if not 1 <= locks <= 70 or not 1 <= stocks <= 80 or not 1 <= barrels <= 90:
        print("Invalid input. Values should be within the range.")
        continue

    total_locks += locks
    total_stocks += stocks
    total_barrels += barrels

    print(f"Total locks: {total_locks}\nTotal stocks: {total_stocks}\nTotal barrels: {total_barrels}")

total_sales = locks_price * total_locks + stocks_price * total_stocks + barrels_price * total_barrels
print(f"\nTotal sales: {total_sales}")

if total_sales > 0:
    commission = calculate_commission(total_sales)
    print(f"The commission is: {commission}")
else:
    print("There are no sales")

----------------------------------------------------------------------------------------------------------------------------

NEXT DATE
def is_leap(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

def get_next_date(day, month, year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2:
        max_days = 29 if is_leap(year) else 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    else:
        max_days = 30

    if day < 1 or day > max_days:
        print(f"Invalid date: {month}/{day}/{year} has an invalid day.")
        return None

    day += 1
    if day > max_days:
        day = 1
        month += 1

    if month > 12:
        month = 1
        year += 1

    return day, month, year

def main():
    day = int(input("Enter the day: "))
    month = int(input("Enter the month: "))
    year = int(input("Enter the year: "))

    next_date = get_next_date(day, month, year)
    if next_date is not None:
        tomm_day, tomm_month, tomm_year = next_date
        print(f"The given date: {day} {month} {year}")
        print(f"The next date: {tomm_day} {tomm_month} {tomm_year}")

if _name_ == "_main_":
    main()
