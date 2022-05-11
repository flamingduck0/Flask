from flask import Flask, render_template, request

def totalCost(days, mics, rooms, roomtime, courts, courttime, bbqtime, spots,tech):
    TotalGreathall = days * 1750
    if request.form.get('cleaning'):
        TotalGreathall += 240
    TotalGreathall += (tech * 35)
    if request.form.get('kitchen'):
        TotalGreathall += 500
    TotalGreathall += (mics * 35)
    if request.form.get('av'):
        TotalGreathall += rooms * 15 * roomtime
    else:
        TotalGreathall += rooms * 10 * roomtime
    TotalGreathall += courts * 20 * courttime
    if request.form.get('bbq'):
        TotalGreathall += 25 * bbqtime
    TotalGreathall += (days*1000 + spots*10)

    return TotalGreathall