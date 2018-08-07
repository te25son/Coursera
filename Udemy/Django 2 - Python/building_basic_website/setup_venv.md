## Setting up a Virtual Environment

#### *STEP 1:* 

Install a virtual environment (venv) using pip3

`$ pip3 install virtualen`

#### *STEP 2:* 

Move to a location where you would like to store your venv

`$ cd <location>`

#### *STEP 3:* 

Create a venv folder in the sepcified location

`$ virtualenv <venv_name>` 

#### *STEP 4:* 

Activate the venv

`$ source <venv_name>/bin/activate`

#### *STEP 5:* 

Check to make sure you can see `(<venv_name>)` in parathenses before the command line

If so, everything is working fine :-)


#### *STEP 6:* 

To deactivate the venv at any time, type `$ deactivate`

To reactivate the venv, repeat STEP 4

#### *STEP 7:* 

Create a Django project in the venv and create a project name (_make sure the venv is activated for this step_)

`$ django-admin startproject <project_name>`

#### *STEP 8:*

Install Django into the venv after pull yourself into your new project folder

`cd <project_name>`

`pip install django==2.0.2` (the "==" specifies the version of django to be installed. it is not necessary)

