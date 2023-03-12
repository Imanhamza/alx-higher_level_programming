#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: PyObject
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *ob;

	/* get the size of the list */
	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	/* Get the allocated memory */
	List = (PyListObject *)p;
	print("[*] Allocated = %ld\n", list->allocated);

	/* Get all the elements' type in the list*/
	for (i = 0; i < size; i++)
	{
		ob = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(ob)->tp_name);
	}
}
