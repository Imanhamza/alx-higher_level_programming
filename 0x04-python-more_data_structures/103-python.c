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
	const int MAX_BYTES = 10;
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid list object\n");
		return;
	}
	printf("[*] Python list info\n");
	printf("[*] Size of the Python list = %zd\n", PyList_Size(p));
	printf("[*] Allocated = %zd\n", ((PyListObject *) p)->allocated);
	for (Py_ssize_t i = 0; i < PyList_Size(p); i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		if (!item)
		{
			printf("[ERROR] Failed to retrieve item %zd\n", i);
			continue;
		}
		const char *type_name = Py_TYPE(item)->tp_name;
		printf("Element %zd: %s\n", i, type_name);
		if (strcmp(type_name, "bytes") == 0)
		{
			print_python_bytes(item);
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
