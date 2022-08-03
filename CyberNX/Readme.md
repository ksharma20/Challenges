# Task Assigment

## Create an API with Login and Register functionality.
- You must ask additional personal information while registration.
Additional fields must contain at least following: First Name, Last Name,
Phone Number and profile photo.
- All fields must have back-end validation.
- Front-end is not a requirement for this app., you can use postman to test
your API.

# Solution
Created 2 APis
### Login 
![image](https://user-images.githubusercontent.com/72795959/182542055-19912527-96b2-42e4-a101-27e43fe26951.png)

Here you can login and logout
- to Login 
![image](https://user-images.githubusercontent.com/72795959/182542691-d00c1c21-0751-463e-b26c-93d9968c69a5.png)

Construct a json post with data as
```json
{
    "username":"keshav",
    "password":"Auth"
}
```
- Response
![image](https://user-images.githubusercontent.com/72795959/182542802-67998e19-8538-4c8a-a8c6-52c7ee1b3513.png)

- to Logout
Send an Empty Request
- Response
![image](https://user-images.githubusercontent.com/72795959/182542982-b1a390a2-f045-4b00-8643-72552dd10595.png)

