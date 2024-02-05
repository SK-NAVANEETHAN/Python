class multiplefunctions():
    def Subfields():
        lists=["Sub-fields in AI are:","Machine Learning","Neural Networks","Vision,Robotics","Speech Processing","Natural Language Processing"]
        for x in lists:
            print(x)
            
    def OddEven():
        num=int(input("Enter a number:"))
        if (num%2==0):
            print("52452 is Even number")
        else:
            print("52452 is odd number")
            
    def Elegible():
        Gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(age==21):
            print("ELIGIBLE")
        elif(age==18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
            
    def percentage():
        Subject1=int(input("Subject1= "))
        Subject2=int(input("Subject2= "))
        Subject3=int(input("Subject3= "))
        Subject4=int(input("Subject4= ")) 
        Subject5=int(input("Subject5= "))
        total=(Subject1+Subject2+Subject3+Subject4+Subject5)
        percentage=((total / 500) * 100)
        print("Total :",total)
        print("Percentage :",percentage)
            
    def triangle():
        Height=int(input("Height :"))
        Breadth=int(input("Breadth :"))
        print("Area formula: (Height*Breadth)/2")
        print("Area formula:",(Height*Breadth)/2)
        Height1=int(input("Height :"))
        Height2=int(input("Height :"))
        Breadth=int(input("Breadth :"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter formula:", Height1+Height2+Breadth)