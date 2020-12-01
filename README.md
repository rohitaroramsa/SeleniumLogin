# Assessment

This test assessment was prepared for . 

## Project Structure
Assessment project is built across multiple folders: 
- features: All the .feature files (Gherkin files/BDD Files) are present inside this folder.
- features/Steps: All the step definitions are present inside this folder. file name should match the feature file name.
- Screenshots: To capture any evidences/screenshots.
- pages: I have followed Page Object Model. So all webelements and the functions/methods to interact with them (get/set) are grouped here inside python files for each of the web page. 

## Setup & Installations
##### Python
Python can be downloaded from [Download Python link](https://www.python.org/downloads/).

##### Chrome Driver
Chrome WebDriver can be downloaded from this [link](https://chromedriver.chromium.org/downloads).

##### Dependencies & Installation
This Python based Test Automation project has 2 major python dependecies:
- Selenium (To interact with the WebDriver)
- Behave (For BDD Test Implementation)

They both are written in file requirement.txt. When user will open this file in any modern Python IDE such as PyCharm Community Edition, IDE will suggest downloading these dependencies and will download itself.
User can run following commands inside Terminal/command prompt to install these python dependencies:
```sh
$  pip install requirements.txt 
```
or install them individually:
```sh
$ pip install selenium 
$ pip install behave
```

## Execution
Path of the downloaded Chrome WebDriver exe file should be updated in features\environment.py. After that project is ready for execution.
##### Way 1 using Terminal 
In terminal, go to the path of root folder using command cd <path>. Afterwards you can run following command:
```sh
$ behave features 
```
This command will execute all feature inside features & steps folder.
Python behave terminal command also accepts several paramters which are available on behave official documentation site [Behave Documetation Link](https://behave.readthedocs.io/en/latest/index.html). 

##### Way 2 using python file
I have created a python file features_runner.py which can be run as simple python file. It will also execute features files in the path specified inside the file. It's a wayaround to use terminal and running behave command. I can also configure any CLI parameters in this file.