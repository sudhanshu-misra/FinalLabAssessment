\# Flask Notes API



A simple \*\*Flask-based Notes API\*\* designed to run inside Docker.  

This project demonstrates a basic Python web service with \*\*CRUD operations\*\*, \*\*JSON responses\*\*, and \*\*in-memory storage\*\*.



---



\## Features



\- \*\*Create, Read, Update, Delete (CRUD)\*\* operations for notes  

\- \*\*JSON-based API responses\*\*  

\- \*\*UUID-based IDs\*\* for each note  

\- \*\*Health and logging\*\* support  

\- Ready to run in \*\*Docker\*\* with customizable `PORT`  



---



\## Endpoints



| Method | Endpoint           | Description                     |

|--------|------------------|---------------------------------|

| GET    | `/`               | Welcome message \& total notes   |

| GET    | `/notes`          | Get all notes                   |

| GET    | `/notes/<id>`     | Get a note by ID                |

| POST   | `/notes`          | Create a new note (`title`, `content` in JSON body) |

| PUT    | `/notes/<id>`     | Update a note (`title` and/or `content` in JSON body) |

| DELETE | `/notes/<id>`     | Delete a note by ID             |



---



\## Installation



1\. Clone the repository:



```bash

git clone https://github.com/sudhanshu-misra/flask-notes-api.git

cd flask-notes-api



