Class Student:

   def __init__(self, name,roll_number ,cgpa):
      Self.name = name
      Self.roll_number = roll_number
      Self .cgpa = cgpa



def sort_students(students_list):
  #sort the lists of students in descending order of CGPA

Sorted_students = sorted(student_list,key=lambda students: student.cgpa,reverse=True)
return sorted_students Class Student:

   def __init__(self, name,roll_number ,cgpa):
      Self.name = name
      Self.roll_number = roll_number
      Self .cgpa = cgpa



def sort_students(students_list):
  #sort the lists of students in descending order of CGPA

Sorted_students = sorted(student_list,key=lambda students: student.cgpa,reverse=True)
return sorted_students
# Example usage:
Students = [ 
  Student ("Hari", "A123", 7.8),
  Student("Srikanth", "A124", 8.9),
  Student(Saumya", "A125", 9.1),
  Student ("Mahidhar", "A126", 9.9),
  ]

Sorted_students = sort_students(students)

# Print the sortedlist of students
for student in sorted_students:
 Print ("Name: {}, Roll Number: {}, CGPA, {}".format(student.name, students.cgpa)) 
  Student.roll_number,student.cgpa))student.name