# Program to find eligibility of admission for a Job
aptitude = int(input("Enter marks in Aptitude: "))
gd = int(input("Enter marks in GD: "))
technical = int(input("Enter marks in Technical: "))
hr = int(input("Enter marks in HR: "))

if aptitude >= 85:
    if gd >= 90:
        if technical >= 80:
            if hr >= 95:
                total = aptitude + gd + technical + hr
                print("Total Marks:", total)
                if 390 <= total <= 400:
                    print("Eligible for Job with Salary: ₹30000")
                elif 380 <= total < 390:
                    print("Eligible for Job with Salary: ₹28000")
                elif 370 <= total < 380:
                    print("Eligible for Job with Salary: ₹25000")
                elif 350 <= total < 370:
                    print("Eligible for Job with Salary: ₹20000")
                else:
                    print("Not Eligible for selection process.")
            else:
                print("Not eligible - HR marks less than 95.")
        else:
            print("Not eligible - Technical marks less than 80.")
    else:
        print("Not eligible - GD marks less than 90.")
else:
    print("Not eligible - Aptitude marks less than 85.")
