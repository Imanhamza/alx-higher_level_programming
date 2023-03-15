#include <python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints some basic info about python bytes
 * @p: python object
 * Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	Py_size_t len,
		  i;
	/* check if the *p is a 'o' or not */
	if (!(Py_bytes_check(*p)))
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
		printf("%02x\n", s[len - 1] & 0xff);
	}
}
/**
 * print_python_list - print some basic info about Python lists
 * @p: python object
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
}
