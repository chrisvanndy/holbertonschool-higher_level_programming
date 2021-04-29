#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks a linked list for a cycle / loop
 * @list: pointer to linked list
 * Return: int 0 if no loop 1 if loop detected
 */
int check_cycle(listint_t *list)
{
	const listint_t *t, *h;

	t = list;
	h = list;

	while (t && h && h->next)
	{
		t = t->next;
		h = h->next->next;
		if (t == h)
			return (1);
	}
	return (0);
}
