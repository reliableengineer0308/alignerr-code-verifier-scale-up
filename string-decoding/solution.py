def decode_string(s):
    stack = []
    current_num = 0
    current_str = ""
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Push current string and number to stack
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == ']':
            # Pop from stack and build current string
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            # Normal character
            current_str += char
    
    return current_str