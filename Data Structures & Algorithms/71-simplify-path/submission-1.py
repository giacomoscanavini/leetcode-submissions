class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/')
        stack = []

        for component in components:
            if component == '' or component == '.': continue
            if component == '..': 
                if len(stack) > 0: stack.pop(-1)
            else: stack.append(component)

        return '/' + '/'.join(stack)