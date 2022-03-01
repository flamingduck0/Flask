from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def landing_page():  # put application's code here
    output = render_template('Home.html')
    return output

@app.route('/test')
def Test_page():  # put application's code here
    output = render_template('Test.html')
    return output

@app.route('/timetable')
def timetable_page():  # put application's code here
    output = render_template('Timetable.html')
    return output

if __name__ == '__main__':
    app.run()