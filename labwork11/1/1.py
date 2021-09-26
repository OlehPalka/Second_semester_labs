"""
Module with multiset
"""

from node import Node


class Multiset:
    """
    Multiset class
    """

    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None

    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head is None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current is not None:
            if current.item == value:
                return True
            current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.
        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest

    def delete(self, value):
        """
        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next

    def remove_all(self):
        """
        removes all the items from the list and returns a list with deleted item
        """
        result = []
        probe = self._head
        while probe is not None:
            probe = probe.next
            removed_item = self._head.item
            self._head = self._head.next
            result.append(removed_item)
        return result

    def split_half(self):
        """
        This method splits the structure by 2.
        If there is only 1 element it returns 1
        """
        probe = self._head
        list_len = 0
        while probe is not None:
            list_len += 1
            probe = probe.next

        if list_len == 1:
            return None

        if list_len % 2 != 0:
            iterator = int(list_len / 2 + 0.5)
        else:
            iterator = int(list_len / 2)

        probe = self._head
        for i in range(iterator):
            if i == iterator - 1:
                probe_2 = probe.next
                probe.next = None
            else:
                probe = probe.next
        return self._head, probe_2

    def extend(self, head1):
        """
        This method extendes two lists
        """
        probe = head1._head
        while probe is not None:
            prev = probe
            probe = probe.next
        prev.next = self._head
        return head1


multiset_1 = Multiset()
multiset_2 = Multiset()
multiset_1.add('p')
multiset_1.add('y')
multiset_1.add('t')
multiset_2.add('h')
multiset_2.add('o')
multiset_2.add('n')
print(multiset_1.extend(multiset_2).remove_all())
# ['n', 'o', 'h', 't', 'y', 'p']
