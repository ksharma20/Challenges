# ProgrammingChallenge 
This is to help us understand your programming style and expertise. Getting Started :

For this round, you have to write a simple API server, which fetches data from Github and serializes it in a certain format, and visualizes it in form of charts. 

### It involves a few steps: 
1. Creating a simple back-end API for which you need to make a REST API call to Github's API service and fetch the data 
1. Creating a small front-end application on Django/FastAPI 

**Challenge Duration** - 3 days 

## Backend API 

You will need to write a simple API that returns the top 10 repositories of an organization in Github by stars.

### API Details 
We will send a POST request to your API at /repos with JSON payload containing Github organization name 

For deepvue-tech, this will look like this:
```json
{ 
"org": "deepvue-tech" 
}
``` 
and the API should return a response in the following format (JSON): 
```json
{ 
"results": [ 
{"name":"rick", "stars": 100}, 
{"name":"morty", "stars": 98}, 
{"name":"jerry", "stars":2}, 
] 
}
```
### Metrics 
**Response Time**: Share your findings on response time and the code that you use for the same. 


## Front-End App 

You will need to create a simple Django/FastAPI app with a single view /dashboard having two charts:
- A Bar Chart showing the results of your API i.e Input an organization, plot the top 10 repos and their star counts coming from your end-point. 
- A Line chart showing commits timelines i.e. Input an organization & a repository and select a time range from the time range filter, plot daily total commit during a time range.

## Extras 
3. It is okay to Google or Bing (if that's your thing) 
3. Think through the edge cases, especially for organizations with a large number of repos 
3. Write good, useful docstrings and comments

## Bonus 
4. Add interactivity in graphs/charts to analyze the data coming from APIs 
4. Deploy this as a microservice on a cloud and share the link Submission 
4. Once you are done, email us the solution and findings/notes/logs in a zip file titled <your-name>-fullstack-intern-hiring-challenge.zip

# Solution
