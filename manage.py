
# Script for building the DB.

# To build the DB from scratch, first delete the migrations folder, then run:
# $ python manage.py db init

# To create a migration script after updating the schema:
# $ python manage.py db migrate

# To apply this update:
# $ python manage.py db upgrade



from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

from app import app, db

app.config.from_object(os.environ['APP_SETTINGS'])
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()