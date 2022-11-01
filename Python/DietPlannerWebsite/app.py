from flask import Flask, render_template, request
import csv
from Food import Food
import random

GOAL_CALORIES = 2000
GOAL_PROTEIN = 128
GOAL_CARBOHYDRATES = 250
GOAL_FATS = 56
NO_ITERATIONS=10
app = Flask(__name__)

def calculate(age, height, weight, gender, activity):
    if gender == "Male":
        bmr = 66.5 + (13.75 * weight) + (5.003 * height) - (6.75 * age)
    elif gender == "Female":
        bmr = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
    if activity == "Sedentary":
        calories = bmr * 1.2
    elif activity == "Lightly Active":
        calories = bmr * 1.375
    elif activity == "Moderately Active":
        calories = bmr * 1.55
    elif activity == "Very Active":
        calories = bmr * 1.725
    elif activity == "Extremely Active":
        calories = bmr * 1.9
    return int(calories)



@app.route('/')
def my_home():
    return render_template('plan.html')


@app.route('/submit_details', methods=['POST', 'GET'])
def submit_details():
    if request.method == 'POST':
        data = request.form.to_dict()
        age = int(data['age'])
        height = int(data['height'])
        weight = int(data['weight'])
        gender = data['gender']
        activity = data['activity']
        cals = calculate(age, height, weight, gender, activity)
        prot = int((cals * 0.25) / 4)
        carbs = int((cals * 0.5) / 4)
        fat = int((cals * 0.25) / 9)
        return render_template("nutrients.html", cals=cals, protein=prot, fat=fat, carbs=carbs)
    else:
        return 'something went wrong, try again'

Foods = []
with open('foods.csv') as foods_csv:
    csv_reader = csv.reader(foods_csv, delimiter=',')
    line_count = 0
    for row in foods_csv:
        row_split = row.split(",")
        row_split[-1] = row_split[-1].replace("\n", "")
        Foods.append(Food(name=row_split[0], cals=row_split[1], carbg=row_split[2], proteing=row_split[3], fatg=row_split[4]))

def generatePlan():
    totalCalories = 0
    mealPlan = []
    while totalCalories < GOAL_CALORIES:
        currentFood = random.choice(Foods)
        mealPlan.append(currentFood)
        totalCalories += int(currentFood.cals)
    return mealPlan

def comparePlans(first, second):
    firstScore = getScore(first)
    secondScore = getScore(second)
    if firstScore > secondScore:
        return 2
    else:
        return 1

def getScore(mealPlan):
    protein, fat, carbs = 0,0,0
    for meal in mealPlan:
        protein += int(meal.proteing)
        fat += int(meal.fatg)
        carbs += int(meal.carbg)
    carbs_dif = abs(GOAL_CARBOHYDRATES - carbs)
    fat_dif = abs(GOAL_FATS - fat)
    protein_dif = abs(GOAL_PROTEIN - protein)
    total_dif = carbs_dif + fat_dif + protein_dif
    return total_dif

def print_plan(meal_plan):
    for meal in meal_plan:
        print(f"{meal.name} - {meal.cals} cals, {meal.fatg}g fat, {meal.carbg}g carbs, {meal.proteing}g protein")

@app.route('/generate_plan', methods=['POST', 'GET'])
def plan():
    if request.method == 'POST':
        data = request.form.to_dict()
        cals = int(data['cals'])
        carbs = int(data['carbs'])
        protein = int(data['prots'])
        fat = data['fats']
        GOAL_CALORIES=cals
        GOAL_CARBOHYDRATES=carbs
        GOAL_PROTEIN=protein
        GOAL_FATS=fat
        planA = generatePlan()
        planB = generatePlan()
        x = 0
        while x < NO_ITERATIONS:
            bestPlan = comparePlans(planA, planB)
            if bestPlan == 1:
                planB = generatePlan()
            if bestPlan == 2:
                planA = generatePlan()
            x += 1
        bestPlan = comparePlans(planA, planB)
        if bestPlan == 1:
            print("PLAN A")
            print("----------")
            print_plan(planA)
        if bestPlan == 2:
            print("PLAN B")
            print("----------")
            print_plan(planB)
        return render_template("plan.html")
    else:
        return 'something went wrong, try again'