# -*- coding: utf-8 -*-
from wtforms import Form, IntegerField, StringField, DateTimeField, SelectField, SelectMultipleField

from booking.models import Sale, Uslugi, session


# TODO: Create "better" field for start_date and end_date (Maybe some JS or CSS?)
class AddReservationForm(Form):
    user_id = IntegerField('User ID')
    room = SelectField('Room', choices=[(i.IdSali, i.Nazwa) for i in session.query(Sale)])
    services = SelectMultipleField('Services', choices=[(i.IdUslugi, i.Nazwa) for i in session.query(Uslugi)])
    start_date = DateTimeField('Start Date')
    end_date = DateTimeField('End Date')
    description = StringField('Description')
