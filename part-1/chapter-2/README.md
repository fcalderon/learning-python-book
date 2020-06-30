# Chapter 2 Notes

How Python Runs Programs

### On .pyc files

These are python code compiled to byte code and are created for imports. The
python interpreter uses the python version that created the .pyc and the
timestamp of the .pyc compared to the source file to determined when to
recompile. .pyc files are stored in __pycache__ located in the directory where
the source code resides.

Python program/script cycles

Source            Byte code           Runtime
file.py    ===>    file.pyc    ===>    PVM (Python Virtual Machine)

### On Python Implemenation Alternatives

The "default" and standard implementation of Python is known as CPython.

### On "Frozen Binaries"

Frozen binaries are self contained executable files of a Python program. The
package the byte code and PVM, thus not requiring Python.

## Quiz

1. The Python interpreter is the python run time that executes your code. It is
responsible for translating code into byte code and executing it in the PVM.

2. The Python code written by the developer
3. Lower level code compiled by Python. Python automatically stores this code
in a .pyc file.
4. The PVM is Python's runtime engine. It interprets compiled bytecode.
5. Jython, Stackless, PyPy, frozen binaries
6. CPython is the standard implementation of Python, Jython allows Python
source to be compiled to Java binaries, IronPython to .NET.
7. Stackless is primarily for concurrency, and PyPy for number processing.
