# djangoProject

Hi! This is a sample **django project** with a couple of apps. This basically is for helping understand how the framework works and what are some functionalities that can be achieved using this framework. 


# Setup

 - Clone the project.
 - Create a virtual environment using **pipenv** or **venv** (*Preffered [pipenv](https://pipenv-fork.readthedocs.io/en/latest/)*)
 - Install all the requirements from the ***Pipfile***

## Running the project

Once you are done with the setup, open a terminal in the project's root folder.

 - Activate the virtual environment. - `pipenv shell`
 - Move in to the folder `src` which contains the file  `manage.py`
 - Hit the following commands:
	 - `python manage.py makemigrations`
	 - `python manage.py migrate`
	 - `python manage.py migrate --run-syncdb`
	 - Finally to run the project - `python manage.py runserver`

## Contributions

I would love contributions, so please feel free to fix bugs, improve things, provide documentation. Just send a pull request and help me make this a better and helpful resource.
