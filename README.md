# Frontend Flipkart Framework

# Description
This project includes a very basic hybrid framework, have used pytest for running the tests. Code is written in Python

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)


## Installation
To get started with Awesome Project, clone the repository and install the dependencies:

git clone https://github.com/username/flipkart_automation_framework.git
cd flipkart

For running the testcases, Few sample Testcases are added in the Testcases folder. FOllowing commands can be used for running it
pytest -v -s -m "sanity" --browser Chrome --html=Reports/report.html 
pytest -v -s .\TestCases\test_selectProduct.py --browser Chrome --html=Reports/report.html
pytest -v -s .\TestCases\test_navigate.py --browser Chrome --html=Reports/report.html 
pytest -v -s .\TestCases\test_productsearch.py --browser Chrome --html=Reports/report.html

Incase you want to run it through a batch file, you can uncomment the desired command and run it.


