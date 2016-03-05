create virtual environment as follows : virtualenv --no-site-packages venv

open virtualenv by typing: source venv/bin/activate
to deactivated venv, just type in deactivate


You should install pakages inside of the activated venv -- example 'pip install flask'


unix command to make a new file:  'touch app.py' makes the app.py file


to get into sql from shell: 'sqlite3 sample.db'
example sql commands
http://zetcode.com/db/sqlite/ --- sqlite tutorial
drop table posts
create table and then INSERT INTO Cars2 SELECT * FROM Cars;
DELETE FROM Cars2 WHERE Id=1;
UPDATE Cars SET Name='Skoda Octavia' WHERE Id=
SELECT * FROM Cars LIMIT 4
SELECT Name, Price FROM Cars ORDER BY Price DESC;
SELECT * FROM Orders WHERE Id=6;
SELECT * FROM Orders WHERE Customer="Smith";
SELECT * FROM Orders WHERE Customer LIKE 'B%';
SELECT DISTINCT Customer FROM Orders WHERE Customer LIKE 'B%';
SELECT sum(OrderPrice) AS Total, Customer FROM Orders GROUP BY Customer HAVING sum(OrderPrice)>1000;
SELECT count(Customer) AS '# of orders'  FROM Orders;
SELECT count(DISTINCT Customer) AS '# of customers' FROM Orders;
SELECT date('now');
SELECT datetime('now')
SELECT date('now', '2 months'); -- date becomes two months from today
SELECT date('now', 'start of year');
.width 100
.headers on
.mode column
select count(nitrite_txt) from patients_total where nitrite_txt like 'P%';
select * from patients_total where nitrite_txt like 'P%';

to run the unittests --- 'python test.py -v'


when setting up heroku -- commands i used were:
heroku login
pip install gunicorn
bind gunicorn to localhost with: gunicorn -b 127.0.0.1:4000 app:app
so now if go to localhost:4000, the app shows up
make a requirements file with dependencies -- pip freeze > requirements.txt (pip freeze on own shows dependencies)
create .gitignore file --- so dont upload certain files --- venv, .pyc files, .db files

now lets add to git repository wiht:
git init
git add .
git commit -m "init"   (our initial commit is titled 'init' by convention)

now lets create our heroku space 
'heroku create flask-intro-karambir'
we can open app with: 'heroku open'
nothing appears yet -- we need to push our app on git to heroku as follows: 'git push heroku master'
assign 1 dyno to app:  'heroku ps:scale web=1'
to check our web process:  heroku ps   
to check heroku commands possible, type this in terminal: heroku


steps to add changes to git and then push to heroku
pip freeze > requirements.txt
git add .
git commit -am "try/except block added"
git push heroku master

to run our unittests on heroku: 'heroku run python test.py -v'

to check the things our repository is connected to: git remote -v

install sqlalchemy -- pip install Flask-SQLAlchemy

to create database: python db_create.py

to query database from the python shell:
from models import BlogPost
posts = BlogPost.query.all()  (like select all from posts)
posts

to insert into databse via sqlalchemy
db.session.add(BlogPost("Good", "I\'m good."))
to query: db.session.query(BlogPost).all()	

set up environment variables in our local environment(development vs production for our config file)
to set up environment variable APP-SETTINGs to a particular value:
export APP_SETTINGS="config.DevelopmentConfig"
to check our app config settings in python shell:
from app import app
print app.config
set our database environment variable:
export DATABASE_URL="sqlite:///posts.db"


To set the heroku environment variable:
heroku config:set APP_SETTINGS=config.ProductionConfig --remote heroku

to generate a secret key:
import os
os.urandom(24)


create postgres database on heroku:
heroku addons:create heroku-postgresql:hobby-dev    (creates hobby-dev level database)
to set it as the database for our project (our db is called postgresql-cubic-22773 ):
heroku pg:promote postgresql-cubic-22773


to confirm that postgres database exists on heroku:
heroku config | grep HEROKU_POSTGRESQL

to install python bindings for postgres:
pip install psycopg2


To make a db on flask, lets run our db_create script on flask:
heroku run python db_create.py
to add data to heroku postgres from python shell
heroku run python
from app import db
from models import BlogPost
db.session.add(BlogPost("Hi", "This is my first post on heroku."))
db.session.commit()

our database environment variable is still pointing to "sqlite:///posts.db"
we change it with:
export DATABASE_URL="postgresql://localhost/discover_flask_dev"   (name of db is discover_flask_dev)

now to create our database:
psql 
CREATE DATABASE discover_flask_dev;
then we run our db_create.py file to make the posts table:
python db_create.py


what we did in lesson 14
setup postgres
change the environment variable
setup the database -- db_create.py 

now lets set up database migrations (way to add data without dropping the whole database):
pip install flask-migrate
this also installs flask-script -- which makes it easy to run scripts against flask applicaiton

to initialize our migrations (create migrations folder that stores config files and future migration scripts)
python manage.py db init
to create the python migration script:
python manage.py db migrate 
to apply the migration:
python manage.py db upgrade

export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/9.5/bin/


lets connect to database and add data to it
psql
'\c discover_flask_dev'  connnects to the database
'\d' shows the tables in the db 
'\d posts' to look closer at posts table 
'select * from Posts'  to see entries in posts table
INSERT INTO users VALUES(1, 'admin', 'ad@min.com', 'admin');  ---- insert a user into admin users table
UPDATE posts SET author_id = 1;   ---- update the posts table with the author_id