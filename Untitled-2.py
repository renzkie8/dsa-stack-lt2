class StackArray:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("\nCANNOT POP. STACK IS EMPTY.")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def height(self):
        return len(self.items)

def get_stack_input(prompt):
    return list(map(int, input(prompt).split()))

def main_menu():
    print("\nDSA - Learning Task 2 (DS List)")

   


    # Get input for three stacks
    stack1 = StackArray()
    stack2 = StackArray()
    stack3 = StackArray()

    stack1_items = get_stack_input("Enter elements for Stack 1 (separated by space): ")
    stack2_items = get_stack_input("Enter elements for Stack 2 (separated by space): ")
    stack3_items = get_stack_input("Enter elements for Stack 3 (separated by space): ")

    for item in stack1_items:
        stack1.push(item)
    for item in stack2_items:
        stack2.push(item)
    for item in stack3_items:
        stack3.push(item)

    # Determine the height of each stack
    height1 = stack1.height()
    height2 = stack2.height()
    height3 = stack3.height()

    # Check if the heights are equal
    if height1 == height2 == height3:
        print(f"All stacks are equal at height: {height1}")
    else:
        print("Stack heights will never be equal")

if __name__ == "__main__":
    
    main_menu()
