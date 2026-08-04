class Student:
    def __init__(self , name , roll_number):
        self.name = name
        self.roll_number = roll_number
    def add_marks(self , physics , chemistry , maths):
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths

    def calculate_average(self):
        self.total = (self.physics + self.chemistry + self.maths)
        self.average = int((self.total) / 3)
        
    def calculate_grade(self):
        if(self.average >= 90 and self.average <= 100):
            self.grade = "A+"
        elif(self.average >= 80 and self.average <= 89):
            self.grade = "A"
        elif(self.average >= 70 and self.average <= 79):
            self.grade = "B"
        elif(self.average >= 60 and self.average <= 69):
            self.grade = "C"
        elif(self.average >= 40 and self.average <= 59):
            self.grade = "D"
        else:
            self.grade = "Fail"   
    
    def display_result(self):
        print("======STUDENT REPORT======")
        print("Name :" , self.name)
        print("Roll Number :" , self.roll_number)
        print("Physics :" , self.physics)
        print("Chemistry :" , self.chemistry)
        print("Maths :" , self.maths)
        print("Total Marks :" , self.total)
        print("Average :" , self.average)
        print("Grade :" , self.grade)
        if (self.average >= 40):
            print("Result :" ,"Pass")
            
        else:
            print("Result :","Fail")
            
name = input("Enter Name :")  
roll_no = int(input("Enter Roll Number :"))         
s1 = Student(name , roll_no)
phy = int(input("Enter a Physics marks :"))
chem = int(input("Enter a chemistry marks :"))
maths = int(input("Enter a maths marks :"))
s1.add_marks(phy , chem , maths)
s1.calculate_average()
s1.calculate_grade()
s1.display_result()