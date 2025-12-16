#imports Flask to create the web application and render_template to load an HTML file.
from flask import Flask, render_template
#imports the datetime module, which is used to get the current day and time.
from datetime import datetime

#creates an instance of the Flask application.
app = Flask(__name__)

#defines a route named /api. When a user visits this URL, the home() function is executed.
@app.route('/api')
def home():

    #gets the current day (for example, Monday, Tuesday).
    day_of_week=datetime.today().strftime('%A')

    #gets the current time in hours, minutes, and seconds
    current_time=datetime.now().strftime('%H:%M:%S')

    #loads the index.html file and sends the values of day_of_week and current_time to the HTML template so they can be displayed using {{ }}.
    return render_template ('index.html',day_of_week=day_of_week,current_time=current_time)

#starts the Flask development server.
#debug=True helps during development by automatically reloading the app and showing errors.
if __name__ == '__main__':

 app.run(debug=True)