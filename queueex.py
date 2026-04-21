class  Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
print("""Choose an option:
1. Enqueue an item into the queue   
2. Dequeue an item from the queue
3. Check if the queue is empty
4. Get the size of the queue
5. Exit""")
q = Queue()
while True:
    choice = input("Enter your choice: ")
    if choice == '1':
        item = input("Enter the item to enqueue: ")
        q.enqueue(item)
        print(item, "enqueued into the queue")
    elif choice == '2':
        if q.is_empty():
            print("Queue is empty")
        else:
            dequeued_item = q.dequeue()
            print(dequeued_item, "dequeued from the queue")
    elif choice == '3':
        if q.is_empty():
            print("Queue is empty")
        else:
            print("Queue is not empty")
    elif choice == '4':
        print("Size of the queue is:", q.size())
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
