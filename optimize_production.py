from pulp import LpMaximize, LpProblem, LpVariable, value, LpInteger
from typing import Tuple


def optimize_production() -> Tuple[int, int, int]:
    # Create the optimization model
    model = LpProblem("Maximize_Production", LpMaximize)

    lemonade = LpVariable("Lemonade", lowBound=0, cat=LpInteger)
    fruit_juice = LpVariable("FruitJuice", lowBound=0, cat=LpInteger)

    # Objective: maximize total number of products
    model += lemonade + fruit_juice, "Total_Products"

    # Constraints
    model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
    model += 1 * lemonade <= 50, "Sugar_Constraint"
    model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
    model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"


    model.solve()

    # Extract the results
    max_lemonade = int(lemonade.varValue)
    max_fruit_juice = int(fruit_juice.varValue)
    total_products = int(value(model.objective))

    return max_lemonade, max_fruit_juice, total_products


if __name__ == "__main__":
    lemonade, fruit_juice, total = optimize_production()
    print(f"Maximum lemonade units: {lemonade}")
    print(f"Maximum fruit juice units: {fruit_juice}")
    print(f"Total units produced: {total}")
