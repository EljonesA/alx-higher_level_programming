#include "lists.h"

/**
 * check_cycle - determines if a singly linked list has a cycle
 * @list: pointer to beginning of linked list
 * Return: 0(no cycle), 1(cycle)
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast) /* cycle present */
			return (1);
	}
	return (0); /* No cycle */
}
