## Indian Banks API Server

This is an API Server which can be used to utlize an DB containing the details of Indian Banks.

#### Dependencies

- Python >=3.6

- psycopg2

- Fastapi

- postgresql

- uvicorn

#### To use

- cd to the project dir.

- Make sure the DB is online.

- ```bash
  uvicorn main:app --reload
  ```

- go to the o/p url in browser ( usually `http://127.0.0.1:8000`)    

- to use it directly through browser :- go to /docs.

- to test :- 

```bash
 python3 test.py
```

#### Steps Followed :-

- A psql DB was created by sourcing the .sql provided in [repo](https://github.com/Amanskywalker/indian_banks). The DB is named `banks` 

- A connection is made from python to the DB using psycopg2 every time get_db_conn() is called in `db.py`.

- In `main.py` fast api is initialized and 5 endpoints are created to .
  
  - get the bank list
  
  - get the branch detail using ifsc code
  
  - search for a bank
  
  - get the list of branches of that bank ( using the view)

- `test.py` contains the test cases for testing our API.



**Time Taken** to complete this assignment :-  1.5hrs + ( 3 hrs  as I had to learn Fastapi )


