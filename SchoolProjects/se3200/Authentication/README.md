# Personal Task List

## Resource

**Tasks**

Attributes:

* task (string)
* due date (integer)
* priority (integer)
* progress (integer)
* reference (string)

**Users**

Attributes:

* email (string)
* first name (string)
* last name (string)
* password (string)

## Schema

```sql
CREATE TABLE tasks (
id INTEGER PRIMARY KEY,
task TEXT,
dueDate INTEGER,
priority INTEGER,
progress INTEGER
reference TEXT);
```

```sql
CREATE TABLE users
(id INTEGER PRIMARY KEY, 
email STRING, 
firstName STRING, 
lastName STRING, 
password STRING);
```

## Password Hashing

Encryption is achieved by using bcrypt.

## REST Endpoints

Name                           | Method | Path
-------------------------------|--------|------------------
Retrieve all tasks             | GET    | /tasks
Retrieve one task              | GET    | /tasks/*\<id\>*
Create task                    | POST   | /tasks
Update task                    | PUT    | /tasks/*\<id\>*
Delete task                    | DELETE | /tasks/*\<id\>*
Create User                    | POST   | /users
Authenticate User              | POST   | /sessions
<!-- Admin use Get All Users        | GET    | /adminusers
Admin use Delete User          | DELETE | /adminusers/*\<id\>* -->
