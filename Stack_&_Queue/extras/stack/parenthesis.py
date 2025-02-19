
def isValid( s: str) -> bool:
    mapping = {
        '(':')',
        '[':']',
        '{':'}'
    }

    stack = []

    for char in s:
        if char in mapping:
            stack.append(char)
        elif char in mapping.values():
            if not stack or mapping[stack.pop()] != char:
                return False
        else:
            return False

    return not stack

print(isValid('()()'))
print(isValid('()())'))