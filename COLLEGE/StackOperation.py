n = int(input("Enter the size of the stack: "))
a = []

def display(stack):
    if len(stack) == 0:
        print("The stack is empty")
    else:
        print("The stack is:")
        for i in reversed(stack):
            print(i)

while True:
    print("\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        if len(a) == n:
            print("Stack Overflow! Cannot push more elements.")
        else:
            element = int(input("Enter the element to be pushed: "))
            a.append(element)
            print(f"Element {element} pushed successfully.")
    
    elif choice == 2:
        if len(a) == 0:
            print("Stack Underflow! The stack is empty.")
        else:
            print("The element popped is:", a.pop())
    
    elif choice == 3:
        display(a)
    
    elif choice == 4:
        print("Exiting program. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please try again.")
