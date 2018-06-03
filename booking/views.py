# -*- coding: utf-8 -*-

from datetime import datetime

from flask import render_template, flash, redirect, url_for, request

from booking import app
from booking.forms import AddReservationForm
from booking.models import Rezerwacje, Sale, Uzytkownicy, RezerwacjeSzczegoly, session

# TODO: Add change_reservation, fix add_reservation


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/reservations/', methods=['GET'])
def reservations_list():
    if request.method == 'GET':
        reservations = session.query(Rezerwacje).order_by(Rezerwacje.DataRezerwacji.desc()).all()
        return render_template('reservations_list.html', reservations=reservations)


@app.route('/reservations/<pk>/', methods=['GET'])
def reservation_details(pk):
    if request.method == 'GET':
        reservation = session.query(Rezerwacje).filter_by(IdRezerwacji=pk).first()
        if reservation is None:
            flash("No reservation with given ID.", category='error')
            return redirect(url_for("reservations_list"))
        return render_template('reservation_details.html', reservation=reservation)


@app.route('/change_reservation/', methods=['POST'])
def change_reservation():
    pass


# TODO: add validation for not working and already reserved hours. Add possibility to set number of services.
@app.route('/add_reservation/', methods=['GET', 'POST'])
def add_reservation():
    form = AddReservationForm(request.form)
    if request.method == 'POST':
        session.query(Rezerwacje.IdRezerwacji).all()
        # It's stupid but I have no idea why it doesn't work without IdRezerwacji. It should work just like for RezerwacjeSzczegoly.
        max_id = session.query(Rezerwacje).order_by(Rezerwacje.IdRezerwacji.desc()).first().IdRezerwacji
        reservation = Rezerwacje(
            DataRezerwacji=datetime.now(),
            DataRozpoczecia=form.start_date.data,
            DataZakonczenia=form.end_date.data,
            OpisRezerwacji=form.description.data,
            IdUzytkownika=form.user_id.data,
            IdSali=int(form.room.data),
            IdRezerwacji=max_id+1,
        )
        session.flush()
        session.add(reservation)
        for service_id in form.services.data:
            detail = RezerwacjeSzczegoly(Ilosc=1,
                                         IdRezerwacji=reservation.IdRezerwacji,
                                         IdUslugi=int(service_id))
            session.add(detail)
            session.commit()
        flash('New reservation added.')
        return redirect(url_for('index'))
    return render_template('add_reservation.html', form=form)


@app.route('/rooms/', methods=['GET'])
def rooms_list():
    if request.method == 'GET':
        rooms = session.query(Sale).order_by(Sale.Nazwa.asc()).all()
        return render_template('rooms_list.html', rooms=rooms)


@app.route('/rooms/<pk>/', methods=['GET'])
def room_details(pk):
    if request.method == 'GET':
        room = session.query(Sale).filter_by(IdSali=pk).first()
        if room is None:
            flash("No room with given ID.", category='error')
            return redirect(url_for("rooms_list"))
        return render_template('room_details.html', room=room)


@app.route('/users/', methods=['GET'])
def users_list():
    if request.method == 'GET':
        users = session.query(Uzytkownicy).all()
        return render_template('users_list.html', users=users)
