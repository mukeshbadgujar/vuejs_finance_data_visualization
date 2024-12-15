# Steps for Setup Djnago Projecr
1. Create a virtual environment by running the following command:
```bash
python3 -m venv venv
```
2. Activate the virtual environment by running the following command:
```bash
source venv/bin/activate
```
3. Install the required packages by running the following command:
```bash
pip install -r requirements.txt
```
4. Run the following command to start the Django server:
```bash
python manage.py runserver
```


## To load CSV in database
1. Run the following command to load the CSV file in the database:
2. add your csv file in the backend(root) folder
3. make sure csv column name should be same as in the file
```bash
python backend/optimized_import_invoices.py
```



