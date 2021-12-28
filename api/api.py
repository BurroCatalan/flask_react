from app import app, db
from app.models import User, ProjectRequest, ProjectType, Status, StatusNet, Customer

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

#@app.shell_context_processor
#def make_shell_context():
#    return {'db': db, 'User': User}
