# Currency Converter

A simple currency converter application built with Python and Tkinter. This program allows users to convert amounts between two currencies (EUR and USD) using a user-friendly graphical interface.

Features
-Convert between EUR and USD with predefined exchange rates.
-Input validation to handle invalid entries (displays "Error" if the input is not a number).
-Clean and intuitive GUI built with Tkinter.
-Easy-to-use dropdown menus for selecting source and destination currencies.

Requirements
-Python 3.x
-Tkinter (included with standard Python installations)
-No additional libraries required

How to Run
-Download the files from this repository.
-Ensure Python 3.x is installed on your computer.

Run the script with:

-python currency_converter.py
-Enter an amount, select the source and destination currencies, and click "Convertir" to see the result.

File Structure
-currency_converter.py: Main Python script containing the application code.
-screenshot.png (optional): Screenshot of the application in action.

Screenshot
-Note: Replace screenshot.png with the actual filename of your screenshot after uploading it to the repository.

Usage
-Select currencies: Choose the source and destination currencies (EUR or USD) from the dropdown menus.
-Enter amount: Type the amount to convert in the "Cantidad a convertir" field.
-Convert: Click the "Convertir" button to display the converted amount in the "Resultado" field.
-Error handling: If you enter an invalid amount (e.g., letters), the result will show "Error".

Notes
-The exchange rates (1 EUR = 1.1 USD, 1 USD = 0.9 EUR) are hardcoded for simplicity. In a production environment, you could integrate an API for real-time rates.
-This is a basic version designed for demonstration purposes, but it can be extended with more currencies or features.

License
-MIT License
