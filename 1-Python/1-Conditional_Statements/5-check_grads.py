marks = int(input("Enter the makrs : "))

if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 70 and marks < 90:
    print("Grade B")    
elif marks >= 50 and marks < 70:
    print("Grade C")  
elif marks >= 40 and marks < 50:
    print("Grade D")         
else:
    print("Fail")