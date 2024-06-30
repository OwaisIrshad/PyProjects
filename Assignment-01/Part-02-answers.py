##### ---------------------- Answer 01 ---------- ##############

# Get user input for salary and years of service
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

# Define the bonus percentage
bonus_percentage = 5

# Calculate the bonus if years of service is more than 5 years
if years_of_service > 5:
    bonus_amount = (salary * bonus_percentage) / 100
else:
    bonus_amount = 0

# Print the net bonus amount
print(f"Net bonus amount: ${bonus_amount:.2f}")


##### ---------------------- Answer 02 ---------- ##############

# Get user input for age
age = int(input("Enter your age: "))

# Check if the person is eligible for voting
if age > 17:
    print("You are eligible for voting.")
else:
    print("You are not eligible for voting.")



##### ---------------------- Answer 03 ---------- ##############

# Get user input for the number
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")



##### ---------------------- Answer 04 ---------- ##############

# Get user input for the number
number = int(input("Enter a number: "))

# Check if the number is divisible by 7
if number % 7 == 0:
    print(f"{number} is divisible by 7.")
else:
    print(f"{number} is not divisible by 7.")



##### ---------------------- Answer 05 ---------- ##############


# Get user input for the number
number = int(input("Enter a number: "))

# Check if the number is a multiple of five
if number % 5 == 0:
    print("Hello")
else:
    print("Bye")


##### ---------------------- Answer 07 ---------- ##############

# Get user input for the number
number = int(input("Enter a number: "))

# Get the last digit of the number
last_digit = number % 10

# Display the last digit
print(f"The last digit of {number} is {last_digit}.")




##### ---------------------- Answer 09 ---------- ##############

# Get user input for length and breadth
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

# Check if it is a square or rectangle
if length == breadth:
    print("It is a square.")
else:
    print("It is a rectangle.")



##### ---------------------- Answer 10 ---------- ##############

# Get user input for two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Compare the two numbers to find the greatest
if num1 > num2:
    print(f"The greatest number is: {num1}")
elif num2 > num1:
    print(f"The greatest number is: {num2}")
else:
    print("Both numbers are equal.")



##### ---------------------- Answer 11 ---------- ##############

# Cost per unit
cost_per_unit = 100

# Get user input for quantity
quantity = int(input("Enter the quantity purchased: "))

# Calculate total cost
total_cost = quantity * cost_per_unit

# Check if discount applies and calculate final cost
if total_cost > 1000:
    discount = 0.1 * total_cost
    final_cost = total_cost - discount
else:
    final_cost = total_cost

# Print the total cost for the user
print(f"Total cost: ${final_cost:.2f}")



##### ---------------------- Answer 12 ---------- ##############

# Get user input for marks
marks = float(input("Enter your marks: "))

# Determine the grade based on the marks
if marks < 25:
    grade = "F"
elif marks >= 25 and marks < 45:
    grade = "E"
elif marks >= 45 and marks < 50:
    grade = "D"
elif marks >= 50 and marks < 60:
    grade = "C"
elif marks >= 60 and marks <= 80:
    grade = "B"
else:
    grade = "A"

# Print the corresponding grade
print(f"Your grade is: {grade}")




##### ---------------------- Answer 14 ---------- ##############


# Get user input for number of classes held and attended
classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

# Calculate attendance percentage
attendance_percentage = (classes_attended / classes_held) * 100

# Print percentage of classes attended
print(f"Percentage of classes attended: {attendance_percentage:.2f}%")

# Check if student is allowed to sit in exam
if attendance_percentage >= 75:
    print("Student is allowed to sit in the exam.")
else:
    print("Student is not allowed to sit in the exam.")




##### ---------------------- Answer 15 ---------- ##############


# Get user input for number of classes held and attended
classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

# Calculate attendance percentage
attendance_percentage = (classes_attended / classes_held) * 100

# Print percentage of classes attended
print(f"Percentage of classes attended: {attendance_percentage:.2f}%")

# Get user input for medical cause ('Y' for Yes, 'N' for No)
medical_cause = input("Do you have a medical cause? (Y/N): ")

# Check if student is allowed to sit in exam
if attendance_percentage >= 75 or medical_cause.upper() == 'Y':
    print("Student is allowed to sit in the exam.")
else:
    print("Student is not allowed to sit in the exam.")




##### ---------------------- Answer 16 ---------- ##############


# Get user input for the year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")




##### ---------------------- Answer 17 ---------- ##############

# Get user input for age, gender, and marital status
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
marital_status = input("Enter your marital status (Y/N): ").upper()

# Determine the place of service based on the rules
if age < 20 or age > 60:
    print("ERROR")
elif gender == 'F':
    print("You will work in urban areas.")
elif gender == 'M':
    if 20 <= age <= 40:
        print("You may work anywhere.")
    elif 40 <= age <= 60:
        print("You will work in urban areas only.")
else:
    print("ERROR")




##### ---------------------- Answer 06 ---------- ##############

# Get user input for number of units consumed
units = int(input("Enter the number of units consumed: "))

# Initialize variables for calculation
total_bill = 0

# Calculate electricity bill based on given criteria
if units <= 100:
    total_bill = 0  # No charge for up to 100 units
elif units <= 300:
    total_bill = (units - 100) * 5  # Rs 5 per unit for next 200 units
else:
    total_bill = (200 * 5) + (units - 300) * 10  # Rs 5 per unit for 200 units and Rs 10 per unit thereafter

# Print the total bill amount
print(f"The total bill amount is Rs. {total_bill}")



##### ---------------------- Answer 06 ---------- ##############


# Get user input for ages of 3 people
age1 = int(input("Enter age of first person: "))
age2 = int(input("Enter age of second person: "))
age3 = int(input("Enter age of third person: "))

# Initialize variables for oldest and youngest
oldest = youngest = age1

# Determine oldest age
if age2 > oldest:
    oldest = age2
if age3 > oldest:
    oldest = age3

# Determine youngest age
if age2 < youngest:
    youngest = age2
if age3 < youngest:
    youngest = age3

# Print the oldest and youngest ages
print(f"The oldest person is {oldest} years old.")
print(f"The youngest person is {youngest} years old.")
