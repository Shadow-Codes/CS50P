def main():
    your_input = input("Your input: ")
    print(convert(your_input))


def convert(string):
    string = string.replace(":)", "🙂")
    string = string.replace(":(", "🙁")
    return string


main()
