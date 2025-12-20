class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Singly_Linked_list:
    def __init__(self):
        self.head = None

# INSERT AT THE END

    def insert(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return
        
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node

    def display(self):
        curr=self.head

        while curr:
            print(curr.data,end=" -> ")
            curr=curr.next
        print("None")

# INSERT AT THE BEGINNING

    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

# SEARCH IN A SINGLY LINKED LIST

    def search(self,val):
        curr=self.head

        while curr:
            if curr.data==val:
                return True
            curr=curr.next

        return False


# DELETE A NODE

    def delete(self,key):
        curr=self.head

# CASE 1: list is empty

        if curr is None:
            print("List is empty")
            return

# CASE 2: node to delete is head
         
        if curr.data==key:
            self.head=curr.next
            print(f"{key} deleted")
            return

# CASE 3: node is in the middle or at the end 
       
        prev=None

        while curr and curr.data != key:
            prev=curr
            curr=curr.next

# CASE 4: key not found

            if curr is None:
                print(f"{key} not found")
                return

# key found and deleted
            
            prev.next=curr.next
            print(f"{key} deleted")

ll=Singly_Linked_list()

ll.insert(3)
ll.insert(5)
ll.insert(7)

ll.insert_at_beginning(2)

ll.search(6)

ll.display()