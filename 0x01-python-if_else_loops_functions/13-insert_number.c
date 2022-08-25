#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *current, *new;

    current = *head;
    if (!head)
        return (NULL);

    new = malloc(sizeof(listint_t));
    if (!new)
        return (NULL);

    new->n = number;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else if (number < current->n)
    {
        new->next = current;
        *head = new;
    }
    else
    {
        while (current->next)
        {
            if (number > current->next->n)
                current = current->next;
            else
                break;
        }

        new->next = current->next;
        current->next = new;
    }

    return (new);
}