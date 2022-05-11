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
            mics = int(request.form['mics'])
            rooms = int(request.form['rooms'])
            roomtime = int(request.form['roomtime'])
            courts = int(request.form['courts'])
            courttime = int(request.form['courttime'])
            spots = int(request.form['spots'])
            tech = int(request.form['tech'])
            bbqtime = int(request.form['bbqtime'])


            total = totalCost(days, mics, rooms, roomtime, courts, courttime, bbqtime, spots, tech)
            return render_template('Result.html',
                                   days=days,
                                   mics=mics,
                                   rooms=rooms,
                                   roomtime=roomtime,
                                   courts=courts,
                                   courttime=courttime,
                                   spots=spots,
                                   tech=tech,
                                   bbqtime=bbqtime,
                                   total=total,
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
