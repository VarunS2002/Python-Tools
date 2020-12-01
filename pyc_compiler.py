import py_compile
import tkinter
import tkinter.filedialog
import tkinter.messagebox


def get_file() -> None:
    # noinspection PyGlobalUndefined
    global path, finish
    path = tkinter.filedialog.askopenfilename(filetypes=[("Python file", "*.py")])
    if path != '':
        finish.config(state=tkinter.NORMAL)
        print(path)


def compile_file() -> None:
    # noinspection PyGlobalUndefined
    global path, finish
    try:
        py_compile.compile(f'{path}')
        print("Check __pycache__ folder")
        tkinter.messagebox.showinfo('Successful', message='Check __pycache__ folder')
    except py_compile.PyCompileError as err:
        print("Error: ", err)
        tkinter.messagebox.showerror('Error', message=err)
    except FileNotFoundError as err:
        print("Error: ", err)
        tkinter.messagebox.showerror('Error', message=err)
    except Exception as err:
        print("Error: ", err)
        tkinter.messagebox.showerror('Error', message=err)
    finish.config(state=tkinter.DISABLED)


root = tkinter.Tk()
root.title('.pyc Compiler')
frame = tkinter.Frame(root)
path_input = tkinter.Button(frame, text="Choose .py File", command=get_file, width=20)
path_input.grid(row=0, column=0, sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W)
finish = tkinter.Button(frame, text="Compile", command=compile_file, state=tkinter.DISABLED, width=20)
finish.grid(row=0, column=1, sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W)
frame.pack(fill="both", expand=True)
root.mainloop()
