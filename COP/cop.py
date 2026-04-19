class TAC:
    def __init__(self, op, arg1, arg2, result):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result


# ---------------------------------------
# DISPLAY FUNCTION
# ---------------------------------------
def display(code):
    print("\nThree Address Code:")
    for ins in code:
        if ins.op == '=':
            print(f"{ins.result} = {ins.arg1}")
        else:
            print(f"{ins.result} = {ins.arg1} {ins.op} {ins.arg2}")


# ---------------------------------------
# CHECK NUMBER
# ---------------------------------------
def is_number(x):
    return x.isdigit()


# ---------------------------------------
# 1. CONSTANT FOLDING
# ---------------------------------------
def constant_folding():
    code = [
        TAC('+', '2', '3', 't1'),
        TAC('*', '4', '5', 't2')
    ]

    print("\n===== CONSTANT FOLDING =====")
    print("\nBefore Optimization:")
    display(code)

    for ins in code:
        if is_number(ins.arg1) and is_number(ins.arg2):

            a = int(ins.arg1)
            b = int(ins.arg2)

            if ins.op == '+':
                res = a + b
            elif ins.op == '*':
                res = a * b

            ins.arg1 = str(res)
            ins.arg2 = ""
            ins.op = '='

    print("\nAfter Optimization:")
    display(code)


# ---------------------------------------
# 2. STRENGTH REDUCTION
# ---------------------------------------
def strength_reduction():
    code = [
        TAC('*', 'a', '2', 't1'),
        TAC('*', 'b', '4', 't2')
    ]

    print("\n===== STRENGTH REDUCTION =====")
    print("\nBefore Optimization:")
    display(code)

    for ins in code:

        if ins.op == '*':

            if ins.arg2 == '2':
                ins.op = "<<"
                ins.arg2 = '1'

            elif ins.arg2 == '4':
                ins.op = "<<"
                ins.arg2 = '2'

    print("\nAfter Optimization:")
    display(code)


# ---------------------------------------
# 3. COMMON SUBEXPRESSION
# ---------------------------------------
def common_subexpression():
    code = [
        TAC('*', 'b', 'c', 't1'),
        TAC('*', 'b', 'c', 't2'),
        TAC('+', 't1', 'd', 't3')
    ]

    print("\n===== COMMON SUBEXPRESSION ELIMINATION =====")
    print("\nBefore Optimization:")
    display(code)

    for i in range(len(code)):
        for j in range(i + 1, len(code)):

            if (code[i].arg1 == code[j].arg1 and
                code[i].arg2 == code[j].arg2 and
                code[i].op == code[j].op):

                code[j].arg1 = code[i].result
                code[j].arg2 = ""
                code[j].op = '='

    print("\nAfter Optimization:")
    display(code)


# ---------------------------------------
# 4. DEAD CODE ELIMINATION
# ---------------------------------------
def dead_code_elimination():

    code = [
        "i = 0",
        "if (i == 1):",
        "a = x + 5",
        "print(i)"
    ]

    print("\n===== DEAD CODE ELIMINATION =====")
    print("\nBefore Optimization:")

    for line in code:
        print(line)

    optimized = []

    i = 0
    while i < len(code):

        line = code[i]

        if line == "if (i == 1):":

            condition = False

            if condition:
                optimized.append(line)
                optimized.append(code[i + 1])

            i += 2
            continue

        optimized.append(line)
        i += 1

    print("\nAfter Optimization:")

    for line in optimized:
        print(line)


# ---------------------------------------
# MAIN
# ---------------------------------------
constant_folding()
strength_reduction()
common_subexpression()
dead_code_elimination()