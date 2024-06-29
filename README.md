# kitws-ces-automation

This is my B.Tech college(KitsW) Course Exit Survey. Basically, we have to fill out the form after every semester. Usually, it was typing the values from 1-5 but recently, the filling pattern has changed. However, I am too lazy to do it manually, so I automated it.

If you are lazy like me, you can use this script to fill out the form automatically.

## How to Use this Python Script for Options Selector CES

### Step 1: Ensure Python is Installed
Make sure you have Python installed on your system. You can download it from <b><sup>[Python's official website](https://www.python.org/downloads/)</sup></b>.



### Step 2: Download the Repository
Download this repository using your preferred method (e.g., zip, ssh, http).

### Step 3: Download Chrome Web Driver
Download the Chrome Driver that matches your Chrome browser version from <b> <sup>[Here](https://sites.google.com/chromium.org/driver/downloads)</sup></b>.

It is suggested that you keep the chrome driver in the same directory as the script.

### Step 4: Open the Directory
Open this directory in your command-line interface (CLI) or favorite IDE.

### Step 5: Set up the virtual environment.

#### For Mac and Linux (I made this script in this environment):

<i> 

```
sudo apt-get install python-pip
pip install virtualenv
python -m venv .venv
source .venv/bin/activate
```
</i>

#### For Windows:

<i>

```
pip install virtualenv
python -m venv .venv
.venv\Scripts\activate (or) .venv\Scripts\activate.bat
```
</i>

### Step 6: 

Run the following command to install the required packages:
<i>
```
pip install -r requirements.txt
```
</i>

### Step 7: 

Create a file with the name <b>`.env`</b> and add your username, password, and chrome driver path like this (do not change variable names in the <b>`options_selector_ces.py`</i>):

<b>

```
STORE_YOUR_UNAME = 'your username here'
STORE_YOUR_USERPASSWORD = 'your password here'

STORE_YOUR_PATH_TO_CHROME_DRIVER = 'path to the chrome driver' 
```
</b>

### Step 8: 

If the CES is in the options selecting format, then run the following command to execute the script:
<i>

```
python options_selector_ces.py
``` 
</i>


# If the CES is in the text box format, follow these steps to complete CES easily
it is sometime text based CES, so here is the solution for that.

## How to Use this JS for typing values CES

### Note: This is a JS script that will fill the text box with the given text.

### Step 1: Open the browser and go to the CES page.
### Step 2: Login with your Credentials.
### Step 3: Open the console by pressing F12 or right-clicking. 
### Step 4: Go to the "Console" tab.
### Step 5: Copy the following code and paste it into the console.

<i>

```
a = document.querySelectorAll('input');
a.forEach(a => { a.value = 5; });
```
</i>

This will fill all the text boxes with the value 5.

### Step 6: Press Enter.

That's it, guys! You have successfully filled the text box with the given text without any stress and manual work.


[![Static Badge](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54)](https://www.python.org/downloads/) [![Static Badge](https://img.shields.io/badge/selenium-white?logo=selenium)](https://www.python.org/downloads/) 
[![Static Badge](https://img.shields.io/badge/dotenv-gray?logo=dotenv)](https://www.python.org/downloads/)

<!-- [![Static Badge](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/downloads/) -->