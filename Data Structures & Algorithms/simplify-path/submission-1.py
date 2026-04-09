class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split('/')
        stk = []
        for c in split_path:
            if c == '..':
                if stk:
                    stk.pop()
            elif c != '' and c != '.':
                stk.append(c)
        return '/' + '/'.join(stk)