def calculate():
    final = 0
    wantsToCont = True
    
    firstNum = input("What is the number? ")
    while wantsToCont:
        operation = input("""Do you want to: 
/
*
+
-
""")
        anotherNum = input("What is the number? ")
        
        if operation == "/":
            if final == 0:
                final = float(firstNum) / float(anotherNum)
            else:
                final /= float(anotherNum)
        elif operation == "*":
            if final == 0:
                final = float(firstNum) * float(anotherNum)
            else:
                final *= float(anotherNum)
        elif operation == "+":
            if final == 0:
                final = float(firstNum) + float(anotherNum)
            else:
                final += float(anotherNum)
        elif operation == "-":
            if final == 0:
                final = float(firstNum) - float(anotherNum)
            else:
                final -= float(anotherNum)
        cont = input(f"Do you want to calculate {final} to something else? ")
        if cont == "no":
            wantsToCont = False

calculate()