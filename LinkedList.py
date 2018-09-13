class LinkedList:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


class SingleLinkedList:
    def __init__(self,data=None,next=None):
        self.head = data;
        print "Linked List Created"



    def __str__(self):
        return   "SINGLE LINKED LIST"



    def append(self,data):
        if(self.head==None):
            self.head=data;
        else:
            current = self.head;
            while(True):
                if(current.next==None):
                    current.next=data;
                    break;
                current = current.next;


    def delete(self,data):
         if(self.head==None):
             print "Linked List is Empty"
         else:
             current = self.head
             while(True):
                 if(self.head.data==data):
                     self.head=self.head.next;
                     break;
                 else:
                     if(current.next.data==data):
                         current.next=current.next.next;
                         break;
                     else:
                         current = current.next;
                         if(current.next==None):
                             break;

    def insert(self,pos,data):
        count = 0
        current = self.head
        while(True):
            if(count==pos-1):
                print count
                temp = current.next
                current.next = data;
                current = current.next
                current.next = temp
                break;
            else:
                current = current.next;
                print count
                count = count +1;


    def traverse(self):
        if(self.head==None):
            print self.head.data
        else:
            current = self.head;
            while(True):
                if(current.next==None):
                    print current.data
                    break;
                else:
                    print current.data;
                    current = current.next;





if __name__ == '__main__':
    l1 = LinkedList("Apple");
    l2 = LinkedList("Google");
    l3 = LinkedList("Microsoft");
    l4 = LinkedList("Intel");
    l5 = LinkedList("Amazon");
    l6 = LinkedList("Adobe");

    s = SingleLinkedList();
    s.append(l1);
    s.append(l2);
    s.append(l3);
    s.append(l4);
    s.append(l5);
    s.append(l6);


    print("\n\nTraverse---")
    s.traverse();
