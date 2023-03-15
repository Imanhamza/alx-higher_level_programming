#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
/**
 * print_python_list - print some basic info about Python lists
 * @p: PyObject
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	PyObject *in_list;

	if (PyList_Check(p))
	{
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < PyList_Size(p); i++)
		{
			in_list = PySequence_GetItem(p, i);
			printf("Element %lu: %s\n", i,
					in_list->ob_type->tp_name);
			if (strcmp(in_list->ob_type->tp_name, "bytes") == 0)
				print_python_bytes(in_list);
		}
	}
}
/**
 * print_python_bytes - prints some basic info about python bytes
 * @p: python object
 * Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	const int MAX_BYTES = 10;
	char *bytes;
	Py_ssize_t size;
	
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid bytes object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &bytes, &size);
	printf("Size: %zd\n", size);
	printf("Contents: ");
	for (int i = 0; i < size && i < MAX_BYTES; i++)
	{
		printf("%02x ", bytes[i] & 0xFF);
	}
	if (size > MAX_BYTES)
	{
		printf("...");
	}
	printf("\n");
}
