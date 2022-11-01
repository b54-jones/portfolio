class CalorieCalculator:
    def __init__(self, height, weight, age, temperature):
        self.height = height
        self.weight = weight
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height + 15 - self.temperature * 10
        return result