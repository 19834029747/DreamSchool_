

def SubSeq_MinI(source, target):
    s_count = 0   # 初始化子序列的计数
    t_index = 0   # 初始化目标字符串的索引

    while t_index < len(target):
        c_index = t_index   # 当前目标索引

        # source每个字符
        for char in source:
            # 字符与目标字符匹配
            if t_index < len(target) and char == target[t_index]:
                t_index += 1

        # 没有匹配任务
        if c_index == t_index:
            return -1
        s_count += 1     # 增加子序列的计数

    return s_count