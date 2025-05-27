"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
"""

"""
使用栈+预测思想：
1.匹配左括号压入与之匹配的右括号  
2.s中的下一个字符与出栈的期望（匹配栈顶）不符则返回False  
3.所有栈中元素全部出栈完毕则返回True

现象化的例子
女友 A 出站，预测 男友a之后会下车，但不知道什么时候 → 栈：['a']
女友 B 出站，预测 b → 栈：['a', 'b']
女友 C 出站，预测 c → 栈：['a', 'b', 'c']
男友 c 出站，匹配 → 匹配成功，栈：['a', 'b']
男友 b 出站，匹配 → 匹配成功，栈：['a']
男友 a 出站，匹配 → 匹配成功，栈：[]
"""
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False

        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            elif not stack or stack.pop() != char:
                return False

        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()
    s = "()[]{}"
    print(s, solution.isValid(s))  # True
    s = "(]"
    print(s, solution.isValid(s))  # False
    s = "([)]"
    print(s, solution.isValid(s))  # False
    s = "{[]}"
    print(s, solution.isValid(s))  # True
    s = "()[]{}["
    print(s, solution.isValid(s))  # False
    s = "()[]{}[*"
    print(s, solution.isValid(s))  # False
