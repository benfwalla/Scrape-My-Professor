# Scrape My Professor

Scrape My Professor is a web application that allows IU students to search
for a class or instructor at IU Bloomington. On one page, users will be 
able to view visuals and analytics about courses and analytics.

Scrape My Professor is still in development. It is being created by a super
team of Python developers at Code@IU. The website is built on the Flask web
framework, which basically allows you to use Python as the backend
programming language. The frontend design uses Bootstrap, and visualizations
were built using the help of Chart.js. When the app is deployed into
full-production, we intend to use Heroku as the hosting platform.

## Create a Local Instance
To use Scrape My Professor on your own computer, simply clone the repository
onto your computer. Navigate to wherever you'd like to locate this repo in
your terminal and insert the following:
```
git clone https://github.com/benfwalla/Scrape-My-Professor.git
```
After the download is complete, move to the root folder of the repository.
In order to run the app, you must activate the virtual environment. The 
virtual environment is where all the external libraries of the flask,
pandas, Python 3, and many others are kept to make this application run.
To activate it, type in the following:

For Windows users: `venv\Scripts\activate`

For Mac users: `source venv/Scripts/activate`

I'm actually not users if this will work on a Mac. Stay tuned for that.

Now, you can run the app. In your terminal, enter: `flask run`

After the server initializes, it will wait for client connections. The 
output from flask run indicates that the server is running on IP address
127.0.0.1, which is always the address of your own computer. This 
address is so common that is also has a simpler name that you may have
seen before: localhost. Flask uses the port 5000. Open up a web browser
and enter the following URL: `http://localhost:5000/`

Scrape My Professor should now be working! To close out the app, either
exit out of your terminal or press Ctrl-C to stop it.