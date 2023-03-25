def ascii():
    string = input("Enter the string :")
    ascii_code = {chr(i): i for i in range(0, 256)}
    temp = lambda x, ascii_code: ascii_code[x]
    print("List of ASCII codes :")
    print([temp(string[i], ascii_code) for i in range(len(string))])


ascii()

"vinoth"

"logesh"


