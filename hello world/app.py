def main() -> None:
    print("hello world")
    
#This the guard  to only run code when it is the executable, otherwise only 
#the items defined in the file can be imported.

#for codes not under a function or within class, without the guard, will get executed when the file is imported.#
if __name__ == "main__":
    print("app1")
    main()




