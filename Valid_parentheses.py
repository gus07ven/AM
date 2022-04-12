
def valid_parentheses(s: str) -> bool:
    valid_map = {'{': '}', '(': ')', '[': ']'}
    stack = []

    for char in s:
        if char in valid_map:
            stack.append(char)
        else:
            if stack and valid_map[stack[-1]] == char:
                stack.pop()
            else:
                return False

    return False if stack else True


if __name__ == '__main__':
    input = '()'
    print(valid_parentheses(input))

    input2 = '[{)]'
    print(valid_parentheses(input2))