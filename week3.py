faculty_file = open("faculty.txt", 'r')
all_faculty = faculty_file.readlines()
for faculty in all_faculty:
    name_and_class = faculty.split("-")
    print(name_and_class[0])
    print(name_and_class[1])