# Todo App

### Brief

* A simple todo app that allow user to perform simple CRUD operations.

<br>

### Technologies Used

1. HTML
1. Bootstrap
1. Python v3.8.3 
1. Flask v1.1.2
1. MongoDB Atlas
1. Heroku (Hosting)

<br>

#### Packages
(default) - Comes with Flask package during installation

1. **_bson==0.5.10_**
1. **_click==7.1.2_**
1. **_Flask==1.1.2_**
1. **_itsdangerous==1.1.0_**
1. **_MarkupSafe==1.1.1_**
1. **_python-dateutil==2.8.1_**
1. **_six==1.15.0_**
1. **_Werkzeug==1.0.1_**

(manual) - Require manual installation
1. **_dnspython==2.0.0_** - 
1. **_gunicorn==20.0.4_** - Deployment to Heroku
1. **_Jinja2==2.11.2_** - Templating language accompany to with Flask usage
1. **_pymongo==3.11.0_** - Usage of Mongo driver and syntax
1. **_Flask-PyMongo==2.3.0_**
1. **_python-decouple==3.3_** - Use to select environment variables from .env

<br>

*(They can be found in requirements.txt)*

<br>

### Instructions - Setup project and deployment

<br>

### (Project folder)

1. Create a project folder
    ```
    C:\Users\to\Path> mkdir <project-name>
    ```

<br>

### (Git and Github)

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

<br>

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


### (Heroku)
1. Install Heroku CLI refer to the [website](https://devcenter.heroku.com/articles/heroku-cli) to install package

2. Log into Heroku via CLI
    ```
    > heroku login
    ```

3. Set environment in Heroku config
    ```
    > heroku config:set <env-var-1>=<value> <env-var-2>=<value> <env-var-3>=<value>
    ```


<br>


## Summary
_*** This guide is created for Windows platfrom based projects_