# 4G Client Project Tracker
4G Clinical is a software company that helps “bring crucial medicine to those who need them, faster”.  
They help sponsors and CROs (Contract Research Organizations) accelerate clinical research by providing 
RTSM (Randomization and Trial Supply Management) and supply forecasting services.

Currently, 4G Clinical’s main form of communication with their clients is email and occasional Zoom meetings. There are several known issues with email communication and 4G would like to introduce a more sophisticated form of communication.

The scope of this project will include developing an external hub that 4G clients can use to better communicate with 4G.  The client hub should include a project milestone tracker, a discussion board, and a basic document sharing tool.  APIs will be used to integrate each of the requirements to the website.

---
## Running the App Locally - WINDOWS
1. Have python3 installed (3.9.10)
2. Delete any existing virtual environment folder and create a new one using command ``` python3 -m venv venv ``` in the first my_app folder
3. Run ``` venv\Scripts\Activate ``` (windows might ask you to enable scripts) to activate the virtual environment
4. Run ``` pip install -r requirements.txt ``` to install dependencies 
5. Run ``` python manage.py runserver ``` to run django site
6. Type into a web browser ``` http://127.0.0.1:8000/admin ``` for the admin login page or ``` http://127.0.0.1:8000/home ``` for the home page
7. To exit the virtual env, type ``` deactivate ``` in terminal
8. To stop the django app, type ``` ctrl-v ``` in terminal 

---
## Mac Users
These instructions are for MAC, so if you use a different machine, your commands will probably be different.
1. Pull this repo to your local machine
2. Install Python3 if you do not have it already installed
    - Run ```% python3 -V``` to check 
3. Navigate to the project directory (```~/GitHub/capstone```)
3. Create a virtual environment (```% python3 -m venv env```)
4. Activate the virtual environment (```% source env/bin/activate```)
    - To deactivate the virtual environment, run ```% deactivate ``` 
5. Run ```% pip install -r requirements.txt``` to install project environment dependencies
    - Run ```% pip freeze```, this should output the contents of requirements.txt file
6. Run ```% django-admin``` to see a list of django commands
7. cd into the src directory; this is the root directory (wherever manage.py lives)
    - Run ```% python manage.py runserver``` to run the server locally
    - Go to http://127.0.0.1:8000/, you should see a basic Django page
8. To create a super user, run ```% python manage.py createsuperuser``` and follow the steps to create an account
    - Go to http://127.0.0.1:8000/admin to sign in and play around 
9. To create an app, run ```% python manage.py startapp <app_name>```
    - Each app should handle one task really well
    - We can create an app to create objects, set up pages, etc.
