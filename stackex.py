class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)
        print(item,"pushed into stack")

    def pop(self, item):
        if self.stack.is_empty():
            raise IndexError("Stack is empty")
        elif len(self.stack) == 0:
            raise IndexError("Stack is empty")
        elif self.stack[-1] != item:
            raise ValueError("Top of stack does not match the item to pop")
        else:
            return self.stack.pop()
        
    def peek(self):
        if self.stack.is_empty():
            raise IndexError("Stack is empty")
        else:
            return self.stack[-1]       
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)

print("""Choose an option:
1. Push an item onto the stack
2. Pop an item from the stack   
3. Peek at the top item of the stack
4. Check if the stack is empty
5. Get the size of the stack
6. Exit""")
s = Stack()
while True:
    choice = input("Enter your choice: ")
    choice == 0
    if choice == '1':
        item = input("Enter the item to push: ")
        s.push(item)
    elif choice == '2':
        item = input("Enter the item to pop: ")
        try:
            popped_item = s.pop(item)
            print(popped_item, "popped from stack")
        except (IndexError, ValueError) as e:
            print(e)
    elif choice == '3':
        try:
            top_item = s.peek()
            print("Top item of the stack is:", top_item)
        except IndexError as e:
            print(e)
    elif choice == '4':
        if s.is_empty():
            print("Stack is empty")
        else:
            print("Stack is not empty")
    elif choice == '5':
        print("Size of the stack is:", s.size())
        
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")


