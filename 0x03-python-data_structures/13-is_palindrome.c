#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of alinked list
 * Return:0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;

	return (check_pal(&temp, *head));
}

/**
 * check_pal - helper function to check if the list is a palindrome
 * @left: pointer to the left end of the list
 * @right: pointer to the right end of the list
 * Return: 1 if is palindrome 0 if not
 */
int check_pal(listint_t **left, listint_t *right)
{
	int is_pal;

	/* base case: end of list */
	if (right == NULL)
		return (1);

	/* check if the rest of the list is a palindrome */
	is_pal = check_pal(left, right->next);

	if (is_pal == 0)
		return (0);

	/* check if the current elements are the same */
	is_pal = ((*left)->n == right->n);
	/* move left pointer to the next element */
	*left = (*left)->next;

	return (is_pal);
}
