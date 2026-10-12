class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num_stack = []
        substring = ''

        i = 0
        while i < len(s):
            if s[i].isdigit(): 
                if s[i : i+3].isdigit(): 
                    num_stack.append(int(s[i : i+3]))
                    i += 3
                elif s[i : i+2].isdigit(): 
                    num_stack.append(int(s[i : i+2]))
                    i += 2
                else: 
                    num_stack.append(int(s[i : i+1]))
                    i += 1

            else:
                if s[i] == '[':
                    stack.append(s[i])
                    i += 1
                elif s[i] == ']':
                    while stack[-1] != '[':
                        top = stack.pop(-1)
                        substring = top + substring
                    stack.pop(-1)
                    num = num_stack.pop(-1)
                    stack.append(num * substring)

                    substring = ''
                    i += 1

                else:
                    stack.append(s[i])
                    i += 1

        return "".join(stack)