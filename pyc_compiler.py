import py_compile
file = input("Enter filename with extension: ")
try:
    py_compile.compile(f'{file}')
    print("Check __pycache__ folder")
except py_compile.PyCompileError as err:
    print("Error: ", err)
except FileNotFoundError as err:
    print("Error: ", err)
except Exception as err:
    print("Error: ", err)
