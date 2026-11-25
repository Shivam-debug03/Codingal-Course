# Step 1 : A list of classmates in the order they joined.
classmates = ["Aiden","Paula","Ricky","Sonia","Dan"]
print("Class list:" , classmates)

# Step 2 : Read the list without changinh it.
print("Total Students : ", len(classmates)) 
print("First :",classmates[0] , " | Last :" , classmates[-1])
print("First Three :" , classmates[ : 3])

# Step 3 : Change the list.
def remove_student(names , name):
  if name in names :
    names.remove(name)
    return True
  return False

classmates.append("Maria")
leaver = input ("Which student leaves the class ? ")
print("Remove" , leaver + ":" , remove_student(classmates , "Kevin" ))
classmates.sort()
print("Sorted : ", classmates)

# Step 4 : A dictionary , where each key is a label for one value
teacher = {"name" : "Mr. Smith" , "Subject" : "Python" , "Experience" : 5}
print("\nTeacher : " , teacher)

# Step 5 : Read , update , add and remove keys.
print("Subject : " , teacher["Subject"])
print("Email :" , teacher.get("email" , "not found"))
teacher["Experience"] = 6
teacher["room"] = "Lab 2"
teacher.pop("Experience")
print("Updated teacher :",teacher)

#Step 6 : 2 lists that line up , position by position.
roll_numbers = [1,2,3,4,5]
directory = dict(zip(roll_numbers , classmates))
print("\nDirectory :", directory)

def find_by_roll (book , roll):
  return book.get(roll , "No student with that roll number")

roll = int(input("Roll number to look up ?"))
print(f"Roll{roll}:",find_by_roll(directory,roll))
print("Roll 9 :", find_by_roll(directory,9))
empty_class = []
print("Empty class :",len(empty_class),empty_class[:3] ,remove_student(empty_class,"Dan"))