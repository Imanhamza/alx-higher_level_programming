#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of alinked list
 * Return:0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	/* Handle empty or single node list */
	if (head == NULL || *head == NULL)
		return (1);
	listint_t *slow = *head,
		  *fast = *head;
	/* Find the middle node */
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	/*reverse the list */
	listint_t *prev = NULL,
		  *current = slow,
		  *next;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	/* compare the first and secod halves */
	listint_t *node1 = *head,
		  *node2 = prev;
	while (node1 != NULL && node2 != NULL)
	{
		if (node1->n != node2->n)
			return (0);
		node1 = node1->next;
		node2 = node2->next;
	}
	return (1);
}
