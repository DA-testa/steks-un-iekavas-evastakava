# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))
    
        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
        opening_brackets_stack.pop()
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    return "Success"

def main():
    input_type = input("Enter F for file input or I for user input: ")
    if input_type.strip().upper == "F":
        file_name = input("Enter file name: ")
        if os.file_name.exists(file_name):
            with open(file_name, "r") as file:
            text = file.read()
            mismatch = find_mismatch(text)
            print(mismatch)
    else: 
        print("Invalid file name")
    elif input_type.strip().upper == "I":
        text = input("Enter text: ")
        mismatch = find_mismatch(text)
        print(mismatch)
    else:
        print("Invalid text")

    
    print(mismatch)

if __name__ == "__main__":
    main()
