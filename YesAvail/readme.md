# Minimal E-Commerce Solution APIs Assignment

### Assignment statement - You need to build a very minimal eCommerce solution APIs, where a user can do the following things:

- Signup
- Login
- See the product list
- See the product in detail and can add it to the cart
- User can checkout cart by selecting one address and order will get placed (No payment system required, it will be cash on delivery only)
- Users can see their order list.

##### You need to build this using the below steps.
1. Build Backend APIs first for above all points. (10 points)
2. Push everything in a single git repository, you should keep pushing as you progress rather than pushing all at once. Commits should be with some meaningful commit message, we'll check your GitHub commits. (5 points)
3. Write proper documentation for setting up the project, so that one can easily set up the project by following the steps there. (5 points)
4. Include a demo video of your assignment, you can share youtube/Vimeo/google drive link (5 points)


##### Technologies to use:
1. For Building Backend APIs, you can use any technologies you want. However, Django REST Framework is preferred.
2. Database you can use any SQL, default SQLite will also work.
3. For writing documentation i.e. README file, you can use markdown i.e. MD or Restructured Text i.e. RST
4. You can use a screen recorder for the demo video


_Note - The assignment is distributed above in multiple points, even if you'll complete anyone
points out of the first two, You are welcome to submit your assignment, we don't want to waste your effort without reviewing the code_


### Explanation / solution :

##### Download the Assignment Folder 
- First of all you need to download the folder using below Download link 
[Download](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/ksharma20/Challenges/tree/main/YesAvail) <== YesAvail Assignment Folder

- This will take you to a Web page where Your download will Get started Automatically
![image](https://user-images.githubusercontent.com/72795959/147810693-64825f36-c9f6-4330-93d0-04f6ddd230b4.png)

- Save Zip file to your Required folder and Then Extract it as Well.

- After Extracting you will see A Readme.md File and a Sub directory with project Name
![image](https://user-images.githubusercontent.com/72795959/147811221-1d7a8201-b66c-45d8-b77e-f4b83e61aed9.png)


- Open this project folder (Dj_eComm).


##### Setting Up the server
- Open it in a Terminal or vs code and open terminal there
![image](https://user-images.githubusercontent.com/72795959/147811935-b0ba6950-acc6-40d6-abfd-4d9f04802abf.png)


- Run the following command 
` python manage.py runserver `

![image](https://user-images.githubusercontent.com/72795959/147812044-c4e36612-9486-47e1-9c66-c6d3e42e2584.png)

- And open the following link in your browser
` http://127.0.0.1:8000/ `

##### Using the APIs
- Its a Basic Backend APIs solution. Therefore, I have not focused much on frontend.
![image](https://user-images.githubusercontent.com/72795959/147812271-f9905346-7514-41e7-8b8e-41a9cf484230.png)

- ###### Login 
Login Page conatins two APIs : Get and POST
* GET API shows the All users registered on this Django APP
* POST API Lets you Login in to the Web app using post request passing a json object in correct format.
![image](https://user-images.githubusercontent.com/72795959/147812438-c7ba2349-c498-4c13-bcd4-e5b0e19c5a10.png)

- ###### Signup
Same goes for sign up page
![image](https://user-images.githubusercontent.com/72795959/147812525-f973b175-c37b-483a-b3d0-71ed0be6ddf1.png)

- ###### Cart 
Cart Page conatins two APIs : Get and POST
* GET API shows the All Products added to part of a particular user
* POST API Lets you Checkout the cart to complete order by Adding Address to POST Request.
![image](https://user-images.githubusercontent.com/72795959/147812688-877c70a2-914b-449a-a5b3-c9b4eabc30f0.png)

- ###### Orders 
Order Page conatins one APIs : Get
* GET API shows the All completed order till date of a particular user
![image](https://user-images.githubusercontent.com/72795959/147812752-1293c349-4b17-4ce8-a224-574a77b3ace8.png)

- ###### Product list 
Product list Page conatins to APIs : Get
* GET API shows the All Products added to Django App
![image](https://user-images.githubusercontent.com/72795959/147812851-73f409e3-1fa3-46dc-b60f-c68b0a19a7f6.png)


- ###### Product Detail 
Product Detail Page conatins two APIs : Get and POST
* GET API shows the Specific Product Detail
* POST API Lets you Add that product to the Loged in users Cart
![image](https://user-images.githubusercontent.com/72795959/147812914-1a298fcd-f361-40ad-8cdf-fb2a7ebf8475.png)


This is How the Whole Minimum ECommerce Solution APIs are Working.
