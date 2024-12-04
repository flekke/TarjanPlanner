def get_user_input():
    answer = []
    
    while True:
        try:
            service = int(input("what do you want? 1. shortest path 2. travel plan with transportation "))
            if service in [1, 2]:
                answer.append(service)
                if service == 1:
                    return answer
                break
            else: 
                print("Please enter either 1 or 2")
        except ValueError:
            print("Please enter either 1 or 2")

    while True:
        try:
            priority = int(input("what is your priority? 1. minimal time 2. minimal cost 3. least amount of transfers "))
            if priority in [1, 2,3]:
                answer.append(priority)
                break
            else:
                print("Please enter either 1 or 2.")
        except ValueError:
            print("Please enter either 1 or 2.")

    return answer

