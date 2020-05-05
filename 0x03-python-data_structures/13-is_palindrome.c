#include "lists.h"

/**
 * is_palindrome - Determine if is polindrome
 * @head: pointer at first node
 * Return: 0 if not is polindrome else 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *aux1 = *head, *aux2 = *head;
	int m = 0, middle, mmm, k;

	if (!*head)
		return (1);

	while (aux1->next)
	{
		aux1 = aux1->next;
		m++;
	}
	if (aux1->n != (*head)->n)
		return (0);
	if (m == 1)
		return (1);

	middle = m / 2;
	mmm = m - 2;

	m = 0;
	while (m < middle)
	{
		aux2 = aux2->next;
		aux1 = aux2;
		for (k = 0; k < mmm; k++)
			aux1 = aux1->next;
		if (aux2->n != aux1->n)
			return (0);
		m++;
		mmm = mmm - 2;
	}
	return (1);
}
