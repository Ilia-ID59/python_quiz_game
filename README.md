# Python Quiz Game
![Static Badge](https://img.shields.io/badge/python-3.12-blue)


A simple quiz game built python

## Table of contents

- [Python Quiz Game](#python-quiz-game)
- [Table of contents](#table-of-contents)
- [Features](#features)
- [Project structure](#project-structure)
- [requirments](#requirments)
- [Installation](#installation)
- [Envoirment setup](#envoirment-setup)
- [Usage](#usage)
- [Example Output](#example-output)
- [Screenshot](#screenshot)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Licence](#licence)
- [Author](#author)

## Features

- Quiz System
  - Asks the player multiple question
  - Checks the answers automaticlly
  - Calcolates the final score
- Resulte storage  
  - Saves quiz results in `results.txt`
- Admin Mode 
  - aske for the admin password 
  - checks if the password is correct
  - keeps the private information outside the main
- python file 
  - loads the password from `.env`

## Project structure

```text
python_quiz_game/
│   .env.example
│   .gitignore
│   main.py
│   question.py
│   README.md
│   requirements.txt
│
├───gifs
│       demo.gif
│
├───pictures
│       1.png
│       2.png
│       3.png
└───
```

### File description

| file | description |
| --- | --- |
| `main.py` | main file used to run quiz game |
| `question.py` | stores questions and answer |
| `requirements.txt` | list the python package neede for the project |
| `.env.example` | shows the envoirmant variables needed by the project |
| `.gitignore` | tells git which files and foldersshold not be tracked |
| `README.md` | contains the project documantation |
| `pictures/` | stores project screenshot |
| `pictures/1.png` | screenshot of the game start |
| `pictures/2.png` | screenshot of the quiz section |
| `pictures/3.png` | screenshot of the final result |
| `gifes/` | stores demo GIF files |
| `gifs\demo.gif` | shows the project demo |

## requirments

before runnig the project, make sure you have :
- ` python 3 `
- ` python-dotenv `

## Installation 

1. open a trminal in the project folder.
2. 2. check that python is installled : 
```bash
python --version
```
3. install the python packages : 
```bash 
pip install -r requirements.txt
```

## Envoirment setup

1. create a `.env` file form `.env.example` : 
```bash 
cp .env.example .env
```
2. open the new `.env` file
3. replace the example value with own password 
```text 
QUIZ_ADMIN_PASSWORD = your_password_here
``` 
4. save the file 
> do not commit your `.env` file because it may contain private information

## Usage

1. open a terminal in the project folder 
2. run the quiz game 
```bash 
python main.py 
``` 
3. choose `yes` or `no` for admin mode  
4. if you choose `yes`, enter the password from your `.env` file 
5. enter your name 
6. answer the question 
7. see your final score and message 
8. your result is saved in `results.txt`

## Example Output 

```text 
do u want to open admin mode ? yes/no : no

whats your name ? al
welcome

 what language are we using ? a
wrong

 what command starts a git ? git init
correct

 what command shows git status ? git status
correct

you score is :  2 out of  3
good job al
```

## Screenshot

### start game
![start game](pictures\1.png)

### quiz
![quiz](pictures\2.png)

### final score
![final score](pictures\3.png)

## Demo
![quiz game demo](gifs\demo.gif)


## Roadmap

- [x] add multiple quiz question 
- [x] calculate the final score 
- [x] save results to a file 
- [x] add admin mode 
- [ ] add more quiz question 
- [ ] add difficultly levels 
- [ ] add a timer 

## Contributing 

## Licence 

## Author

creat by [ilia](https://github.com)