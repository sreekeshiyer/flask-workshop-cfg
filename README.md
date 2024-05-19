## Local Setup

### Create a new python environment
```bash
cd ./todo-app
# or
cd ./todo-simple

# Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv .venv
source .venv/bin/activate

# macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
py -3 -m venv .venv
# Use forward slashes if you are using Git Bash
.venv\scripts\activate
```

### Install all Dependencies
```bash
pip install -r requirements.txt
```

### Setup Firebase

Login to your Google Cloud account on [Firebase Dashboard](https://firebase.google.com/).
Create a new Project; and under Project Settings, generate a new Private Key in the Service accounts section.

![Firebase Project Settings - Service accounts screen](https://github.com/sreekeshiyer/flask-workshop-cfg/assets/67017933/2868d209-e064-4df1-9c4f-b9ebfcede22f)

### Run your app

```bash
python3 app.py
## Alternatively
flask run
```

### Deploying to Render

![Adding a secrets file on Render](https://github.com/sreekeshiyer/flask-workshop-cfg/assets/67017933/13d419cf-a2b1-43fe-b60e-97da90279dc1)

You'll need to add your `credentials.json` file to the secrets when you're deploying the app to Render. 

## What the final app looks like
![A screenshot of the website homepage showing a list of todos](https://github.com/sreekeshiyer/flask-workshop-cfg/assets/67017933/7dacfac2-95d0-4129-9d9c-88f76ee98e3d)


Developed with 💙 on
         
         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 
