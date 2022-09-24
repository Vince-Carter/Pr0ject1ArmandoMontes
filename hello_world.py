faculty_file = open("requiredCS.txt", 'r')
all_class_lines = faculty_file.readlines()
print(all_class_lines)
for class_line in all_class_lines:
    loud_line = class_line.lower()
    class_and_name = class_line.split(":")
    print(class_and_name[0])
    print(class_and_name[1])
print("those are the courses you have to take")