#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list to check
 * Return: 0 if is not loop and 1 if is loop.
 */

int check_cycle(listint_t *list)
{
	listint_t *aux1 = NULL;
	listint_t *aux2 = NULL;

	aux1 = list;
	aux2 = list;

	while (aux1 && aux2)
	{
		aux2 = aux2->next;
		aux1 = aux1->next->next;
		if (aux2 == aux1)
		{
			return (1);
		}
	}
	return (0);
}
