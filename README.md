# mysql_cloudmanaged_databases

## GCP Setup Process
1. Log into `console.cloud.google.com`.
2. Click on `'Select a project` in the upper left side of the screen and click on `New Project`. Fill in the information and click `Create`.
3. In the navigation menu on the left side of the screen, click on `SQL`.
4. Click on `Create Instance`. Choose `MySQL` and click `Next`, and then `Enable API`.
5. When creating the MySQL instance, create a password for the `root` user. Then change the default configuration options to `MySQL 8`, `Enterprise`, `Sandbox`, `and Shared core 1vCPU/.614gb RAM`. Click `Create` to start the deployment.
6. Once the instance is created, open `MySQL Workbench` and create a new connection. Use the IP address of the instance as the hostname, and use the `root` user and password created earlier. the IP address can be found in the `Overview` tab of the instance. Click `OK` to connect.

## Azure Setup Process
1. Log into `portal.azure.com`.
2. Click on `Create a resource` in the upper left side of the screen and click on `Databases` and then `Azure Database for MySQL`, and `Flexible server`. Fill in the information and click `Create`.
3. Change the default configuraton options to  `Burstable`, `B1s`, `1 vCores`, `1 GiB RAM`, and `20 GiB storage`. Click `Review + create` and then `Create`.
4. Once the instance is created, open `MySQL Workbench` and create a new connection. Use the IP address of the instance as the hostname, and use the `root` user and password created earlier. the IP address can be found in the `Overview` tab of the instance. Change the username from `root` to the server admin name. Click `OK` to connect.

## Python Interaction Challenges
I was able to connect my `python_connection.py` with my GCP database. However, I encountered the following challenges when trying to run `populate.py`:
1. When I tried to run the file, I got the following error:
```
File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\engine\base.py", line 1410, in execute
    meth = statement._execute_on_connection
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'str' object has no attribute '_execute_on_connection'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "c:\Users\16462\mysql_cloudmanaged_databases\populate.py", line 84, in <module>
    insert_fake_data(db_engine)
  File "c:\Users\16462\mysql_cloudmanaged_databases\populate.py", line 43, in insert_fake_data
    connection.execute(f"INSERT INTO providers (first_name, last_name, specialization) VALUES ('{first_name}', '{last_name}', '{specialization}')")
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\engine\base.py", line 1412, in execute
    raise exc.ObjectNotExecutableError(statement) from err
sqlalchemy.exc.ObjectNotExecutableError: Not an executable object: "INSERT INTO providers (first_name, last_name, specialization) VALUES ('Peter', 'Gonzalez', 'Radiology')" 
```

I was able to fix this error by changing the line 
```
connection.execute(f"INSERT INTO providers (first_name, last_name, specialization) VALUES ('{first_name}', '{last_name}', '{specialization}')")

```
to 
```
query = text("INSERT INTO providers (first_name, last_name, specialization) VALUES (:first_name, :last_name, :specialization)")
connection.execute(query, {"first_name": first_name, "last_name": last_name, "specialization": specialization})
```
I had to import `text` from `sqlalchemy.sql` to make this work. I had to do the same thing for the other tables in the database. I think that this error is due to me trying to execute a query string instead of an executable SQL statement using SQLAlchemy.

2. When I tried to run the file again, I got the following error:
```
Traceback (most recent call last):
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\engine\base.py", line 1964, in _exec_single_context
    self.dialect.do_execute(
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\engine\default.py", line 748, in do_execute    
    cursor.execute(statement, parameters)
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
             ^^^^^^^^^^^^^^^^^^
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymysql\connections.py", line 558, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymysql\connections.py", line 822, in _read_query_result  
    result.read()
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymysql\connections.py", line 1200, in read
    first_packet = self.connection._read_packet()
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymysql\connections.py", line 772, in _read_packet        
    packet.raise_for_error()
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymysql\protocol.py", line 221, in raise_for_error        
    err.raise_mysql_exception(self._data)
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymysql\err.py", line 143, in raise_mysql_exception       
    raise errorclass(errno, errval)
pymysql.err.DataError: (1406, "Data too long for column 'phone_number' at row 1")

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\16462\mysql_cloudmanaged_databases\populate.py", line 103, in <module>
    insert_fake_data(db_engine)
  File "C:\Users\16462\mysql_cloudmanaged_databases\populate.py", line 91, in insert_fake_data
    connection.execute(insert_query, {
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\engine\base.py", line 1414, in execute
    return meth(
           ^^^^^
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\sql\elements.py", line 486, in _execute_on_connection
    return connection._execute_clauseelement(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\engine\base.py", line 1638, in _execute_clauseelement
    ret = self._execute_context(
          ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\engine\base.py", line 1842, in _execute_context
    return self._exec_single_context(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\engine\base.py", line 1983, in _exec_single_context
    self._handle_dbapi_exception(
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\engine\base.py", line 2326, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\engine\base.py", line 1964, in _exec_single_context
    self.dialect.do_execute(
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\engine\default.py", line 748, in do_execute    
    cursor.execute(statement, parameters)
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
             ^^^^^^^^^^^^^^^^^^
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymysql\connections.py", line 558, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymysql\connections.py", line 822, in _read_query_result
    result.read()
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymysql\connections.py", line 1200, in read
    first_packet = self.connection._read_packet()
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymysql\connections.py", line 772, in _read_packet        
    packet.raise_for_error()
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymysql\protocol.py", line 221, in raise_for_error        
    err.raise_mysql_exception(self._data)
  File "C:\Users\16462\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymysql\err.py", line 143, in raise_mysql_exception       
    raise errorclass(errno, errval)
sqlalchemy.exc.DataError: (pymysql.err.DataError) (1406, "Data too long for column 'phone_number' at row 1")
[SQL:
                        INSERT INTO demographics (patient_id, first_name, last_name, date_of_birth, address, phone_number, email)
                        VALUES (%(patient_id)s, %(first_name)s, %(last_name)s, %(date_of_birth)s, %(address)s, %(phone_number)s, %(email)s)                    ]
[parameters: {'patient_id': 901, 'first_name': 'Anthony', 'last_name': 'Rhodes', 'date_of_birth': datetime.date(1981, 7, 20), 'address': '532 Christopher Mill Apt. 629, Robinsonberg, IL 27246', 'phone_number': '(422)427-5316x25908', 'email': 'zacharysmith@example.net'}]        
(Background on this error at: https://sqlalche.me/e/20/9h9h)                                                                                                                         
```
This error is due to the phone number being too long for the `phone_number` column in the `demographics` table. I fixed this by changing the line 
```
 phone_number = fake.phone_number()
```
to 
```
phone_number = fake.phone_number()[:12]
```
This will truncate the phone number to 12 characters, which is the maximum length of the `phone_number` column in the `demographics` table.

3. When I ran the file again, it was successful and I did not encounter any errors. However, when I tried retrieve data from one of the tables and store it in a Pandas DataFrame, I got the following output:
```
Providers Data:
Empty DataFrame
Columns: [provider_id, first_name, last_name, specialization]
Index: []
```
This is the same for all the other tables. I think that this is due to `populate.py` not committing the changes to the database. I fixed this by adding `connection.commit()` to the end of the `insert_fake_data` function. 