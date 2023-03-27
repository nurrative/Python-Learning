res='yes'
while res=='yes':
    try:
        num1 = (float(input("Введите первое число: ")))
        num2 = (float(input("Введите второе число: ")))
        print("Операции которые вы можете производить:\n'+'-сложение\n'-'-вычитание\n'*'-умножение \n'/'-деление\n '%'-остаток\n'**'-возведение в степень \n'//'-деление без остатка")    
        operation = (input("Введите операцию, которую хотите произвести: "))
        


        if operation == "+":
            print(f"Ответ: {num1} + {num2} =",num1+num2)
        elif operation == "-":
            print(f"Ответ: {num1} - {num2} =",num1-num2)
        elif operation == "*":
            print(f"Ответ: {num1} * {num2} =",num1*num2)
        elif operation == "/":
            print(f"Ответ: {num1} / {num2} =",num1/num2)
        elif operation == "%":
            print(f"Ответ: {num1} % {num2} =",num1%num2)
        elif operation == "**":
            print(f"Ответ: {num1} ^ {num2} =",pow(num1,num2))    
        elif operation == "//":
            print(f"Ответ: {num1} // {num2} =",num1//num2)
        else: print("Данной операции нет в системе")




    except ZeroDivisionError:
        print("На ноль делить нельзя")
    except ValueError:
        print("Вы не ввели число")
        
    # print("Нажмите 'yes' чтобы начать сначала")
    res =input("Нажмите 'yes' чтобы начать сначала: ")    


