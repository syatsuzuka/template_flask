from flask.ext.script import Manager
from template.app import app

manager = Manager(app)
app.config['DEBUG'] = True

if __name__ == '__main__':
  manager.run()

