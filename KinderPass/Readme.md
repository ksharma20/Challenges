# Problem statement:

Create an application where users can create tasks, view them, mark them as completed and delete them. Create REST APIs alone. No need to develop the front-end.

## Users should be able to do the following.

- Signup using email and password
- Create tasks
- View all tasks
- Mark a task as completed
- Delete tasks
- Login & logout

## Use the following tools/frameworks:

- Django (DRF is optional)
- Django ORM
- Sqlite
- Git

# Solution:
### Home page

![image](https://user-images.githubusercontent.com/72795959/189635157-3ba51586-3b00-4a84-adf0-d2c38e68546b.png)
Go to Any of the Api

### Sign up using Api

Enter an Email & Password (as payload) to create a user
```json
{
    "email": "kbr@csegeeks.com",
    "password": "kabir12345"
}
```
![image](https://user-images.githubusercontent.com/72795959/189635535-5d4ec79a-5ba0-413f-b27d-bb07e46eea31.png)

After Sending post request, It tells User created
![image](https://user-images.githubusercontent.com/72795959/189635718-4e2d4100-da04-4d33-a293-3ac6f861efa8.png)


### Login

Enter Email & Password to Login
```json
{
    "email": "kbr@csegeeks.com",
    "password": "kabir12345"
}
```
![image](https://user-images.githubusercontent.com/72795959/189635952-5ac266e4-4655-449c-aef0-adc2a94de593.png)

it than Tells that User is logged-In
![image](https://user-images.githubusercontent.com/72795959/189636030-89e9e023-ed8d-4c7b-afd0-916b355b0d2b.png)


### Create Task

Create a Task by providing
```json
{
    "task": "Complete a Django book",
    "description": "Complete Back and Return back"
}
```
![image](https://user-images.githubusercontent.com/72795959/189636514-e8ae8ca7-f0ad-499c-b1c0-300eba35708a.png)

Created Task is then Displayed
![image](https://user-images.githubusercontent.com/72795959/189636717-fa69502d-1919-4e28-886c-3710bb660fdd.png)


### View All Tasks

Here You can view all the tasks of that Particular user (logged-in User)
![image](https://user-images.githubusercontent.com/72795959/189636875-2e3a06aa-e792-4293-8598-8d99e5d492e9.png)


### View a Particular Task:
To make less apis & get things done efficiently, I used payload for partular task to delete or mark a task as complete.
![image](https://user-images.githubusercontent.com/72795959/189637280-113e4391-b907-41c1-87e9-b519bf945ade.png)


#### Mark task Complete
```json
{
    "option": "mark"
}
``` 
OR 
```json
{
    "option": "complete"
}
```
Use Above json as payload

![image](https://user-images.githubusercontent.com/72795959/189637490-d7b25c28-e096-4fa2-8617-abcd63bef73a.png)

It will Mark the Task Complete
![image](https://user-images.githubusercontent.com/72795959/189637660-2883596c-5b58-4a71-b804-7ba638958a6c.png)

Can Be seen at All Tasks as well
![image](https://user-images.githubusercontent.com/72795959/189637754-3e665116-6d09-4754-ab5a-df0b906e5030.png)


#### Delete Task
```json
{
    "option": "del"
}
``` 
OR 
```json
{
    "option": "delete"
}
```
Use above json as Payload

![image](https://user-images.githubusercontent.com/72795959/189638094-898ca161-cfd5-475e-8ade-002b83cb40ac.png)

It will Delete the Particular Task
![image](https://user-images.githubusercontent.com/72795959/189638160-eec94a4d-8641-4263-8eb3-1628770e8427.png)

All Tasks list for logged-in User
![image](https://user-images.githubusercontent.com/72795959/189638283-dcafe2b6-bf17-4f5b-929e-769abfc2a7dd.png)


### Logout

Got to login api & send a Empty Post payload or write logout
![image](https://user-images.githubusercontent.com/72795959/189638480-fc694bca-a890-4c8a-91bd-667eac832b52.png)

This will Log you out 


### Note
Onces you have logged out, You can not access API's to create or view tasks
![image](https://user-images.githubusercontent.com/72795959/189639183-ed87929d-248e-407f-913d-7172cf15f490.png)

