import pandas as pd

# Example data for a food hub
data = {
    'Item': ['Apples', 'Bananas', 'Carrots', 'Dates'],
    'Category': ['Fruit', 'Fruit', 'Vegetable', 'Fruit'],
    'Price_per_kg': [3.5, 2.0, 1.8, 5.0],
    'Stock_kg': [100, 150, 200, 50]
}

# Create a DataFrame
food_hub_df = pd.DataFrame(data)

# Display the DataFrame
print(food_hub_df)
