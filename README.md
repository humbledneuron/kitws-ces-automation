# kitws-ces-automation

This is my B.Tech college(KitsW) Course Exit Survey. Basically, we have to fill out the form after every semester. Usually, it was typing the values from 1-5 but recently, the filling pattern has changed. However, I am too lazy to do it manually, so I automated it.

If you are lazy like me, you can use this script to fill out the form automatically.

## How to Use this Python Script for Options Selector CES

### Step 1: Make sure you have Python installed on your OS.

### Step 2: Download this repository using your preferred method (e.g., zip, ssh, http).

### Step 3: Download the Chrome Driver for your preferred OS with the version of your Chrome browser from the following link:

[https://sites.google.com/chromium.org/driver/downloads](https://sites.google.com/chromium.org/driver/downloads)

### Step 4: Open this directory in your command-line interface (CLI) or favorite IDE.

### Step 5: Set up the virtual environment.

#### For Mac and Linux (I made this script in this environment):

```
sudo apt-get install python-pip
pip install virtualenv
python -m venv .venv
source .venv/bin/activate
```

#### For Windows:

```
pip install virtualenv
python -m venv .venv
.venv\Scripts\activate (or) .venv\Scripts\activate.bat
```

### Step 6: 

Run the following command to install the required packages:

```
pip install -r requirements.txt
```

### Step 7: 

Create a file with the name `.env` and add your username, password, and chrome driver path like this (do not change variable names):

```
STORE_YOUR_UNAME = 'your username here'
STORE_YOUR_USERPASSWORD = 'your password here'

STORE_YOUR_PATH_TO_CHROME_DRIVER = 'path to the chrome driver' 
```

It is suggested that you keep the chrome driver in the same directory as the script.

### Step 8: 

If the CES is in the options selecting format, then run the following command to execute the script:

```
python options_selector_ces.py
``` 

# If the CES is in the text box format, follow these steps to complete CES easily
it is sometime text based CES, so here is the solution for that.

## How to Use this JS for typing values CES

### Note: This is a JS script that will fill the text box with the given text.

### Step 1: Open the browser and go to the CES page.
### Step 2: Login with your Credentials.
### Step 3: Open the console by pressing F12 or right-clicking. 
### Step 4: Go to the "Console" tab.
### Step 5: Copy the following code and paste it into the console.

```
a = document.querySelectorAll('input');
a.forEach(a => { a.value = 5; });
```

This will fill all the text boxes with the value 5.

### Step 6: Press Enter.

That's it, guys! You have successfully filled the text box with the given text without any stress and manual work.

