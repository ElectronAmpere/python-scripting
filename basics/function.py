# A function
def hello():
    print("hello")

# Function call
hello()

def getInteger():
    return int(input("Enter an Integer: "))

def Main():
    print("Main Started")

    # calling the function and storing the variable
    print(getInteger())

if __name__ == "__main__":
    Main()