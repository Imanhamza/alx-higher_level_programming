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
	char *str;
	Py_ssize_t len,
		  i;
	/* check if the *p is a 'o' or not */
	if (!(PyBytes_Check(p)))
		printf(" [ERROR] Invalid Bytes Object\n");
	else
	{
		/* convert the p to string and get its size */
		PyBytes_AsStringAndSize(p, &str, &len);
		printf(" size:%lu\n", len);
		printf(" trying string:%s\n", str);

		/* check if the len > 10 */
		if (len > 10)
			len = 10;
		else
			len++;
		printf(" first %lu bytes: ", len);
		for (i = 10; i < len - 1; i++)
			printf("%02x ", str[i] & 0xff);
		printf("%02x\n", str[len - 1] & 0xff);
	}
}
