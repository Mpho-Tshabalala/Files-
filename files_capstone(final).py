path_tasks = 'tasks.txt'
path_user = 'user.txt'

user_names = []
passwords = []
with open(path_user, 'r') as file_password:
    for line in file_password:
        user_list = line.split(', ')
        user_names.append(user_list[0])
        passwords.append(user_list[1].strip('\n'))

#====Login Section====
'''Here you will write code that will allow a user to login.
   - We ask the user to enter the username and the password
   - We take the username and password from our lists to check so see if the username entered is valid
'''
username_input = input("Enter username: ").lower()
password_input = input("Enter your password: ").lower()

while username_input in user_names and password_input in passwords:
    # Present the menu to the user and
    # make sure that the user input is converted to lower case.
    if username_input == "admin":
        menu = input('''Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    s - statistics
    e - exit
    : ''').lower()
        '''This code block will add a new user to the user.txt file
            This block will check if the admin is the one loging in and if it it then they can add register names '''

        if menu == 'r':
            while True:
                new_username = input("Enter new username: ").lower()
                new_password = input("Enter a new password: ").lower()
                confirm_new_password = input("Confirm the new password: ").lower()

                if confirm_new_password == new_password:
                    with open(path_user, 'a') as file_user:
                        file_user.write(f"\n{new_username}, {new_password}" )
                        user_names.append(new_username)
                        passwords.append(new_password)
                        break

                else:
                    print("Passwords do not match, please try again")

        elif menu == 'a':
            '''This code block will allow a user to add a new task to task.txt file
            So here we take each new detail that is added and add it to our list libry'''

            username = input("Enter the username of the person the task is assigned to: ").lower().strip()
            task_title = input("Enter the title of the task: ").lower().strip()
            task_description = input("Enter the description of the task: ").lower().strip()
            due_date = input("Enter the due date of the task: ").lower().strip()
            current_date = input("Enter current date: ").lower().strip()


            with open(path_tasks, 'a') as file_user:
                    file_user.write(f"\n{username}, {task_title}, {task_description}, {due_date}, {current_date}, No")

        elif menu == 'va':
            '''This code block will strategically print the elements of our list libry thus far'''
            with open(path_tasks, 'r') as file_password:
                for line in file_password:
                    task_list = line.split(', ')
                    print("Task:                            "+task_list[1]+"\n"
                          "Assigned to:                     "+ task_list[0]+"\n"
                          "Date assigned:                   "+ task_list[4]+"\n"
                          "Due date:                        "+ task_list[3]+"\n"
                          "Task complete?                   "+ task_list[5].strip('\n')+"\n"
                          "Task description:                "+ task_list[2]+"\n")

        elif menu == 'vm':
            '''This code block will print the part of the task pertaining to the current user'''
            username = input("Enter your username: ").lower().strip()
            tasks = []
            count = []
            with open(path_tasks, 'r') as file_password:
                for line in file_password:
                    line.strip('\n')
                    task_list = line.split(', ')
                    count.append(task_list[0])
                    tasks.append(task_list)

                for i in range(len(count)):
                    if username == tasks[i][0]:
                        print("Task:                            "+tasks[i][1]+"\n"
                              "Date assigned:                   "+tasks[i][4]+"\n"
                              "Due date:                        "+tasks[i][3]+"\n"
                              "Task complete?                   "+tasks[i][5].strip('\n')+"\n"
                              "Task description:                "+tasks[i][2]+"\n")

        elif menu == 's':
            count = []
            with open(path_tasks, 'r') as file_password:
                for line in file_password:
                    task_list = line.split(', ')
                    count.append(task_list[0])

            print("The total number of users is: "+"               "+str(len(user_names)))
            print("The total number of tasks is: "+"               "+str(len(count)))

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

    else:
        menu = input('''Select one of the following options:
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    : ''').lower()
        if menu == 'a':
            '''This code block will allow a user to add a new task to task.txt file
            So here we take each new detail that is added and add it to our list libry'''

            username = input("Enter the username of the person the task is assigned to: ").lower().strip()
            task_title = input("Enter the title of the task: ").lower().strip()
            task_description = input("Enter the description of the task: ").lower().strip()
            due_date = input("Enter the due date of the task: ").lower().strip()
            current_date = input("Enter current date: ").lower().strip()


            with open(path_tasks, 'a') as file_user:
                    file_user.write(f"\n{username}, {task_title}, {task_description}, {due_date}, {current_date}, No")

        elif menu == 'va':
            '''This code block will strategically print the elements of our list libry thus far'''
            with open(path_tasks, 'r') as file_password:
                for line in file_password:
                    task_list = line.split(', ')
                    print("Task:                            "+task_list[1]+"\n"
                          "Assigned to:                     "+ task_list[0]+"\n"
                          "Date assigned:                   "+ task_list[4]+"\n"
                          "Due date:                        "+ task_list[3]+"\n"
                          "Task complete?                   "+ task_list[5].strip('\n')+"\n"
                          "Task description:                "+ task_list[2]+"\n")

        elif menu == 'vm':
            '''This code block will print the part of the task pertaining to the current user'''
            username = input("Enter your username: ").lower().strip()
            tasks = []
            count = []
            with open(path_tasks, 'r') as file_password:
                for line in file_password:
                    line.strip('\n')
                    task_list = line.split(', ')
                    count.append(task_list[0])
                    tasks.append(task_list)

                for i in range(len(count)):
                    if username == tasks[i][0]:
                        print("Task:                            "+tasks[i][1]+"\n"
                              "Date assigned:                   "+tasks[i][4]+"\n"
                              "Due date:                        "+tasks[i][3]+"\n"
                              "Task complete?                   "+tasks[i][5].strip('\n')+"\n"
                              "Task description:                "+tasks[i][2]+"\n")


        elif menu == 'e':
            print('Goodbye!!!')
            exit()


