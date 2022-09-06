# Eating Calculator App
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

## About
The Eating Calculator allows user to control his day of eating. After setting daily intake goal of proteins, carbohydrates and fats, user can add his meals to control himself. User can check his day of eating, remaining nutritional values or eaten products at any time of the day. 
The app has also a innovative function which lets user to type any number of products and then the app optimizes amount of each given product to reach the user's daily nutritional goal.

## How to start?
Download the repository and run `pip install -r requirements.txt`. Then run TheEatingCalculator.exe file or run `python src/main.py`.
App uses API to find products. I'm aware that it is using my personal tokens. In this case these tokens are free, so I decided to give open acces to .env file to make checking this application's working nature easier. 
I encourage you to modify the .env file with your own tokens. Acces to these tokens is free and available by this site: https://developer.nutritionix.com/signup.

## Usage example
### Set daily goal
![alt text](https://github.com/milosz-k/Eating-Calculator-App/blob/master/doc/Set.PNG)

### Add new meal
![alt text](https://github.com/milosz-k/Eating-Calculator-App/blob/master/doc/Add.PNG)

### Show eaten energy content
![alt text](https://github.com/milosz-k/Eating-Calculator-App/blob/master/doc/Energy.PNG)

### Calculate remaining nutrients by meal containing following products
![alt text](https://github.com/milosz-k/Eating-Calculator-App/blob/master/doc/Solver.PNG)

### Result of calculation
![alt text](https://github.com/milosz-k/Eating-Calculator-App/blob/master/doc/SolverResult.PNG)

### Eaten products containing calculated meal
![alt text](https://github.com/milosz-k/Eating-Calculator-App/blob/master/doc/ProductsAfterSolver.PNG)

### Daily nutrients intake containing calculated meal
![alt text](https://github.com/milosz-k/Eating-Calculator-App/blob/master/doc/NutrientsAfterSolver.PNG)
