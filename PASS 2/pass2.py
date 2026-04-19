MNT = []
MDT = []
LAST_ALA = []


def print_line():
    print("-" * 50)


def read_mnt():
    with open("mnt.txt", "r") as file:
        for line in file:
            line = line.strip()

            if line != "":
                parts = line.split()
                MNT.append((parts[0], int(parts[1])))


def read_mdt():
    with open("mdt.txt", "r") as file:
        for line in file:
            line = line.strip()

            if line != "":
                MDT.append(line)


def read_ic():
    code = []

    with open("ic.txt", "r") as file:
        for line in file:
            line = line.strip()

            if line != "":
                code.append(line)

    return code


def macro_names():
    names = []

    for item in MNT:
        names.append(item[0])

    return names


def expand_macro(line):
    global LAST_ALA

    words = line.split()

    if len(words) == 0:
        return [line]

    names = macro_names()

    label = ""
    macro_name = ""
    operands = ""

    if words[0] in names:
        macro_name = words[0]

        if len(words) > 1:
            operands = words[1]

    elif len(words) >= 2 and words[1] in names:
        label = words[0]
        macro_name = words[1]

        if len(words) > 2:
            operands = words[2]

    else:
        return [line]

    pos = -1

    for i in range(len(MNT)):
        if MNT[i][0] == macro_name:
            pos = i
            break

    if pos == -1:
        return [line]

    ALA = []

    if label != "":
        ALA.append(label)

    if operands != "":
        args = operands.split(",")

        for arg in args:
            ALA.append(arg.strip())

    LAST_ALA = ALA.copy()

    mdtp = MNT[pos][1]

    output = []

    while mdtp < len(MDT):

        card = MDT[mdtp]

        if card == "MEND":
            break

        temp = card

        for i in range(len(ALA)):
            temp = temp.replace(f"#{i+1}", ALA[i])

        output.append(temp)
        mdtp += 1

    return output


def pass2(ic):
    expanded = []

    for line in ic:
        result = expand_macro(line)

        for item in result:
            expanded.append(item)

    return expanded


def print_tables():
    print("\nMNT TABLE")
    print_line()
    print("Index\tMacro Name\tMDT Index")

    for i in range(len(MNT)):
        print(i + 1, "\t", MNT[i][0], "\t\t", MNT[i][1])

    print("\nMDT TABLE")
    print_line()
    print("Index\tCard")

    for i in range(len(MDT)):
        print(i + 1, "\t", MDT[i])

    print("\nALA TABLE")
    print_line()
    print("Index\tArgument")

    for i in range(len(LAST_ALA)):
        print(i + 1, "\t", LAST_ALA[i])


read_mnt()
read_mdt()
IC = read_ic()

expanded_code = pass2(IC)

print("\n===== PASS-2 OF TWO PASS MACRO PROCESSOR =====")

print("\nINTERMEDIATE CODE")
print_line()

for line in IC:
    print(line)

print("\nEXPANDED CODE")
print_line()

for line in expanded_code:
    print(line)

print_tables()