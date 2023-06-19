# Bank Data Analysis
The repository includes all the Python code for analyzing a bank dataset stored in a CSV file(Bank.csv). 
The code performs the following tasks:

* Provides information or reads the contents of the bank data set from a CSV file.
* It prints the headers of the data set from the CSV file.
* Provides the number or count of the people married, single and divorced.
* Prepares a histogram for different age groups in the data set

## About The Data Set
The dataset used for analysis is stored in the file bank.csv, located at Data. 
It is important to note that the correct file path should be provided when executing the code.

## Code Files
lab1.ipynb: Contains the Python code for analyzing the bank dataset.

## Usage
Make sure that Visual Studio Code is installed in your system.
Clone this repository or download the lab1.ipynb file.
Modify the file path in the code to match the location of your bank.csv file.
Open a terminal or command prompt and navigate to the directory where the lab1.ipynb file is located.
Run the following command to execute the code:
bash python lab1.ipynb

## Functions used
* Header() displays the headers of the dataset. It reads the first line of the dataset and splits it into individual headers.
* Count()function counts the number of married, single, and divorced people in the dataset
* create_age_histogram This function prepares a histogram for the age distribution in the dataset. It extracts the age of each customer from the dataset and groups them into age classes.

## Conclusion
The objective of this lab program was to handle a csv file that consisted of the data of bank users. 
The program enabled us to create menu driven program with the help of certain user defined functions.
