# Function for inserting values into stack
def push(stack, item):
    stack.append(item)  # PUSH by appending

# Function for removing values from stack
def pop(stack):
    if len(stack) == 0:  # if stack is empty, no pop
        return None 
    return stack.pop()  # POP by popping (list method)

# Function for all stack operations
def StackProg():
    stack_no = 3  # sets number of stacks to 3
    stacks = [] 
    heights = [] 
    for i in range(stack_no):  # 3 loops for 3 stacks
        while True:  # error handling for input
            try:
                item = input(f'Enter elements of Stack {i+1} (separate using space): ').split() 
                item = [int(x) for x in item] 
                break
            except ValueError: 
                print("Invalid input! Enter INTEGERS ONLY.")
        stack = [] 
        height = 0 
        for val in item: 
            push(stack, val) 
            height += val 
        stacks.append(stack) 
        heights.append(height) 
    print("-" * 35) 
    for h in range(len(heights)):
        print(f'Stack {h+1} total height: {heights[h]}')  # prints height of each stack
    print("-" * 35) 

    # Blocks for equalizing height of each stack
    while len(set(heights)) != 1:  # len(set(heights)) check no of unique elements in 'heights' list, if not equal to 1 meaning all height in 'heights' are not same values
        if any(h == 0 for h in heights):
            print("Stack heights will never be equal.")  # automatically, stack will never be equal
            print("-" * 35)  # lines---
            return

        # When all stacks contain NEGATIVE values,
        if all(h < 0 for h in heights):
            for i in range(stack_no):  # 3 loops for 3 stacks
                if heights[i] == min(heights): 
                    popit = pop(stacks[i]) 
                    if popit is not None: 
                        break

        for i in range(stack_no):  # 3 loops for 3 stacks
            if heights[i] == max(heights):  # find stack with HIGHEST height (highest height would contain highest absolute value)
                popit = pop(stacks[i])  # pops a value from it
                if popit is not None:  # if stack is not/still not empty,
                    heights[i] -= popit  # decrement height with popped value
                break

        else:
            for i in range(stack_no):  # 3 loops for 3 stacks
                if heights[i] == max(heights): 
                    popit = pop(stacks[i]) 
                    if popit is not None:  # if stack is not/still not empty,
                        heights[i] -= popit  # decrement height with popped value
                    break

    if len(set(heights)) == 1:  # identifies if values of each stack height in 'heights' list after popping are equal
        print(f'All stacks are equal at Height: {heights[0]}')  # so, equal height success, prints success message
        for s in range(len(stacks)):  # for no of stack in stacks; " ".join(map(str, stacks[s]))}') removes [] and "" from individual values in list
            print(f'Stack {s+1}: {" ".join(map(str, stacks[s][::-1]))}')  # print resulting values for each stack, IN REVERSE, after equalizing
        print("-" * 35) 
    else: 
        print("Stack heights will never be equal.")  # fail message
        print("-" * 35)  # lines---

# Function if want to continue or exit
def main():
    while True:
        StackProg()
        while True:
            confirm = input("Continue? Y or N?: ").upper()  # ask user yes or no, if want to confirm; input capitalize to be uniform
            if confirm == 'N':  # if not continue
                print("\nOK. Thanks.")  # prints farewell message
                return  # terminates program
            elif confirm == 'Y':  # if continue
                print("-" * 35)  # lines---
                break  # break loop StackProg() restart
            else:
                print("INVALID INPUT!!! Please enter Y or N ONLY!")

# Starts program
if __name__ == "__main__":
    main()
