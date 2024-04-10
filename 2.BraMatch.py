
def Bra_Match(strings):
    res = []
    for string in strings:
        # 初始化左右括号数量
        l_bra = 0
        r_bra = 0
        blank = [' ' for _ in string]  # 填入空字符串中
        # 加括号过程
        for i, char in enumerate(string):
            if char == '(':
                l_bra += 1
            elif char == ')':
                if l_bra > 0:
                    l_bra -= 1
                else:
                    blank[i] = '?'

        # 逆序加x过程
        for i in range(len(string) - 1, -1, -1):
            if string[i] == '(' and l_bra > 0:
                blank[i] = 'x'
                l_bra -= 1

        res.append(string + '\n' + ''.join(blank))

    return res