from flask import Flask, render_template, request
from costCalculator import totalCost
import os


app = Flask(__name__)


@app.route('/')
def home_page():  # put application's code here
    output = render_template('Home.html')
    return output


@app.route('/quotes', methods=['GET', 'POST'])
def quotes_page():  # put application's code here
    if request.method == 'POST':
        try:
            days = int(request.form['days'])
            cleaning = bool(request.form['cleaning'])
            total = totalCost(days)
            return render_template('Result.html',
                                   days=days,
                                   cleaning=cleaning,
                                   total=total
                                   )
        except Exception:
            pass
    return render_template('Quotes.html')


@app.route('/contact')
def contact_page():  # put application's code here
    output = render_template('Contact.html')
    return output

@app.route('/thegreathall')
def thegreathall_page():  # put application's code here
    output = render_template('The Great Hall.html')
    return output

@app.route('/fairlandpavilion')
def fairlandpavilion_page():  # put application's code here
    output = render_template('Fairland Pavilion.html')
    return output

@app.route('/theottersidecentre')
def theottersidecentre_page():  # put application's code here
    output = render_template('The Otterside Centre.html')
    return output

@app.route('/utsgymnasium')
def utsgymnasium_page():  # put application's code here
    output = render_template('UTS Gymnasium.html')
    return output

if __name__ == '__main__':
    app.run()
