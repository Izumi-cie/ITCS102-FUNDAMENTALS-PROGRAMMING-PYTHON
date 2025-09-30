isDrawing = True

while isDrawing == True:
    ask = input("Do you want to draw the Christmas tree? (y/n) --> ")

    if ask.lower() == 'y':
        # sizes
        top = 5
        middle = 6
        lower = 7
        body_height = 4
        body_width = 5

        #star
        i = 1
        while i <= 2:  
            print(" " * (lower - i) + "*" * (2 * i - 1))
            i += 1
        i = 1
        while i > 0:  
            print(" " * (lower - i) + "*" * (2 * i - 1))
            i -= 1

        #pyramid
        i = 1
        while i <= top:
            print(" " * (lower - i) + "*" * (2 * i - 1))
            i += 1 
            
        i = 1
        while i <= middle:
            print(" " * (lower - i) + "*" * (2 * i - 1))
            i += 1
            
        i = 1
        while i <= lower:
            print(" " * (lower - i) + "*" * (2 * i - 1))
            i += 1

        # body
        trunk = 1
        while trunk <= body_height:
            print(" " * (lower - 3) + "*" * body_width)
            trunk += 1

        continue
    else:
        print("Okay, I won't make you one.")
        break
