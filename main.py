print("===================")
print("  Student Dashboard  ")
print("===================")

Studentid = int(input("Enter Student ID: "))
Studentname = input("Enter Student Name: ")

Subject1 = input("Enter Subject 1 Name: ")
NumofHrspersubject1 = int(input("Enter Subject 1 Hours: "))

Subject2 = input("Enter Subject 2 Name: ")
NumofHrspersubject2 = int(input("Enter Subject 2 Hours: "))

Subject3 = input("Enter Subject 3 Name: ")
NumofHrspersubject3 = int(input("Enter Subject 3 Hours: "))

TotalHours = (NumofHrspersubject1 +
              NumofHrspersubject2 +
              NumofHrspersubject3)

average =TotalHours/3



print("Student ID:", Studentid)
print("Student Name:", Studentname)
print("------------------------")

print("Subject 1:", Subject1)
print("Study Hours:", NumofHrspersubject1)
print("-----------------------")
print("Subject 2:", Subject2)
print("Study Hours:", NumofHrspersubject2)
print("-------------------")
print("Subject 3:", Subject3)
print("Study Hours:", NumofHrspersubject3)

print("--------------------")
print("Total Study Hours:", TotalHours)
print("--------------------")

print("Average Study Hours:", average)
print("--------------------")
if (TotalHours > 9):
    print("Your a good student")

else:
    print("Your a bad student")