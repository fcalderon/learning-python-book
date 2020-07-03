#include <stdio.h>
#include <Python.h>

int main() {
  printf("Running python from C...");
  Py_Initialize();
  PyRun_SimpleString("x = 'I am ' + 'Python3.8'");
  PyRun_SimpleString("print(x)");


  return 0;
}
