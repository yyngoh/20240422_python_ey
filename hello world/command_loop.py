
def main() -> None:
    while True:
        command = input("enter a command: ")
        if command  == "exit":
            break
        #f-string is a convenient way to format (string interpolation)
        print(f"received command: {command}")
        
        
        
if __name__=="__main__":
    main()