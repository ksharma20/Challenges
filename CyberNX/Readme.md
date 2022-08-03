# Task Assigment

## Create an API with Login and Register functionality.
- You must ask additional personal information while registration.
Additional fields must contain at least following: First Name, Last Name,
Phone Number and profile photo.
- All fields must have back-end validation.
- Front-end is not a requirement for this app., you can use postman to test
your API.

# Solution

##### Download the Assignment Folder 
- First of all you need to download the folder using 
[Download link](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/ksharma20/Challenges/tree/main/CyberNX) <== CyberNX Assignment Folder

- This will take you to a Web page where Your download will Get started Automatically
![image](https://user-images.githubusercontent.com/72795959/147810693-64825f36-c9f6-4330-93d0-04f6ddd230b4.png)

- Save Zip file to your Required folder and Then Extract it as Well.

- After Extracting you will see A Readme.md File and a Sub directory with project Name


- Open this project folder (Dj_Auth).


##### Setting Up the server
- Open it in a Terminal or vs code and open terminal there
![image](https://user-images.githubusercontent.com/72795959/147811935-b0ba6950-acc6-40d6-abfd-4d9f04802abf.png)


- Run the following command 
` python manage.py runserver `

![image](https://user-images.githubusercontent.com/72795959/147812044-c4e36612-9486-47e1-9c66-c6d3e42e2584.png)

- And open the following link in your browser
` http://127.0.0.1:8000/ `


## Task Completed - Created 2 APis
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
