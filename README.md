# Eating Calculator App
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

## About
The Eating Calculator allows user to control his day of eating. After setting daily intake goal of proteins, carbohydrates and fats, user can add his meals to control himself. User can check his day of eating, remaining nutritional values or eaten products at any time of the day. 
The app has also a innovative function which lets user to type any number of products and then the app optimizes amount of each given product to reach the user's daily nutritional goal.

## How to start?
### Option 1
Download the repository and run TheEatingCalculator.exe file.
I'm aware that .exe file is using my personal tokens. In this case these tokens are free, so I decided to give open acces to .env file to make checking this application's working nature easier.

### Option 2
Download the repository and modify the env. file with your own tokens. Acces to these tokens is free and available by this site: https://developer.nutritionix.com/signup.
After modifying .env file, you can run `python src/main.py`.

## Usage example
### Set daily goal
![alt text](https://github.com/milosz-k/Eating-Calculator-App/blob/master/src/img/Set.PNG)

### Add new meal
![alt text](https://github.com/milosz-k/Eating-Calculator-App/blob/master/src/img/Add.PNG)

### Show eaten energy content
![alt text](https://github.com/milosz-k/Eating-Calculator-App/blob/master/src/img/Energy.PNG)

### Calculate remaining nutrients by meal containing following products
![alt text](https://github.com/milosz-k/Eating-Calculator-App/blob/master/src/img/Solver.PNG)

### Result of calculation
![alt text](https://github.com/milosz-k/Eating-Calculator-App/blob/master/src/img/SolverResult.PNG)

### Eaten products containing calculated meal
![alt text](https://github.com/milosz-k/Eating-Calculator-App/blob/master/src/img/ProductsAfterSolver.PNG)

### Daily nutrients intake containing calculated meal
![alt text](https://github.com/milosz-k/Eating-Calculator-App/blob/master/src/img/NutrientsAfterSolver.PNG)
