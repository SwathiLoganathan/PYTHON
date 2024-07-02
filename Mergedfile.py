class Multifuntion:
    def Subfields():
        subfields = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing", "Natural Language Processing" ]
        print("Sub-fields in AI are:")
        for subfield in subfields:
            print(subfield)
    def oddeven():
        num1 = int(input("Enter a number: "))
        if num1 % 2 == 0:
            print(num1, "is Even")
            message = "even"
        else:
            print(num1, "is Odd")
            message = "odd"
        return message
    def Eligible():
        gender = input("Your Gender: ")
        age = int(input("Your Age: "))
        if (((gender.lower() =="male") & (age>=21)) or ((gender.lower() =="female") & (age>=18))):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
    def percentage():
        S1 = int(input("S1"))
        S2 = int(input("S2"))
        S3 = int(input("S3"))
        S4 = int(input("S4"))
        S5 = int(input("S5"))
        total = S1 + S2 + S3 + S4 + S5
        percentage = (total / 5) 
        print("Total:", total)
        print("Percentage:", percentage)
    def triangle():
        height = int(input("height"))
        breadth = int(input("Breadth"))
        area = (height * breadth) / 2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:", area)
        h1 = int(input("h1"))
        h2 = int(input("h2"))
        breadth =int(input("Breadth")) 
        perimeter = h1 + h2 + breadth
        print("Perimeter formula: H1+H2+Breadth")
        print("Perimeter of Triangle:", perimeter)


    
    
    