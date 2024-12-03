# Sets representing the students enrolled in Java and Python courses
java_course = {"John", "Jack", "Jill", "Joe"}
python_course = {"Jake", "John", "Eric", "Jill"}

# a. List the number of students enrolled in the Python course
print(f"Number of students enrolled in Python course: {len(python_course)}")

# b. List the names of students enrolled for Java course only
java_only = java_course - python_course
print(f"Students enrolled for Java course only: {java_only}")

# c. List the names of students enrolled for Python course only
python_only = python_course - java_course
print(f"Students enrolled for Python course only: {python_only}")

# d. List the number and names of students enrolled in both Java and Python courses
both_courses = java_course & python_course
print(f"Number of students enrolled in both courses: {len(both_courses)}")
print(f"Students enrolled in both courses: {both_courses}")

# e. List the number and names of students enrolled for either Java or Python courses but not both
either_but_not_both = java_course ^ python_course
print(f"Number of students enrolled in either course but not both: {len(either_but_not_both)}")
print(f"Students enrolled in either course but not both: {either_but_not_both}")

# f. List names and number of students enrolled for either Java or Python courses
either_course = java_course | python_course
print(f"Number of students enrolled in either course: {len(either_course)}")
print(f"Students enrolled in either course: {either_course}")
