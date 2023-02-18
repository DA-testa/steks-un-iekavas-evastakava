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
    choice = input("Enter F for file input or I for user input: ")
    if choice == "I":
        text = input("Enter brackets: ")
        mismatch = find_mismatch(text)
        print(mismatch)
    elif choice == "F":
        with open("test1.txt") as f:
            for line in f:
                mismatch = find_mismatch(line.strip())
                print(mismatch)
    else:
        print("Invalid choice")

    
    print(mismatch)

if __name__ == "__main__":
    main()
