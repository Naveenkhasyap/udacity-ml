#my_version
names =raw_input("Enter student names seperated by commas\n") 
name= names.replace(" ","").split(",")
assignment =list(input("Enter assignment seperated by commas\n") )
grade =list(input("Enter grades seperated by commas\n")) 
# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name,assignment,grade in zip(name,assignment,grade):
    print(message.format(name,assignment,grade,grade+(2*assignment)))

'''
#actual solution
names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
'''