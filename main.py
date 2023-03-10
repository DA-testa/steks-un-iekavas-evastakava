from collections import  namedtuple
import os

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
            
        if next in ")]}":
            if not  are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            opening_brackets_stack.pop()
    
      
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
            
    return "Success"

def main():
    choise = input("Enter F to choose file or I to choose input: ")
    choise = choise.strip()
    if (choise == "F"):
        file_name = input("Enter file name: ")
        if os.path.isfile(file_name):
            with open(file_name) as f:
                text = f.read()
        else:
            print("File does not exist.")
            return
    elif (choise == "I"):
        text = input("Enter brackets: ")
    else:
        print("Invalid choice " + choise)
        return
    new_func(text)


def new_func(text):
    
    result = find_mismatch(text)
    print(result)


if __name__ == "__main__":
    main()
