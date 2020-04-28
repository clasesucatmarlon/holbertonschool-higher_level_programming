#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node at a given index
 * @head: double pointer to head node
 * @number: value of new node
 *
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *prev;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;
	prev = NULL;
	current = *head;

	while (current && current->n < number)
	{
		prev = current;
		current = current->next;
	}
	new->next = current;
	if (prev)
		prev->next = new;
	else
		*head = new;
	return (new);
}
