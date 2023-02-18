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
    user_input = input("Choose F to input from file or I to input brackets: ")
    if user_input == "F":
        filename = input("Enter file name: ")
        with open(filename) as f:
            text = f.read().strip()
    elif user_input == "I":
        text = input("Enter brackets: ")
    else: 
        print("Invalid input")
        return
    mismatch = find_mismatch(text)
    if mismatch == "Success":
        print(mismatch)
    else:
        print(mismatch)

if __name__ == "__main__":
    main()
