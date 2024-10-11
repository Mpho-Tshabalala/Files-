
#=====importing libraries===========
'''This is the section where you will import libraries''' 
path_tasks ='tasks.txt'
path_user ='user.txt'

#raw data sets
data_password = []
data_set = []
data_set_1 = []
data_set_2 = []


# Organized data sets
name_of_tasks = []
description_of_tasks = []
assigned_dates = []
due_dates = []
state_of_completion = []
new_users = []
total_users = 0

#User infomation
user_names = [] 
passwords = []

# Empty sentences that will be used to populate the various lists 
sentence_1 = ""
sentence_2 = ""

# Take each line in the tasks folder, split it and add each element of the sentence to the required list
with open(path_tasks, 'r+') as file_tasks:
    for lines in file_tasks:
        data = lines.strip()
        data = lines.split("\n")
        data_set.append(data)
        

with open(path_user, 'r') as file_password:
    for lines in file_password:
       pword = lines.strip()
       passwords = pword.split()
       
        
#Seperate each line into seperate sentences    
sentence_1 = data_set[0]     
sentence_2 = data_set[1]
sentence_1 = str(sentence_1).strip("[]'")
sentence_2 = str(sentence_2).strip("[]'")
sentence_1 = sentence_1.lower()
sentence_2 = sentence_2.lower()

#Seperate the sentences into lists 
data_set_1 = sentence_1.split(", ")
data_set_2 = sentence_2.split(", ")
    
# Now take each variable in the the data sets and add them to thier own lists for each variable
user_names.append(data_set_1[0])
user_names.append(data_set_2[0])
name_of_tasks.append(data_set_1[1])
name_of_tasks.append(data_set_2[1])
description_of_tasks.append(data_set_1[2])
description_of_tasks.append(data_set_2[2])
assigned_dates.append(data_set_1[3])
assigned_dates.append(data_set_2[3])
due_dates.append(data_set_1[4])
due_dates.append(data_set_2[4])
state_of_completion.append(data_set_1[5])
state_of_completion.append(data_set_2[5])

    
  
#====Login Section====
'''Here you will write code that will allow a user to login.
   - We ask the user to enter the username and the password
   - We take the username and password from our lists to check so see if the username entered is valid
'''
with open(path_user, 'r+') as file_user:
    username_input = input("Enter username: ").lower()
    password_input = input("Enter your password: ").lower()


while username_input in user_names and password_input in passwords:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
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
        pass
        if username_input == "admin":
            new_username = input("Enter new username: ").lower()
            new_password = input("Enter a new password: ").lower()
            confirm_new_password = input("Confirm the new password: ").lower()
            
            if confirm_new_password == new_password:
            
                with open(path_user, 'a+') as file_user:
                    file_user.write(new_username+", "+new_password)
                    new_users.append(new_username)
                    passwords.append(new_password)
                
            else:
                print("Passwords do not match, please try again")
        else:
            print("Sorry only the admin is allowed to edit the usernames")
        
        
        
        
        

    elif menu == 'a':
        
        '''This code block will allow a user to add a new task to task.txt file
        So here we take each new detail that is added and add it to our list libry'''
            
        pass
        username = input("Enter the username of the person the task is assigned to: ").lower()
        task_title = input("Enter the title of the task: ").lower()
        task_description = input("Enter the description of the task: ").lower()
        due_date = input("Enter the due date of the task: ").lower()
        current_date = input("Enter current date: ").lower()
        
        
        with open(path_tasks, 'a+') as file_user:
                file_user.write(username+ ", " +task_title+ ", " +task_description+ ", " +due_date + ", "+ current_date)
                user_names.append(username)
                name_of_tasks.append(task_title)
                description_of_tasks.append(task_description)
                assigned_dates.append(current_date)
                due_dates.append(due_date)
                state_of_completion.append("no")
        
            
            
        
    elif menu == 'va':
        pass
        '''This code block will strategically print the elements of our list libry thus far'''
        i = 0
        for i in range(0,len(name_of_tasks)):
            print("Task:                            "+name_of_tasks[i]+"\n"
              "Assigned to:                     "+ user_names[i]+"\n"
              "Date assigned:                   "+assigned_dates[i]+"\n"
              "Due date:                        "+due_dates[i]+"\n"
              "Task complete?                   "+state_of_completion[i]+"\n"
              "Task description:                "+description_of_tasks[i]+"\n")
            i +=1 
            
            
    elif menu == 'vm':
        pass
        '''This code block will print the part of the task pertaining to the current user'''
        username = input("Enter your username: ").lower()
        i = 0 
        endpoint = len(user_names) + 2
        for i in range(0,len(user_names)):
            if username == user_names[i]:
                
                print("Task:                            "+name_of_tasks[i]+"\n"
                    "Date assigned:                   "+assigned_dates[i]+"\n"
                      "Due date:                        "+due_dates[i]+"\n"
                      "Task complete?                   "+state_of_completion[i]+"\n"
                      "Task description:                "+description_of_tasks[i]+"\n")
              
       
               
            
                          
    elif menu == 's':
        total_users = len(user_names) + len(new_users)
        print("The total number of users is: "+"               "+str(total_users))
        print("The total number of tasks is: "+"               "+str(len(name_of_tasks)))
                
    
       

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

else:
    print("You have entered an invalid input. Please try again")
        
