##### ---------------------- Answer 01 ---------- ##############

# Define the details
name = "Owais Irshad"
father_name = "Irshad Ullah"
dob = "Aril 26, 1983"

# Print the details using escape sequences for newline and tab
print("Name:\t\t" + name + "\nFather's Name:\t" + father_name + "\nDate of Birth:\t" + dob)




##### ---------------------- Answer 02 ---------- ##############

# Define the bio details
name = "Owais Irshad"
father_name = "Irshad Ullah"
dob = "April 26, 1983"
occupation = "Private Employee"
hobbies = "Learning, Assisting, Chatting"

# Print the bio using the print function
print("Bio:")
print("Name:            " + name)
print("Father's Name:   " + father_name)
print("Date of Birth:   " + dob)
print("Occupation:      " + occupation)
print("Hobbies:         " + hobbies)



##### ---------------------- Answer 03 ---------- ##############

# Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")
print()

# Comparison Operators
print("Comparison Operators")
print(f"Equal: {a} == {b} is {a == b}")
print(f"Not Equal: {a} != {b} is {a != b}")
print(f"Greater than: {a} > {b} is {a > b}")
print(f"Less than: {a} < {b} is {a < b}")
print(f"Greater than or equal to: {a} >= {b} is {a >= b}")
print(f"Less than or equal to: {a} <= {b} is {a <= b}")
print()

# Logical Operators
x = True
y = False

print("Logical Operators")
print(f"Logical AND: {x} and {y} is {x and y}")
print(f"Logical OR: {x} or {y} is {x or y}")
print(f"Logical NOT: not {x} is {not x}")
print()

# Bitwise Operators
print("Bitwise Operators")
print(f"Bitwise AND: {a} & {b} = {a & b}")
print(f"Bitwise OR: {a} | {b} = {a | b}")
print(f"Bitwise XOR: {a} ^ {b} = {a ^ b}")
print(f"Bitwise NOT: ~{a} = {~a}")
print(f"Bitwise Left Shift: {a} << 1 = {a << 1}")
print(f"Bitwise Right Shift: {a} >> 1 = {a >> 1}")
print()

# Assignment Operators
print("Assignment Operators")
c = a
print(f"c = {a} -> c = {c}")
c += b
print(f"c += {b} -> c = {c}")
c -= b
print(f"c -= {b} -> c = {c}")
c *= b
print(f"c *= {b} -> c = {c}")
c /= b
print(f"c /= {b} -> c = {c}")
c %= b
print(f"c %= {b} -> c = {c}")
c //= b
print(f"c //= {b} -> c = {c}")
c **= b
print(f"c **= {b} -> c = {c}")
c &= b
print(f"c &= {b} -> c = {c}")
c |= b
print(f"c |= {b} -> c = {c}")
c ^= b
print(f"c ^= {b} -> c = {c}")
c <<= b
print(f"c <<= {b} -> c = {c}")
c >>= b
print(f"c >>= {b} -> c = {c}")
print()

# Membership Operators
list_ = [1, 2, 3, 4, 5]

print("Membership Operators")
print(f"Is {a} in list_? {'Yes' if a in list_ else 'No'}")
print(f"Is {b} not in list_? {'Yes' if b not in list_ else 'No'}")
print()

# Identity Operators
print("Identity Operators")
print(f"Is a identical to b? {'Yes' if a is b else 'No'}")
print(f"Is a not identical to b? {'Yes' if a is not b else 'No'}")



##### ---------------------- Answer 04 ---------- ##############

# Step 1: Mention Marks of English, Islamiat, and Maths out of 100 in 3 different variables
marks_english = 85
marks_islamiat = 90
marks_maths = 95

# Step 2: Mention Variable of Total Marks and assign 300 to it
total_marks = 300

# Step 3: Calculate Percentage
obtained_marks = marks_english + marks_islamiat + marks_maths
percentage = (obtained_marks / total_marks) * 100

# Print the results
print("Marks Obtained:")
print(f"English: {marks_english}")
print(f"Islamiat: {marks_islamiat}")
print(f"Maths: {marks_maths}")
print(f"Total Marks: {total_marks}")
print(f"Obtained Marks: {obtained_marks}")
print(f"Percentage: {percentage:.2f}%")
