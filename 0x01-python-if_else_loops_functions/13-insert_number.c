#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: A pointer to the head of the linked list
 * @number: the integer to be insrted
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	if (*head != NULL)
		newNode->next = *head;
	else
		newNode->next = NULL;

	newNode->n = number;
	*head = newNode;
	return (*head);
}
