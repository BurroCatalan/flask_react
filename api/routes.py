import time
from app import app

@app.route('/')
@app.route('/time')
def index():
	return {'time': time.time()}
