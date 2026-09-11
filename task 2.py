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


