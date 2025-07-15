class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    """
    Linked_List class for managing a singly linked list.
    Parameters:
        - None: No parameters are needed for instantiation, initializes with an empty list.
    Processing Logic:
        - Utilizes nodes to construct a linked list, beginning with an empty head.
    """
    def __init__(self):
        self.head = None

    def Insert_At_End(self, new_data):
        """Insert_At_End method to append a new node at the end of a linked list.
        Parameters:
            - new_data (any): The data to be stored in the new node that will be appended to the list.
        Returns:
            - None: This method does not return any value.
        Processing Logic:
            - If the list is empty, the new node becomes the head of the list.
            - Traverse the list until the end to append the new node."""
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def Sort(self):
        """Sort the linked list in ascending order.
        Parameters:
            - self: An instance of the class containing a linked list head node.
        Returns:
            - None: This function modifies the linked list in place and does not return a value.
        Processing Logic:
            - Iteratively selects the minimum element from the unsorted portion of the list.
            - Swaps the selected minimum element with the current element being positioned.
            - Continues until all elements are sorted in ascending order."""
        temp = self.head
        while temp:
            minn = temp
            after = temp.next
            while after:
                if minn.data > after.data:
                    minn = after
                after = after.next
            key = temp.data
            temp.data = minn.data
            minn.data = key
            temp = temp.next

    def Display(self):
        temp = self.head
        while temp:
            print(temp.data, "->", end=" ")
            temp = temp.next
        print("None")


if __name__ == "__main__":
    L_list = Linked_List()
    L_list.Insert_At_End(8)
    L_list.Insert_At_End(5)
    L_list.Insert_At_End(10)
    L_list.Insert_At_End(7)
    L_list.Insert_At_End(6)
    L_list.Insert_At_End(11)
    L_list.Insert_At_End(9)
    print("Linked List: ")
    L_list.Display()
    print("Sorted Linked List: ")
    L_list.Sort()
    L_list.Display()
