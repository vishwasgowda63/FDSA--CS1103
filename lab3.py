class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None 

class SinglyLinkedList:
    def __init__(self):
        self.head = None  

    
    def append_node(self, data):
        new_node = Node(data)  
        if self.head is None:
          
            self.head = new_node
            return
      
        last = self.head
        while last.next:
            last = last.next
       
        last.next = new_node

   
    def search_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True  
            current = current.next
        return False  

    
    def display_list(self):
        current = self.head
        if not current:
            print("List is empty")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None") 


if __name__ == "__main__":
    
    sll = SinglyLinkedList()

    
    sll.append_node(10)
    sll.append_node(20)
    sll.append_node(30)

   
    print("List after appending nodes:")
    sll.display_list() 

    print("Is 20 in the list?", sll.search_node(20))  

 
    print("Is 100 in the list?", sll.search_node(100))  
    
    
