def main():
    x, y, z = input("Expression: ").split(" ")

    output = None

    interpret(x, y, z, output)
    print(output)


def interpret(a, b, c, calc):
    match b:
        case "+":
            calc = round(float(a) + float(c), 1)
            print(calc)
        case "-":
            calc = round(float(a) - float(c), 1)
            print(calc)
        case "*":
            calc = round(float(a) * float(c), 1)
            print(calc)
        case "/":
            calc = round(float(a) / float(c), 1)
            print(calc)


main()
