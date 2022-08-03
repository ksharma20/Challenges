# Task Assigment

## Create an API with Login and Register functionality.
- You must ask additional personal information while registration.
Additional fields must contain at least following: First Name, Last Name,
Phone Number and profile photo.
- All fields must have back-end validation.
- Front-end is not a requirement for this app., you can use postman to test
your API.

# Solution
## Created 2 APis
### 1. Login 
![image](https://user-images.githubusercontent.com/72795959/182542055-19912527-96b2-42e4-a101-27e43fe26951.png)

Here you can login and logout
- to Login 
![image](https://user-images.githubusercontent.com/72795959/182546255-79512b88-43a7-4a83-a996-f6c92f30ed40.png)


Construct a json post with data as
```json
{
    "username":"kabir",
    "password":"pass"
}
```
- Response
![image](https://user-images.githubusercontent.com/72795959/182546336-128f9331-1655-4036-9558-cf15c1d1b78f.png)

- to Logout
Send an Empty Request
- Response
![image](https://user-images.githubusercontent.com/72795959/182546024-f76a3c1f-ba05-4ffb-8159-8189de6db68c.png)

### 2. Register
- ON GET Request
![image](https://user-images.githubusercontent.com/72795959/182543751-96c17f11-74e3-42e6-97dd-0b86b89f7e4e.png)

Shows all the registered accounts so far !

- On POST Request
![image](https://user-images.githubusercontent.com/72795959/182545069-7ea45987-d45b-4829-9e65-7fd528fecfde.png)

Construct a json post with data as
```json
{
    "username":"kabir",
    "password":"pass",
    "first name":"kabir",
    "last name":"Sharma",
    "phone number":"8528425675",
    "profile pic": ""
}
```
- Response
![image](https://user-images.githubusercontent.com/72795959/182545158-fd9ae2e9-a484-4b9d-ba37-d60c35dc00ab.png)

A Default user with default profile pic is created (Bcoz No profile was mentioned)
![image](https://user-images.githubusercontent.com/72795959/182545476-f50be709-488c-4c35-a98f-ba01aaf7dfaf.png)

Here you need to upload profile pic using Pillow in Django so If you can send pic in request, It will put it as profile pic!
