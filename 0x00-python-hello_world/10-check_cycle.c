#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
/**
 * check_cycle - checks a linked list for a cycle / loop
 * @list: pointer to linked list
 * Return: int 0 if no loop 1 if loop detected
 */
int check_cycle(listint_t *list)
{
	const listint_t *torty, *harry;

	torty = list;
	harry = list;
	
	while(totry->next != NULL && harry->next->next != NULL)
	{
		torty = torty->next;
		harry = harry->next->next;
		if (torty == harry)
			return (1);
	}
	return (0);
}
