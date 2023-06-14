def Add(a1,a2): return a1 + a2
def Sub(a1,a2): return a1 - a2
def Div(a1,a2): return a1 / a2
def Mul(a1,a2): return a1 * a2

def calcU():
    """whole calculation function to call the calculator and use as a starting point"""
    Continu = True
    num1 = float(input("enter the first number\n"))
    
    while Continu:
        
        key = input("enter \'+' to add,"+
                "enter \'-' to subtract,"+
                "enter \'/' to divide,"+
                "enter \'*' to multiply\n")    
        num2 = float(input("enter the second number\n"))
        operations = {
            "+":Add,
            "-":Sub,
            "/":Div,
            "*":Mul
        }    

        calC = operations[key]
        ans = calC(num1,num2)
        print(f"your answe is {ans}")
        choice = input("do you want to continue calculating with your answer? y for yes, n for starting with a new calculation\n")
        
        if choice.lower() == "y":
            num1 = ans
            
        else:
            Continu = False
            calcU()
calcU()

