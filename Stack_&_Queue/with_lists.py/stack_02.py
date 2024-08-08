
stack = []

def push():
    if len(stack)==limit:
        print("StackOverflow")
    else:
        element = input("Enter the element to push: ")
        stack.append(element)
        print("updated stack:",stack)
    print("-------------------------")

def pop():
    if len(stack)==0:
        print("StackUnderFlow")
    else:
        popped_elem = stack.pop()
        print("poppped element:",popped_elem," updated stack:",stack)
    print("-------------------------")


def quit():
    print('Exiting the program')
    global running
    running = False

#---------------------------------------------------
limit = int(input("enter stack limit: "))
options = {
    1:push,
    2:pop,
    3:quit
}
running = True
while running:
    print("select the options: \n1.push \n2.pop \n3.quit")
    choice = int(input('enter the option: '))

    try:
        if choice in options:
            options[choice]()
        else:
            print("enter the correct option")
    except ValueError:
        print("invalid input")