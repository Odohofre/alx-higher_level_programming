#include <Python.h>
/**
 * print_python_list_info - Prints information about python objects
 * @p: PyObject pointer to print info about
 * Compile with:
 * gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared
 (* -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4
 (* 100-print_python_list_info.c
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, idx;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (idx = 0; idx < size; idx++)
	{
		printf("Element %ld: %s\n",
			   idx,
			   (PY_TYPE(PyList_GetItem(p, idx)))->tp_name);
	}
}
