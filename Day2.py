mealCost = float(raw_input())
tipPercent = int(raw_input())
taxPcent = int(raw_input())

tip= (mealCost* tipPercent)/100.0
tax = (mealCost* taxPcent)/100.0

totalCost = mealCost + tip + tax

print("The total meal cost is " + str(int(round(totalCost))) + " dollars.")