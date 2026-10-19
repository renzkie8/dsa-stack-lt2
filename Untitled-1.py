print("\nDSA - Learning Task 2 (DS List)")

 # we first set a class stack array 

def __init__(stackarr): # initializator that our stack array is empty
        stackarr.items = []

def push(stackarr, item):  # a push is define to let us input item in ou stackarr
        stackarr.append(item)
        
def pop(stackarr): # here same with delete method this parameter only has what we define the stack arr as what this just do is delete the item in our stack_arr
        stack = stackarr.head
        #CASE: Empty array
        if len(stackarr) is None:
            print("\nCANNOT POP. ARRAY IS EMPTY.")# if stack is empty cannot delete
            return None
        return stackarr.pop()

def is_empty(stack_arr):
        return len(stack_arr.items) == 0 # if stack is empty,there will nothing to be pop

    #def height(self):
       # return len(self.items)

def StackArray(position= None):
        empty_stacks = []
        empty_heights = []
        stack_count = 3 # the number of the stack status is set to three
        
        for data in range(stack_count): # the parameter to argument our 3 stacks and has a array of items:
            while True: #CASE 1 : Array has  a items of elements
                try: #exception handling
                    integer = input(f'\n Enter elements of Stack {data+ 1} : ').split() 
                    integer = [int(num) for num in integer] 
                    break
                except ValueError:
                    print("PLEASE ENTER A VALID INTEGER. \n\n***\n")
            stacks = []   # initialize a stack that is not empty
            heights = 0   # initialize a height that is not empty

            for values in integer:
                push(stacks,values)   
                heights += values
            
            empty_stacks.append(stacks)
            empty_heights.append (heights)

        print("\n------------------------------ ")

        for heights in range(len(empty_heights)): # CASE 2 : HEIGHT IS NOT EMPTY AND HAS A VALUE.
            print(f'\n Stack {heights+ 1} total height:  {empty_heights[heights]}.')
        print("\n------------------------------ ")

        # CASE 4: ELEMENTS OF EACH STACKS HEIGHT WILL BE NON-EQUAL.
        while len(set(empty_heights)) != 1:  # setting a while loop to check the data elements of heights in our stacks
            if any(heights == 0 for heights in empty_heights):  # when node is empty before or on specified position
                    print("\nStack heights will never be equal.")
                    print("\n------------------------------ ")
                    return
        else: # CASE 5: USER INPUT A NEGATIVE ELEMENTS/INTEGERS. 
        
         if all(heights < None for heights in empty_heights):
                  for data in range(stack_count): 
                        if empty_heights [data] == min(empty_heights): # for elements in stackarray check and find the minimum height
                         poppin = pop(empty_stacks[data])
                        if poppin is not None:            #exception: check if the array is empty to none/ not empty.
                            empty_heights[data] -= poppin # let us to decrement its value and reassigning it with pop valued.
                        break   
          # CASE 6: This time for height that count the height in our created data or stacks
         for data in range(stack_count):
                if empty_heights[heights] == max(empty_heights): #check the highest(maximum) heights in the three stack array
                    poppin = pop(empty_stacks[data])
                    if poppin is not None: #exception: check if the array is empty to none/ not empty.
                        break
        #CASE 7 : THIS TIME the else method is for the initialization of maximum heights in our data array stack
         else: 
           for data in range(stack_count):
                if empty_heights[data] == max(empty_heights):#for elements in stackarray check and find the maximum height
                    poppin = pop(empty_stacks[data])
                    if poppin is not None: #exception: check if the array is empty to none/ not empty.
                        empty_heights[data] -= poppin
                        break

         if len(set(empty_heights)) == 1:  
            print(f'All stacks are equal at Height: {empty_heights[0]}')  # so, equal height success, prints success message

            for stackarr in range(len(empty_stacks)):  
             print(f'Stack {stackarr+1}: {" ".join(map(str, empty_stacks[stackarr][::-1]))}')  

        print("\n------------------------------ ")
        print(f'\nStack {data+1} total height: {empty_heights[data]}.')  # fail message
        print("\n------------------------------ ")
       # print(f'\n"{heights+ 1}" total height:  {empty_heights[heights]}.') # fail message
       # print("\n------------------------------ ")

                     


# E X I T  O P T I O N
# main_menu to exit or continue the program
def main_menu():
    stack = StackArray()
    while True:
        choice = input("\n""Continue? Y or N?: ")
        if choice == 'Y':
             print("\n------------------------------ ")
             return
        elif choice == 'N':
            print("\n------------------------------ \n\nT H A N K  Y O U !\n")
            break
        else:
            print("PLEASE ENTER [0] FOR YES OR [1] FOR NO.\n\n------------------------------\n")


if __name__ == "__main__":
    main_menu()
