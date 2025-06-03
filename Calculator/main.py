def add (n1,n2):
    return n1 + n2


def substract(n1,n2):
    return n1 - n2


def multiply(n1,n2):
    return n1 * n2


def devided(n1,n2):
    return n1 / n2


operations = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":devided,
}
def calculator():
    should_accumulate = True
    num1 = float(input("Whats is the first number?: "))
    while should_accumulate:

        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Whats is the next number?: "))
        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation ")
        if choice == "y":
            num1 = answer
        else:
            break
calculator()