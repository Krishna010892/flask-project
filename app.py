from flask import Flask

app =  Flask(__name__)

@app.route('/')

def home():

    return 'Welcome to the First page.'

@app.route('/second')
def second():

    #hi

    return 'Welcome to second page'

if __name__ == '__main__':

    app.run(debug=True)