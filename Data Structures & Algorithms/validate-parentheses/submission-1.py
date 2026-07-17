class Solution:
    def isValid(self, s: str) -> bool:
        paran = []
        for char in s:
            match char:
                case '(':
                    paran.append(char)
                case '[':
                    paran.append(char)
                case '{':
                    paran.append(char)
                case ')':
                    if len(paran) == 0 or paran.pop() != '(':
                        return False
                case ']':
                    if len(paran) == 0 or paran.pop() != '[':
                        return False
                case '}':
                    if len(paran) == 0 or paran.pop() != '{':
                        return False
                case _:
                    return False
        return len(paran) == 0

        