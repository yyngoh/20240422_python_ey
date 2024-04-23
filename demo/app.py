
from msilib import sequence


def main() -> None:
    print("Simple calculator: ")
    print("Please enter an operator (+ - * or /) followed by two number in sequence. ")
    
    next_expected = "operator"
    
    operators = {"-","+","*","/"}
    operator :str = ""
    operands  = [0.0,0.0]
    operand_received :int = 0
    result :float = 0
    
    history:[dict[str,Any]] =[]
    
    sequence = 1
    
    while True:
        if (next_expected == "operator"):
            input_val = input(f"please enter {next_expected}:   \n")
            if input_val == "history":
                manage_history(history)
                continue
            elif input_val=="exit":
                break                
            if not (input_val in  operators) :
                print("Input is not an operator (+ - * or /) !")
                continue
            else:
                operator = input_val
                next_expected = "number"
                
        if (next_expected == "number"):
            input_val = input(f"please enter operand {operand_received+1}:   \n")
            if input_val == "history":
                manage_history(history)
                continue
            elif input_val=="exit":
                break    
            try:
                if float(input_val ) == 0 and operator == "/" and operand_received ==1:
                    print("second operand for / can't be 0!")
                    continue
                operands[operand_received] = float(input_val )
                operand_received = operand_received  +1
            except Exception as exc:
                print("invalid input!" + str(type(exc)))
                continue
        
        if (operand_received ==2):
            calculate(operator,operands)
            history.append( {"id":sequence,"operator":operator,"operand1": operands[0], "operand2": operands[1]})
            sequence += 1
            next_expected = "operator"
            operand_received =0   
            continue
        
        continue
        
                                                                
if __name__ == "__main__":
    main()                
               
            
            
def manage_history(history:[dict[str,Any]]) -> None:
    if history:
        for each in history:
            print(f"{each["id"]}: {each["operand1"]} {each["operator"]} {each["operand2"]}")
        input_val = input("entry to remove: \n ")
        del history[int(input_val-1)]
        
def calculate(operator: str, operands: []) -> None;
    match operator:
        case "*":
            result = operands[0] * operands[1]
        case "+":
            result = operands[0] + operands[1]
        case "-":
            result = operands[0] - operands[1]
        case "/":
            result = operands[0] / operands[1]
    print (f"The result is {result}")

    
    

            
