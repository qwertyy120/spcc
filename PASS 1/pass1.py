# PASS-1 OF TWO PASS MACRO PROCESSOR
# Reads Source Code from input.txt

# ---------------- DATA STRUCTURES ----------------
MNT = []        # Macro Name Table -> (Index, Macro Name, MDT Index)
MDT = []        # Macro Definition Table
ALA = []        # Argument List Array

MNTC = 1        # MNT Counter
MDTC = 1        # MDT Counter


# ---------------- DISPLAY FUNCTION ----------------
def print_line():
    print("-" * 50)


# ---------------- PASS-1 FUNCTION ----------------
def pass1(source_code):
    global MNTC, MDTC

    intermediate_code = []
    i = 0

    while i < len(source_code):

        line = source_code[i].strip()

        # Ignore blank lines
        if line == "":
            i += 1
            continue

        # Check MACRO
        if line == "MACRO":

            i += 1
            header = source_code[i].strip()

            parts = header.split()

            # Header Example:
            # &LAB INCR &ARG1,&ARG2,&ARG3

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

            # Enter into MNT
            MNT.append((MNTC, macro_name, MDTC))
            MNTC += 1

            # Build ALA
            ALA.clear()

            if label != "":
                ALA.append(label)

            if arguments != "":
                args = arguments.split(',')

                for arg in args:
                    ALA.append(arg.strip())

            # Store Header in MDT
            MDT.append((MDTC, header))
            MDTC += 1

            i += 1

            # Read Macro Body
            while source_code[i].strip() != "MEND":

                body = source_code[i].strip()

                # Replace Arguments by Positional Notation
                for index, arg in enumerate(ALA):
                    body = body.replace(arg, f"#{index+1}")

                MDT.append((MDTC, body))
                MDTC += 1

                i += 1

            # Store MEND
            MDT.append((MDTC, "MEND"))
            MDTC += 1

        else:
            intermediate_code.append(line)

        i += 1

    return intermediate_code


# ---------------- MAIN PROGRAM ----------------

# Read Source Code from input.txt
with open("input.txt", "r") as file:
    source_code = file.readlines()

# Run Pass-1
intermediate = pass1(source_code)

# ---------------- OUTPUT ----------------

print("\n===== PASS-1 OF TWO PASS MACRO PROCESSOR =====")

# Source Code
print("\nSOURCE PROGRAM:")
print_line()
for line in source_code:
    print(line.strip())

# Intermediate Code
print("\nINTERMEDIATE CODE:")
print_line()
for line in intermediate:
    print(line)

# MNT
print("\nMNT (MACRO NAME TABLE):")
print_line()
print("Index\tMacro Name\tMDT Index")
for row in MNT:
    print(row[0], "\t", row[1], "\t\t", row[2])

# MDT
print("\nMDT (MACRO DEFINITION TABLE):")
print_line()
print("Index\tCard")
for row in MDT:
    print(row[0], "\t", row[1])

# ALA
print("\nALA (ARGUMENT LIST ARRAY):")
print_line()
print("Index\tArgument")
for i, arg in enumerate(ALA, start=1):
    print(i, "\t", arg)

# Counters
print("\nCOUNTERS:")
print_line()
print("MNTC =", MNTC - 1)
print("MDTC =", MDTC - 1)