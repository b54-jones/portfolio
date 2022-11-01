import csv
from Food import Food
import random
import requests
import lxml.html

GOAL_CALORIES = 2000
GOAL_PROTEIN = (GOAL_CALORIES * 0.25) / 4
GOAL_CARBOHYDRATES = (GOAL_CALORIES * 0.5) / 4
GOAL_FATS = (GOAL_CALORIES * 0.25) / 9
NO_ITERATIONS = 5

Foods = []
with open('DietPlannerConsole/foods.csv') as foods_csv:
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
    totalCals = 0
    totalFat = 0
    totalCarb = 0
    totalProtein = 0
    for meal in meal_plan:
        print(f"{meal.name}")
        totalCals += int(meal.cals)
        totalFat += int(meal.fatg)
        totalCarb += int(meal.carbg)
        totalProtein += int(meal.proteing)
    print(f"Total Calories: {totalCals}")
    print(f"Total Fat: {totalFat}")
    print(f"Total Carbohydrates: {totalCarb}")
    print(f"Total Protein: {totalProtein}")

def plan():
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
        print_plan(planA)
    if bestPlan == 2:
        print_plan(planB)

def writeToFile(name, cals, carb, protein, fat):
    with open('DietPlannerConsole/foods.csv', mode='a', newline='\n') as foods:
        foods_writer = csv.writer(foods, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        foods_writer.writerow([name, cals, carb, protein, fat])

def getFoodFromSite(url):
        #works with BBC Good Food links
        r = requests.get(url)
        tree = lxml.html.fromstring(r.text)
        depth = 3
        #Some recipes have the nutrition information embedded a bit deeper
        kcals_tree = tree.xpath("/html/body/div[1]/div[3]/main/div/section/div/div[3]/table/tbody[1]/tr[1]/td[3]")
        if kcals_tree != []:
            kcals = kcals_tree[0]
        else:
            depth = 2
            kcals = tree.xpath("/html/body/div[1]/div[3]/main/div/section/div/div[3]/table/tbody[1]/tr[1]/td[2]")[0]
        name = tree.xpath("/html/body/div[1]/div[3]/main/div/section/div/div[3]/div[1]/h1")[0]
        fat = tree.xpath(f"/html/body/div/div[3]/main/div/section/div/div[3]/table/tbody[1]/tr[2]/td[{depth}]")[0]
        carbs = tree.xpath(f"/html/body/div/div[3]/main/div/section/div/div[3]/table/tbody[1]/tr[4]/td[{depth}]")[0]
        protein = tree.xpath(f"/html/body/div/div[3]/main/div/section/div/div[3]/table/tbody[2]/tr[3]/td[{depth}]")[0]

        name = name.text_content()
        kcals = int(kcals.text_content())
        fat = int(fat.text_content().replace("g", ""))
        carbs = int(carbs.text_content().replace("g", ""))
        protein = int(protein.text_content().replace("g", ""))

        writeToFile(name, kcals, carbs, protein, fat)

def addFood():
    while True:
        link = input("Enter a BBC Good Food link or N if you don't have one: ")
        if link == "N":
            name = input("Name: ")
            kcals = input("KCals: ")
            carbs = input("Carbs: ")
            protein = input("Protein: ")
            fat = input("Fat: ")
            writeToFile(name, kcals, carbs, protein, fat)
        else:
            getFoodFromSite(link)
        again = input("Add another food? Y or N: ")
        if again == "N":
            break


while True:
    choice = input("What would you like to do today? ADD to add a food, PLAN to make a diet plan ").upper()
    if choice == "ADD":
        addFood()
    elif choice == "PLAN":
        GOAL_CALORIES = int(input("How many calories do you need daily? "))
        plan()
    else:
        exit()