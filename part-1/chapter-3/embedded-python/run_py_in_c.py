import os

os.system('gcc -I/usr/include/python3.8 run_py_in_c.c -lpython3.8')
os.system('./a.out')
