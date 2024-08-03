:: Create and activate virtual environment
python -m venv venv
call venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt

:: Run tests
@REM pytest -v -s -m "sanity" --browser Chrome --html=Reports/report.html 
@REM pytest -v -s .\TestCases\test_selectProduct.py --browser Chrome --html=Reports/report.html
@REM pytest -v -s .\TestCases\test_navigate.py --browser Chrome --html=Reports/report.html 
@REM pytest -v -s .\TestCases\test_productsearch.py --browser Chrome --html=Reports/report.html
