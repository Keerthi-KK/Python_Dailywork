# Program to check exam eligibility based on attendance percentage

classes_held = int(input("Enter number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))

attendance_percentage = (classes_attended / classes_held) * 100

print("Total classes held:", classes_held)
print("Total classes attended:", classes_attended)
print(f"Attendance Percentage: {attendance_percentage}%")

if attendance_percentage > 75:
    print("Not Allowed to attend exam")
else:
    print("Allowed for Exam ")
