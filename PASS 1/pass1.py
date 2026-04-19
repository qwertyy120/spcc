MNT = []
MDT = []
ALA = []

MNTC = 1
MDTC = 1


def print_line():
    print("-" * 50)


def pass1(source_code):
    global MNTC, MDTC

    intermediate_code = []
    i = 0

    while i < len(source_code):

        line = source_code[i].strip()

        if line == "":
            i += 1
            continue

        if line == "MACRO":

            i += 1
            header = source_code[i].strip()

            parts = header.split()

            if len(parts) == 3:
                label = parts[0]
                macro_name = parts[1]
                arguments = parts[2]

            elif len(parts) == 2:
                label = ""
                macro_name = parts[0]
                arguments = parts[1]

            else:
                label = ""
                macro_name = parts[0]
                arguments = ""

            MNT.append((MNTC, macro_name, MDTC))
            MNTC += 1

            ALA.clear()

            if label != "":
                ALA.append(label)

            if arguments != "":
                args = arguments.split(',')

                for arg in args:
                    ALA.append(arg.strip())

            MDT.append((MDTC, header))
            MDTC += 1

            i += 1

            while source_code[i].strip() != "MEND":

                body = source_code[i].strip()

                for index, arg in enumerate(ALA):
                    body = body.replace(arg, f"#{index+1}")

                MDT.append((MDTC, body))
                MDTC += 1

                i += 1

            MDT.append((MDTC, "MEND"))
            MDTC += 1

        else:
            intermediate_code.append(line)

        i += 1

    return intermediate_code


with open("input.txt", "r") as file:
    source_code = file.readlines()

intermediate = pass1(source_code)

print("\n===== PASS-1 OF TWO PASS MACRO PROCESSOR =====")

print("\nSOURCE PROGRAM:")
print_line()
for line in source_code:
    print(line.strip())

print("\nINTERMEDIATE CODE:")
print_line()
for line in intermediate:
    print(line)

print("\nMNT (MACRO NAME TABLE):")
print_line()
print("Index\tMacro Name\tMDT Index")
for row in MNT:
    print(row[0], "\t", row[1], "\t\t", row[2])

print("\nMDT (MACRO DEFINITION TABLE):")
print_line()
print("Index\tCard")
for row in MDT:
    print(row[0], "\t", row[1])

print("\nALA (ARGUMENT LIST ARRAY):")
print_line()
print("Index\tArgument")
for i, arg in enumerate(ALA, start=1):
    print(i, "\t", arg)

print("\nCOUNTERS:")
print_line()
print("MNTC =", MNTC - 1)
print("MDTC =", MDTC - 1)
