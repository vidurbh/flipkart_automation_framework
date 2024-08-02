rem pytest -v -s -m "sanity" --browser Chrome --html=Reports/report.html 
pytest -v -s .\TestCases\test_selectProduct.py --browser Chrome --html=Reports/report.html
rem pytest -v -s .\TestCases\test_navigate.py --browser Chrome --html=Reports/report.html 
@REM pytest -v -s .\TestCases\test_productsearch.py --browser Chrome --html=Reports/report.html