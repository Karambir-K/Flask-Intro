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
