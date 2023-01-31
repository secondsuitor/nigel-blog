from nigel import app

@app.route('/')
@app.route('/index')
def index():
    return "hello world"

@app.route('/test')
def tester():
    return "hello tester"