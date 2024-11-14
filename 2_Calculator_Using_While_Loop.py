o=1
while o!=100:
    print("""
    <<<<<<  Basic Calculator  >>>>>>>

        Press 1 for Addition
        Press 2 for Subtruction
        Press 3 for Multiplication
        Press 4 for Division
        Press 5 for Remainder
        Press 6 for Square
        Press 7 for Square root
        Press 8 for Persent(%)
        Press 9 for Simple Interset Calculation
        Press 10 for Grade Calculation
        Press 11 for 2D 3D Shapes Calculation
        Press 12 for Celsious Fahrenheit Converter
        press 13 for exit
    """)
    c=int(input("Enter Your Choice :"))

    if(c==1):
        x=eval(input("Enter the first number: "))
        y=eval(input("Enter the second number: "))
        print(x,"+",y,"=",x+y)
    elif(c==2):
        x=eval(input("Enter the first number: "))
        y=eval(input("Enter the second number: "))
        print(x,"-",y,"=",x-y)
    elif(c==3):
        x=eval(input("Enter the first number: "))
        y=eval(input("Enter the second number: "))
        print(x,"*",y,"=",x*y)
    elif(c==4):
        x=eval(input("Enter the first number: "))
        y=eval(input("Enter the second number: "))
        print(x,"/",y,"=",x/y)
    elif(c==5):
        x=eval(input("Enter the first number: "))
        y=eval(input("Enter the second number: "))
        print(x,"%",y,"=",x%y)
    elif(c==6):
        x=eval(input("Enter the number: "))
        print(x,"^2=",x**2)
    elif(c==7):
        import math
        x=eval(input("Enter the number: "))
        print("Square root of",x,"=",math.sqrt(x))
    elif(c==8):
        x=eval(input("Enter the main value :"))
        y=eval(input("Enter the persent value :"))
        p=(x*y)/100
        print(x,"*",y,"% =",p)
    
    elif(c==9):
        p=int(input("Enter Your Principal Amount ="))
        r=int(input("Enter the interest rate ="))
        t=int(input("Enter the time period ="))
        si=(p*t*r)/100
        print(t,"Year's", r, "% interest rate of Rs.",p,"=",si)
        print("Total amount with interest is =", p+si)
    elif(c==10):
        n=int(input("Enter your number:"))
        if(n<40):
            print("You are Fail ")
        elif(n>=40 and n<50):
            print("Third Division")
        elif(n>=50 and n<60):
            print("Second Division")
        elif(n>=60 and n<75):
            print("First Division")
        elif(n>=75 and n<80):
            print("Star Mark")
        elif(n>=80 and n<90):
            print("Letter")
        elif(n>=90 and n<=100):
            print("Outstanding")
        else:
            print("Invalid Input")
    elif(c==11):
        o=1
        while o!=100:
            print("""
                ********** 2D 3D Shapes Calculation ************

                        Press 1 for Square
                        Press 2 for Ractangle
                        Press 3 for Triangle
                        Press 4 for Circle
                        Press 5 for Cylinder
                        Press 6 for Cone
                        Press 9 for Exit
            """)
            c1=int(input("Enter your choice :"))
            if(c1==1):
                e=eval(input("Enter the value of the square's edge ="))
                area=e*e
                perimeter=4*e
                diagonal=(2**0.5)*e
                print("Area of the Square is =",area)
                print("Perimeter of the Square is =",perimeter)
                print("Diagonal of the square is =",diagonal)

            elif(c1==2):
                l=eval(input("Enter the value of the ractangle's length is ="))
                w=eval(input("Enter the value of the ractangle's width is ="))
                area=l*w
                perimeter=2*(l+w)
                diagonal=(l**2+w**2)**0.5
                print("Area of ractangle is =", area)
                print("Perimeter of ractangle is =", perimeter)
                print("Diagonal of ractangle is =", diagonal)

            elif(c1==3):
                b=eval(input("Enter the value of the triangle's base ="))
                h=eval(input("Enter the value of the triangle's height ="))
                area=0.5*b*h
                print("Area of the triangle is =", area)

                a=int(input("Enter the value of the triangle's first edge ="))
                b=int(input("Enter the value of the triangle's second edge ="))
                c=int(input("Enter the value of the triangle's third edge ="))
                perimeter=a+b+c
                print("Perimeter of the triangle is =",perimeter)

            elif(c1==4):
                r=eval(input("Enter the value of the radius : "))
                pi=3.1416
                area=pi*r*r
                circumference=2*pi*r
                diameter=2*r
                print("The area of circle is =", area)
                print("The Circumference of circle is =",circumference)
                print("The diameter of circle is =", diameter)

            elif(c1==5):
                r=eval(input("Enter the value of the radius ="))
                h=eval(input("Enter the value of the cylinder's height ="))
                pi=3.1416
                volume=pi*(r**2)*h
                lsa=2*pi*r*h        # Lateral Surface Area
                tsa=2*pi*r*(h+r)    # Total Surface Area
                print("The volume of cylinder is =",volume)
                print("Lateral Surface Area of cylinder is =",lsa)
                print("Total Surface Area of cylinder is =", tsa)

            elif(c1==6):
                r=eval(input("Enter the value of the Cone's radius ="))
                h=eval(input("Enter the value of the Cone's height ="))
                pi=3.1416
                l=(r**2 + h**2)**0.5 #Slant Height
                volume=(1/3)*(pi*r*r*h)
                lsa=pi*r*l  #Lateral Surface Area
                tsa=pi*r*(l+r) #Total Surface Area
                print("Slant Height of the Cone is =", l)
                print("Volume of the Cone is =", volume)
                print("Lateral Surface Area of the Cone is =",lsa)
                print("Total Surface Area of the Cone is =", tsa)

            elif(c1==9):
                break
            else:
                print("Invalid Input")

    elif(c==12):
        print("<<<<<<<<< Celsius to Fahrenheit Converter >>>>>>>>>>>>")

        c=eval(input("Enter the vlaue of the Celsius Scale : "))
        f=(9/5*c)+32
        print("Fahrenheit Scale value is :",f)

        print("<<<<<<<<< Fahrenheit to Celsius Converter >>>>>>>>>>>>")

        f=eval(input("Enter the value of the fahrenheit Scale : "))
        c=(f-32)*(5/9)
        print("Celsius Scale value is :", c)

    if(c==13):
        break

    else:
        print("Invalid Input")
        
   



