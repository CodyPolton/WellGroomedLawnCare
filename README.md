# Quick Start

**Before running install:**
1. [Visual Studio Code](https://code.visualstudio.com/download) (Code Editor Used for this projects development)
2. [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) (Used to maintain consistant coding style)
3. [npm](https://www.npmjs.com/get-npm) (Open Source Package Manager)

## Download

```bash
#Create a directory and enter it

mkdir WellGroomedLawnCare
cd WellGroomedLawnCare

#Download repository
git clone git@github.com:CodyPolton/WellGroomedLawnCare.git

### Install and Run the Frontend

```bash
#Go to front end directory
cd frontend

#install front end dependencies
npm install

#Start app for dev on server
npm run serve

#In browser, navigate to:
http://localhost:8080/
```

### Install and Run the Backend

```bash
#Go to front end directory
cd backend

#install backend dependences
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

#go into django framework folder
cd backend-framework

#Start django dev server
django manage.py runserver

```