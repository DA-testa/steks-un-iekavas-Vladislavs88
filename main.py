class Bracket:
    def __init__(self, type, position):
        self.type = type
        self.position = position

    def match(self, c):
        if self.type == '[' and c == ']':
            return True
        if self.type == '{' and c == '}':
            return True
        if self.type == '(' and c == ')':
            return True
        return False

text = input()

opening_brackets_stack = []
for position in range(len(text)):
    next = text[position]

    if next in ['(', '[', '{']:
        # Process opening bracket, write your code here
        opening_brackets_stack.append(Bracket(next, position + 1))

    if next in [')', ']', '}']:
        # Process closing bracket, write your code here
        if not opening_brackets_stack or not opening_brackets_stack[-1].match(next):
            print(position + 1)
            exit()
        opening_brackets_stack.pop()

# Printing answer, write your code here
if not opening_brackets_stack:
    print("Success")
else:
    print(opening_brackets_stack[-1].position)
