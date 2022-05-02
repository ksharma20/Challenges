# Problem 

We are an AI-IoT company and need a maverick python-django web developer to help us with our Cloud Dashboard.
This is a small test for you to check if you can take a website template (django/python/bootstrap) and can create couple of pages. If you are able to do that then welcome onboard.

What is the dashboard and what it does ?

- A dashboard gives details of the fleet of IoT devices for  a user,
- A user can have one or more devices like raspberry pi etc,
- Each is running some linux OS and some apps.
- Dashboard simly shows a list of online / offline devices and how can we see what is running on them.

The sample template is
- https://www.creative-tim.com/live/soft-ui-dashboard-django,
- https://github.com/creativetimofficial/soft-ui-dashboard-django,
- https://www.creative-tim.com/product/soft-ui-dashboard-django,

I need you to design 2 pages with minimal elements This are two screen shots from a similar website

**Page 1 - List of devices**

So your task is to design a similar page which shows
1. side bar
2. list view
3. Buttons (Add Device)
- Rest you can remove.
 

**Page 2-  Device Info**

- This  screen comes when you click on one of the devices
- What you have to show
- Side bar
- Device Info (same holy bird one)
- Botton Services list view
- Logs and Terminal showing nothing, you can pick any graph UI element from the Soft-UI template.


# Solution 
For the demonstartion Purpose and to keep it bare minimum 

### Download the solution
Download Link = [Emvirt Task Solution](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/ksharma20/Challenges/tree/main/Emvirt)

**Please consider downloading it from the above link so you get current project related dir**
![image](https://user-images.githubusercontent.com/72795959/166184978-943432a2-ff55-4c6a-b784-665bcb47cc92.png)

After you click on link you download will start in 5 secs !


### These are the steps I followed :
- Created a basic model class 

![model](https://user-images.githubusercontent.com/72795959/166142468-4ca0d60b-1318-42d6-9d0b-60cb0e4d9288.png)

- Created 2 Basic pages using bootstrap (1. Home & 2. Detail/Info )
- Home page contains:
  * A sidebar
  * A List View of machines
  * Add Device Button

![image](https://user-images.githubusercontent.com/72795959/166142531-4ca7379a-e9b9-43b6-8200-447727ae0de3.png)


- Detail Page Contains:
  * A side bar
  * Device Info
  * Services
  * Logs Image
  * Terminal Image
  
![image](https://user-images.githubusercontent.com/72795959/166142544-eff129b0-a53a-4f48-87b7-756a8dde538e.png)

