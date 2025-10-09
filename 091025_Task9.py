# Program to calculate bonus based on years of service

salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))
if years_of_service > 5:
    bonus = salary * 0.05
    net_salary = salary + bonus
    print(f"You are eligible for a bonus of  Rs.{bonus}/-")
    print(f"Your total salary after bonus is  Rs.{net_salary}/-")
else:
    print("Sorry,you are not eligible for the bonus.")
    print(f"Your salary is Rs.{salary}/- only")
