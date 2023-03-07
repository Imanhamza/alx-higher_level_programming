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
		  *current = *head;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;

	if (current == NULL || newNode->n >= number)
	{
		newNode->next = current;
		current = newNode;
		return (newNode);
	}

	while (current && current->next && newNode->next->n < number)
		newNode = newNode->next;

	newNode->next = current->next;
	current->next = newNode;

	return (newNode);
}
