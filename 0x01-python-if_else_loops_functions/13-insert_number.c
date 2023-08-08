#include "lists.h"
#include <stdlib.h>

/**
 * inseert_node - inserts a number into a sorted linked list
 * @head: pointer to beginning of list
 * @number: the number to be inserted in the list
 *
 * Description: insert_node number insertion
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	listint_t *current = *head;

	while (current->next != NULL && current->next->n < number)
		current = current->next;
	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
