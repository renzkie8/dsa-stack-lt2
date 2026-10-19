print("\nDSA - Learning Task 2 (DS Stack)")

def push(stack, item): #defining the pushing method with it parameter of stack and a item/value in our stack, to let us input item in ou stackarr
    stack.append(item) # then this will append or just insert that item in a first in last out method
    

def pop(stack): #defining the popping method or the deletion with its parameter of a stack as what this just do is delete the item in our stack_arr
    if len(stack) == 0: 
        #CASE 0 : Empty array
        return None 
    return stack.pop() 


def StackArray(position=None): 
    empty_stacks = []
    empty_heights = []
    stack_count = 3  # the number of the stack status is set to three

    for data in range(stack_count):  # the parameter to argument our 3 stacks and has an array of items:
        while True:  # CASE 1 : Array has items of elements
            try:  # exception handling
                integer = input(f'\nEnter elements of Stack {data + 1}: ').split()
                integer = [int(num) for num in integer]
                break
            except ValueError:
                print("PLEASE ENTER A VALID INTEGER. \n\n***\n")

        stacks = []  # initialize a set of stack that is not empty 
        heights = 0  # initialize a set of height that is not empty

        for values in integer:
            push(stacks, values)
            heights += values

        empty_stacks.append(stacks)
        empty_heights.append(heights)
 
    print("\n---------------------------------------------- ")

    for i in range(len(empty_heights)):  #  HEIGHT IS NOT EMPTY AND HAS A VALUE.
        print(f'\nStack {i + 1} total height: {empty_heights[i]}.')

    print("\n---------------------------------------------- ")

    # CASE 2: ELEMENTS OF EACH STACKS HEIGHT WILL BE NON-EQUAL.
    while len(set(empty_heights)) != 1:  # setting a while loop to check the data elements of heights in our stacks
        if any(h == 0 for h in empty_heights):  # when node is empty before or on specified position
            print("\nStack heights will never be equal.")
            print("\n---------------------------------------------- ")
            return

        # CASE 3: USER INPUT A NEGATIVE ELEMENTS/INTEGERS.
        if all(h < 0 for h in empty_heights):
            for data in range(stack_count):
                if empty_heights[data] == min(empty_heights):  # for elements in stackarray check and find the minimum height
                    poppin = pop(empty_stacks[data]) # typically removes and returns the top element of stack and stored it to poppin .
                    if poppin is not None:  # exception: check if the array is empty to none/ not empty.
                        empty_heights[data] -= poppin  # let us decrement its value and reassign it with pop value.
                    break

        # CASE 4: This time for height that count the maximum height in our created data or stacks
        for data in range(stack_count):
            if empty_heights[data] == max(empty_heights):  # check the highest(maximum) heights in the three stack array
                poppin = pop(empty_stacks[data])# The pop function removes and returns the top element of the stack.
                if poppin is not None: #If poppin is not None, it subtracts the popped value
                     # exception: check if the array is empty to none/ not empty.
                    empty_heights[data] -= poppin
                    break

        # CASE 5&6: THIS TIME the else method is for the initialization of maximum heights in our data array stack
        else:
            for data in range(stack_count):
                if empty_heights[data] == max(empty_heights):  # for elements in stackarray check and find the maximum height
                    poppin = pop(empty_stacks[data])
                    if poppin is not None:  # exception: check if the array is empty to none/ not empty.
                        empty_heights[data] -= poppin
                        break

    # CASE 7: Checkts all the elements in empty_heights if or are the same heights or elements thus if is ==1
    # remember that the elements in our stack is in a set of datas, which will haveonly 1 elem. making its length combined to 1
    if len(set(empty_heights)) == 1: 
        print(f'All stacks are equal at Height: {empty_heights[0]}')  #  equal height success, prints success message
    #for loop implement iterates over each stack in the empty_stacks list.
        for stackarr in range(len(empty_stacks)):  #It let the elements in our stack array print
            print(f'Stack {stackarr + 1}: {" ".join(map(str, empty_stacks[stackarr][::-1]))}')
            # so in its printing state it we used a .join method to join the string main output and a map class is use to converts each element in the stack to a string.
        
        print("\n---------------------------------------------- ")

def main_menu():
    while True:
        StackArray()
        while True:
            confirm = input("Continue? Y or N?: ")  # ask user yes or no, if want to confirm; input capitalize to be uniform
            if confirm == 'N':  # if not continue
                print("\n----------------------------------------------\n\nT H A N K  Y O U !\n")  # prints farewell message
                return  # terminates program
            elif confirm == 'Y':  # if continue
                print("\n----------------------------------------------")  # lines---
                break  # break loop StackProg() restart
            else:
                print("INVALID INPUT!!! Please enter Y or N ONLY!")

if __name__ == "__main__":
    main_menu()
