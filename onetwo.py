# 导入math模块
import math

# 声明输入要求
print('声明:须化为一般式再进行输入!!!')


# 设置函数quadratic_equation_with_one_unknown，用于解一元二次方程
def quadratic_equation_with_one_unknown(a, b, c):
    # 计算判别式delta
    delta = b ** 2 - (4 * a * c)
    # 判断delta的值
    if delta > 0:
        # 当delta大于0时，方程有两个不同的实根
        x1 = (-b + math.sqrt(delta)) / (2 * a)  # 这是第一个解
        x2 = (-b - math.sqrt(delta)) / (2 * a)  # 这是第二个解
        print(f'所以，原方程的解为，x1 = {x1} ,x2 = {x2}')
    elif delta == 0:
        # 当delta等于0时，方程有两个相同的实根（即一个实根）
        x = -b / (2 * a)  # 注意这里的括号，确保除法优先
        print(f'所以，原方程的解为，x = {x}')
    else:
        # 当delta小于0时，方程无实数根
        print('原方程无实数根')

# 设置函数check，用于检查并转换输入为浮点数
def check(number):
    while True:
        try:
            # 尝试将输入转换为浮点数并返回
            return float(number)
        except ValueError:
            # 如果转换失败，提示用户重新输入
            number = input('请重新输入')

        # 设置主循环，用于不断请求用户输入并处理


while True:
    # 请求用户输入a的值，并调用check函数获取转换后的浮点数
    a = check(input('请输入a的值'))
    # 同上，对b和c的值进行相同的操作
    b = check(input('请输入b的值'))
    c = check(input('请输入c的值'))
    # 调用quadratic_equation_with_one_unknown函数解方程，此时传递的是浮点数
    quadratic_equation_with_one_unknown(a, b, c)
    # 请求用户输入是否停止运行
    s = input('输入y停止运行')
    if s == 'y':
        break  # 如果用户输入y，则退出循环
# 有没有好心人能帮帮我......