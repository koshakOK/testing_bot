from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import server, db

migrate = Migrate(server, db, compare_type=True)

manager = Manager(server)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()