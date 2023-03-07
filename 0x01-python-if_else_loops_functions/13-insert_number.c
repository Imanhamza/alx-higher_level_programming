#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: A pointer to the head of the linked list
 * @number: the integer to be insrted
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode,
		  *current = *head,
		  *prev = NULL;
	if (head == NULL)
		return (NULL);

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	while (current != NULL)
	{
		if (current->n > number)
			break;
		prev = current;
		current = current->next;
	}
	newNode->n = number;
	if (prev == NULL)
	{
		newNode->next = current;
		*head = newNode;
		return (newNode);
	}
	prev->next = newNode;
	newNode->next = current;

	return (current);
}
