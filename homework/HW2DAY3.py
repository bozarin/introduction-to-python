#HW3
#Student dictionary plus list 
#Day2

def test(dictt,keys):
    return [list(d[k] for k in keys) for d in dictt] 

students = [
    
        {'student_no': 1, 'fullname' : 'AJ Nuclear', 'midterm': '50' , 'homework': '70' , 'final': '80' }, 
        {'student_no': 2, 'fullname' : 'Kevin Tianjin', 'midterm': '71' ,'homework': '95' , 'final': '75'},
        {'student_no': 3, 'fullname' : 'Pluto Dwarf', 'midterm': '79' , 'homework': '90' , 'final': '85'}, 
        {'student_no': 4, 'fullname' : 'Catto Bored', 'midterm': '85' , 'homework': '65' , 'final': '73'}, 
        {'student_no': 5, 'fullname': ' Grinch Green ', 'midterm': '95' , 'homework': '78' , 'final': '88'}
        


]

print("Student numbers , names and final marks are : ")
print("\n",test(students,('student_no', 'fullname', 'final')))
print("\n")
print("Student numbers , names and midterm marks are : ")
print(test(students,('fullname', 'midterm')))
print("Student numbers , names and homework marks are : ")
print("\n")
print(test(students,('fullname', 'homework')))
print("\n")
print(test(students,('fullname', 'final')))


midterm = [50 , 71 , 79 , 85 , 95]

midterm.sort()
midterm




#Until here I just wanted show all students grades clearly. Now i will do list their grades in descending order according to their avarage. 



fullname = ['AJ Nuclear','Kevin Tianjin','Pluto Dwarf','Catto Bored','Grinch Green']

midterm = ['midterm1', 'midterm2', 'midterm3', 'midterm4', 'midterm5']

homework = ['HW1', 'HW2', 'HW3', 'HW4', 'HW5']

final = ['final1', 'final2', 'final3', 'final4', 'final5']

avg = ["avg1","avg2","avg3","avg4","avg5"]


for i in range(len(fullname)):

midterm[i] = int(input("Enter the midterm grade: "))
final[i] = int(input("Enter the final grade : "))
homework[i] = int(input("Homework notu girin: "))
avg[i] = ( midterm[i] + final[i] + homework[i] ) / 3

avg.sort(reverse=True)
avg





#grades represents homework midterm and final mark respectively according to the name orde given in fullname matrix



print("\n")

#For AJ 

print("AJ Nuclear's avarage")
Midterm = float(50)
Homework= float(70)
Final= float(80)

 
total = Midterm + Homework + Final 
average = total / 3
percentage = (total / 300) * 100
 
print("Average Marks = %.2f"  %average)
print("Marks Percentage = %.2f"  %percentage)
print("\n")
print("\n")


#For Kevin 
      
print(" Kevin Tianjin's average: " )
Midterm = float(71)
Homework= float(95)
Final= float(75)
      
total = Midterm + Homework + Final 
average = total / 3
percentage = (total / 300) * 100
 
print("Average Marks = %.2f"  %average)
print("Marks Percentage = %.2f"  %percentage)
print("\n")
print("\n")

#Pluto Dwarf
print("Pluto Dwarf's avarage ")
Midterm = float(79)
Homework= float(90)
Final= float(85)
      
total = Midterm + Homework + Final 
average = total / 3
percentage = (total / 300) * 100
 
print("Average Marks = %.2f"  %average)
print("Marks Percentage = %.2f"  %percentage)

print("\n")
print("\n")
#Catto Bored

print("Catto Bored's grade calculations:")
Midterm = float(85)
Homework= float(65)
Final= float(73)
      
total = Midterm + Homework + Final 
average = total / 3
percentage = (total / 300) * 100
 
print("Average Marks = %.2f"  %average)
print("Marks Percentage = %.2f"  %percentage)




#Grinch Green

print("Grinch Green's grade calculations : ")

Midterm = float(95)
Homework= float(78)
Final= float(88)
      
total = Midterm + Homework + Final 
average = total / 3
percentage = (total / 300) * 100
 
print("Average Marks = %.2f"  %average)
print("Marks Percentage = %.2f"  %percentage)
