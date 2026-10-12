class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = [asteroids[0]]

        i = 1
        while i < len(asteroids):
            if len(stack) == 0: 
                stack.append(asteroids[i])
                i += 1
            
            else:
                if stack[-1] > 0 and asteroids[i] < 0: 
                    if abs(stack[-1]) > abs(asteroids[i]): 
                        i += 1
                    elif abs(stack[-1]) == abs(asteroids[i]):
                        stack.pop(-1)
                        i += 1
                    else:
                        stack.pop(-1)

                else:
                    stack.append(asteroids[i])
                    i += 1

        return stack