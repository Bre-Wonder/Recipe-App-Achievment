# Recipe App Python

### Project Description
The objective of this project is to build out the command line version of a Recipe App that will build out in a later project as a web app.

### Technologies Used:
Python | virtualenvwrapper | ipython shell |


### How to start this Project:

* Install Python, at the time of writing this Python 3.13.5. I was able to do this by going to Python's website and using their MacOS installer. 
* Create yourself a virtual environtment by typing this command into your terminal (for MacOS users) : `pip3.13 install virtualenvwrapper` (note pip is automatically installed when you install Python)
* Confirm your terminal knows the path to this virtualenvwrapper install by typig this into your terminal: `which virtualenvvwrapper.sh`
* Modify Shell Start Up File by running `sudo nano ~/.zshrc` for MacOS 10.15 or newer. 
* Add these lines the bottom of the file that is showing in the terminal by typing this in at the very end:
  `export VIRTUALENVWRAPPER_PYTHON=$(which python3.8)`
   `source $(which virtualenvwrapper.sh)`
  Then be sure to close the editor by pressing Ctrl X and they type Y and press enter. This will modify the shell start up file so that it will always show up.
* To create your own new virtual environment type in your terminal this command: 
  `mkvirtualenv   <your-chosen-environment-name>`
* Note: see terminal commands defined - `deactivate`, use to deactivate a virtual environment. `workon`, to display all options of install environments. `workon <environment name>`, to load an installed environment. `rmvirtualenv <environment name>`, remove installed environment. 
* You have many places you can go from here. You can create a script in your preferred IDE and once saved you    can navigate to it in your terminal. Once in your terminal, you can run the command: `python3 <name-of-your-script-file>`. For example if you named your script `app.py`, you would write - `python3 app.py` in your terminal. This will run the Python commands in your script file. Be sure to make sure you are in your virtual environment.
* Another option you have to run Python code is to run the Python code in your command line. Once in your virtual environment, you can just type `python3` and then begin by writing the command directly into the terminal. 
* Note: If you would like to install the ipython shell you can type: `pip install ipython`.
* Creating a Requirement.txt File: First, go to the desired directory in your terminal. Second, run you chosen virtual environment. Third, type this command into your terminal and it will create a requirement.txt file for you - `pip freeze > requirements.txt`. 


### API Use


### Lessons Learned:
Python can be used in virtual environments and run in command line. The virtual environments keep the dependancies clear and organized since different scripts can require different dependancies. Having Pythong work in a command line is very convient as you can test the code even before it goes into a scrip file. Python also has a requirement.txt file that is really helpful if you want to know what an application is using and easily download that installation and modules to recreate the environment. 


### What would I do differently? 


GitHub Repository site: 

Live Site:  
