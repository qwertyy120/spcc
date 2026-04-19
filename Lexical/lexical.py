code = r"""#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cout << "Enter first number";
    c = a + b;
    cout << "Sum = ";
    return 0;
}"""

keywords_list = [
    "int", "float", "return", "if", "else", "using",
    "namespace", "std", "include", "char", "double", "void"
]

keywords = []
identifiers = []
numbers = []
operators = []
separators = []
literals = []

i = 0

while i < len(code):

    if code[i].isspace():
        i += 1
        continue

    if code[i] == '#':
        i += 1
        continue

    if code[i] == '"':
        i += 1
        literal = ""

        while i < len(code) and code[i] != '"':
            literal += code[i]
            i += 1

        i += 1

        if literal not in literals:
            literals.append(literal)

        continue

    if code[i].isalpha() or code[i] == '_':
        word = ""

        while i < len(code) and (code[i].isalnum() or code[i] == '_'):
            word += code[i]
            i += 1

        if word in keywords_list:
            if word not in keywords:
                keywords.append(word)
        else:
            if word not in identifiers:
                identifiers.append(word)

        continue

    if code[i].isdigit():
        num = ""

        while i < len(code) and code[i].isdigit():
            num += code[i]
            i += 1

        if num not in numbers:
            numbers.append(num)

        continue

    two_char = code[i:i+2]

    if two_char in ["<<", ">>", "==", "!=", "<=", ">="]:
        if two_char not in operators:
            operators.append(two_char)

        i += 2
        continue

    if code[i] in "+-*/=<>":
        if code[i] not in operators:
            operators.append(code[i])

        i += 1
        continue

    if code[i] in ";(){}[],":
        if code[i] not in separators:
            separators.append(code[i])

        i += 1
        continue

    i += 1


print("\nKeywords:")
for x in keywords:
    print(x)
print("\nCount =", len(keywords))

print("\nIdentifiers:")
for x in identifiers:
    print(x)
print("\nCount =", len(identifiers))

print("\nNumbers:")
for x in numbers:
    print(x)
print("\nCount =", len(numbers))

print("\nLiterals:")
for x in literals:
    print(f'"{x}"')
print("\nCount =", len(literals))

print("\nOperators:")
for x in operators:
    print(x)
print("\nCount =", len(operators))

print("\nSeparators:")
for x in separators:
    print(x)
print("\nCount =", len(separators))