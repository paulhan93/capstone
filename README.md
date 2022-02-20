# 4G Client Project Tracker
4G Clinical is a software company that helps “bring crucial medicine to those who need them, faster”.  
They help sponsors and CROs (Contract Research Organizations) accelerate clinical research by providing 
RTSM (Randomization and Trial Supply Management) and supply forecasting services.

Currently, 4G Clinical’s main form of communication with their clients is email and occasional Zoom meetings. There are several known issues with email communication and 4G would like to introduce a more sophisticated form of communication.

The scope of this project will include developing an external hub that 4G clients can use to better communicate with 4G.  The client hub should include a project milestone tracker, a discussion board, and a basic document sharing tool.  APIs will be used to integrate each of the requirements to the website.

---
# Running the App Locally
1. Have python3 installed (3.9.10 listed in pyvenv.cfg)
2. Run ``` env\Scripts\Activate ``` (windows might ask you to enable scripts)
3. CD into ``` my_app ``` directory
4. Run ``` python manage.py runserver ```
5. Type into a web browser ``` http://127.0.0.1:8000/admin ``` for the admin page or ``` http://127.0.0.1:8000/hello ``` for the hello page
6. To exit the virtual env, type ``` deactivate ``` in terminal
7. To stop the django app, type ``` ctrl-v ``` in terminal 