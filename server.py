# coding=utf-8
from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand

from project import create_app

manager = Manager(create_app)

# Add Flask-Migrate commands under `db` prefix, for example:
# $ python manage.py db init
# $ python manage.py db migrate
manager.add_command('db', MigrateCommand)


from project import create_app

app = create_app()

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
