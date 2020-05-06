#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Determine if is polindrome
 * @p: list
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t aux, length;
	PyListObject *l;
	PyObject *item;
	PyVarObject *o;

	l = (PyListObject *)p;
	o = (PyVarObject *)p;
	length = Py_SIZE(o);
	printf("[*] Size of the Python List = %li\n", length);
	printf("[*] Allocated = %li\n", l->allocated);

	for (aux = 0; aux < length; aux++)
	{
		item = PyList_GetItem(p, aux);
		printf("Element %li: %s\n", aux, Py_TYPE(item)->tp_name);
	}
}
