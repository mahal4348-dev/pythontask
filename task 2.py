# case 1 Declare variables to store the detail
# Store the student name
student_name = "maha"

# Store the course name
course_name = "Python Fundamentals"

# Store the training institute name
institute_name = "Inceptez Technologies"

# Print the formatted message
print("Name:", student_name, "is learning the course", course_name, "at the institute", institute_name)

#case 2 Dynamic inference,Dynamic typing,Strong typing
# Dynamic inference

fee = 45000
#print fee
print("Fee:", fee)

#print fee datatype
print("Data type:", type(fee))


# Dynamic typing - applying 18% GST

#calculation fee
fee = fee + (fee * 0.18)

#after calculated fee
print("Fee after 18% GST:", fee)

#datatype
print("Data type:", type(fee))



# Strong typing - different data types cannot be directly operated
# fee int
fee = 45000
#18 percent string
gst = "18 percent"

# print(fee + gst)   # TypeError

#Variables Naming Conventions
#2student = 'Ravi'  - invalid  Variable name cannot start with a number
_student_id = 1001
studentName = 'lubu'
#class name = 'Python' - invalid Spaces are not allowed in variable names
inceptez_batch = 'Morning'

print(_student_id)
print(studentName)
print(inceptez_batch)

#Declare 3 variables following naming styles
# PascalCase - Each word starts with a capital letter
DataEngineeringBatch = "Morning"

# camelCase - first word lowercase, next words Capital
dataEngineeringBatch = "Morning"

# snake_case - Words are separated using underscores
data_engineering_batch = "Morning"

print('pascalcase:', DataEngineeringBatch)
print('camelCase:',dataEngineeringBatch)
print('snake_case:',data_engineering_batch)

# Type identification & Casting
#input()
age = input("Enter the employee's age:")
#Check the Type
print(type(age))
#Converts it to int
age = int(age)
retirement_age = 60
#Calculate years pending
years_pending = retirement_age - age
print(f"You will retire in {years_pending} years at Inceptez Technologies.")

#Debug
#salary = '50000'
#bonus = 10000
#print('Total Salary in Inceptez:', salary + bonus)
#correct the code
salary = '50000'
bonus = 10000
#convert to int
salary = int(salary)
print(type(salary))
print('Total Salary in Inceptez:', salary + bonus)

#Data types and casting
employee_name = input("Enter employee name:")
base_salary = float(input("Enter Base Salary:"))
hra_percent =int(input("Enter hra percent:"))
bonus_amount = float(input("Enter bonus amount:"))
#Calculate
HRA = base_salary * (hra_percent / 100)
Total_Salary = base_salary + HRA + bonus_amount
print("Total_Salary:", Total_Salary)
print(type(Total_Salary))

#Operators
#Internet Data Usage Calculator
data_limit =  float(input("Total monthly data limit in GB:"))
Data_used = float(input("data used so far in GB:"))
#Calculate using arithmetic operators
Remaining_data = data_limit - Data_used
Usage_percentage = (Data_used/ data_limit) * 100
print("Remaining_data:", Remaining_data)
print("Usage_percentage:", round(Usage_percentage,2),"%")
if Usage_percentage >= 80:
    print( "Warning: High usage, consider upgrading your plan.")

#Shopping Discount Calculation
Original_price = (float(input("Enter Original price:")))
discount_percent = (int(input("Enter Discount percent:")))
discount_amount = (Original_price * discount_percent) / 100
Final_price = Original_price - discount_amount

print("Original price:", Original_price)
print("Discount percent:", discount_percent)
print("final price:", Final_price)
print("discount amount:", discount_amount)


item_name = input("Enter product name: ")
price = (float(input("Enter price per item: ")))
quantity = (int(input("Enter quantity: ")))
total_cost = price * quantity
print("Total cost:", total_cost)
# f -> formatted string method
print(f"You purchased  {quantity}   units of  {item_name}")
#string + int pana mudiyathu so convert to str
#print("You purchased " + quantity + " units of " + item_name)
print("You purchased " + str(quantity) + " units of " + item_name)
print("Total payable: " + str(total_cost))
print(f"Total payable: {total_cost} ")

# String + int cannot be concatenated directly.
# So, we use str() to convert the integer into a string.

# f-string is a formatted string method.
# It allows us to insert variables directly using {}.

#Incorrect code:
"""age = input("Enter age: ")
 citizen = input("Are you an Indian citizen? (yes/no)")
if age > "18" and citizen = "yes":
 print("Eligible to vote")
 else:
 print("Not eligible")"""

age = input("enter age: ")
age = int(age)
citizen = input("Are you an Indian citizen? (yes/no)")
if age >= 18 and citizen == "yes":
    print("Eligible to vote")
else:
    print("Not eligible")