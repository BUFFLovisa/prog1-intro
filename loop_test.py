while True:
    restart_loop = False
    user_input = input("vill du fortsätta? (ja/nej)")
    if user_input.lower() == 'nej':
        print("exit loop")
        break 
    elif user_input.lower() == 'ja':
        print("continue loop")
        restart_loop = True

    else:
        print("invalid input")
        restart_loop = True

        if restart_loop:
            continue