## This is a web application using Django REST framework + React for powerline visulization, with data provided by Prof. Chalgham and GIRS @UCLA.

[login page](http://ec2-52-53-245-35.us-west-1.compute.amazonaws.com:3000/)

username: ucla

password: girs


Planned to be finished within 5 days during school visit, but other factors (hardware technical problems, getting covid...) affacted the development process and extended it to be 10 days.

## Stages of development: 

1. Preparing for the backend: learning Django, getting the data ready, etc. 
2. Preparing for the frontend: reviewing React components.
3. Backend development: building the database, models, and views with Django, creating endpoints for the frontend to call.
4. Frontend development: coding the logics and components. 
5. Integration and deployment: integrating the seperated backend and frontend, learning and deploying on AWS EC2.

## Other available endpoints: 

Access to all:

- **POST:** [POST to the end](http://ec2-52-53-245-35.us-west-1.compute.amazonaws.com:8000/list)

Access to one: 

- **GET:** [GET the 100th pwerline](http://ec2-52-53-245-35.us-west-1.compute.amazonaws.com:8000/detail/100)

- **PUT:** same as above

- **DELETE:** smave as above

## To be improved: 

1. (General) A more detailed Gantt chart can be used, divide the whole task and conquer the smaller tasks. Can be devided even more. 
2. (Django) function views VS class views?
3. (Django) Auth not completed enough. Very convenient wheels already exist and can be used. 
4. (Deployment) Docker
5. TBD


 
