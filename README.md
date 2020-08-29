# Todo App

### Brief

* A simple todo app that allow user to perform simple CRUD operations.


### Technologies Used

1. HTML5
1. CSS3
1. JavaScript 
1. Bootstrap
1. Python v3.8.3 
1. Flask v1.1.2
1. MongoDB Atlas
1. Heroku (Hosting)


#### Packages
(default) - Comes with Flask package during installation

| Package | Version  | Description |
|---    |---    |---    |   
| bson             | 0.5.10 | 
| click            | 7.1.2 | 
| Flask            | 1.1.2 | 
| itsdangerous     | 1.1.0 | 
| MarkupSafe       | 1.1.1 | 
| pip              | 20.2.2 | 
| python-dateutil  | 2.8.1 | 
| setuptools       | 41.2.0 | 
| six              | 1.15.0 | 
| Werkzeug   | 1.0.1 | 

<br>

_(manual) - Require manual installation_

| Package | Version  | Description |
|---    |---    |---    |   
| dnspython        | 2.0.0 | DNS Tookit for Python
| Flask-PyMongo    | 2.3.0 |
| gunicorn         | 20.0.4 | Deployment to Heroku 
| Jinja2           | 2.11.2 | Templating language accompany to with Flask usage
| pymongo          | 3.11.0 | Usage of Mongo driver and syntax
| python-decouple  | 3.3 | Use to select environment variables from .env
| pytz             | 2020.1 | Python Timezone use to display timezone from datetime
 

*(They can be found in requirements.txt)*


### Instructions - Setup project and deployment

#### (Project folder)

1. Create a project folder
    ```
    C:\Users\to\Path> mkdir <project-name>
    ```

#### (Git and Github)

1. Create a new repository for your project on your local computer, within the project folder
    ```
    > git init .                  // initialize repo with all files
    > git add .                   // add all files into local staging
    > git status                  // check if any files are left out before commiting
    > git commit -m <message>     // commit change with message of your files into repo
    ```
2. Add your remote git link for uploading your files onto Github later on.
    ```
    > git remote add origin <your-remote-git-link>    // add your remote repo link
    ```
3. Push your files onto your remote
    ```
    > git push -u origin master   // upload your files into your remote repo
    ```

4. Should you have the interest to work the files offline, you can do so by cloning a copy.
    ```
    > git clone <remote-link>     // Clone the selected repo offline
    ```

### (Flask)
1. Install Flask using pip package manager
    ```
    pip install Flask
    ```

2. Create a virtualenv
    ```
    > cd <project-name>
    > python3 -m venv venv
    ```

3. Activate the environment
    ```
    > venv\Scripts\activate
    ```

4. Tell the terminal to run application

    ```
    # From Powershell
    ------------------------
    > PS C:\path\to\app> $env:FLASK_APP = "<app-name>.py"

    # Run the application
    ------------------------
    > python -m flask run
    * Running on http://127.0.0.1:5000/
    ```

5. Make sure to create an .env, environment file to store your credentials in your project directory
    ```
    # Create .env file in project directory
    ------------------------
    > echo env-var-1=some env-var-2=some env-var-3=some > .env
    
    # View .env file
    ------------------------
    > type .env
    ```


#### (Heroku)
1. Install Heroku CLI refer to the [website](https://devcenter.heroku.com/articles/heroku-cli) to install package

2. Log into Heroku via CLI
    ```
    > heroku login
    ```

3. Set environment in Heroku config
    ```
    > heroku config:set <env-var-1>=<value> <env-var-2>=<value> <env-var-3>=<value>
    ```



## Summary
_*** This guide is created for Windows platform based projects_