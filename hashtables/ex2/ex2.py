#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    '''
    load all ticket key, value pairs in a hash table
    we can load the ticket with a source of 'NONE' at 
    the start of the route array since we know where it goes
    '''
    for i in range(length):
        # tkt w/source of NONE goes at the start of the array
        if tickets[i].source == 'NONE':
            route[0] = tickets[i].destination
        hash_table_insert(ht, tickets[i].source, tickets[i].destination)

    for j in range(length):
        # print(j-1, route[j-1])
        if route[j-1] is not None:
            # get next array value by sending the key (source) and getting back the value (destination)
            route[j] = hash_table_retrieve(ht, route[j-1])

    return route
