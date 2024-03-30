# Importing necessary libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('data.csv')

# Extracting features and target variablee
X = data['Temperature'].values.reshape(-1, 1)  # Features (temperature)
y = data['Ice Cream Profits'].values  # Target variable (profits)

# Creating a linear regression model
model = LinearRegression()

# Training the model
model.fit(X, y)

# Making predictions
new_temperature = 45  # Example temperature for prediction
predicted_profit = model.predict([[new_temperature]])
print("Predicted profit at temperature {}°C: ${:.2f}".format(
    new_temperature, predicted_profit[0]))

# Visualizing the data and regression line
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.title('Ice Cream Profits vs Temperature')
plt.xlabel('Temperature (°C)')
plt.ylabel('Ice Cream Profits ($)')
plt.show()
