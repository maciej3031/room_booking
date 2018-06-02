# -*- coding: utf-8 -*-

from sqlalchemy.orm import Session

from booking import Base, db

Uzytkownicy = Base.classes.Uzytkownicy
Sale = Base.classes.Sale
Rezerwacje = Base.classes.Rezerwacje
Dzialy = Base.classes.Dzialy
Uslugi = Base.classes.Uslugi
RezerwacjeSzczegoly = Base.classes.RezerwacjeSzczegoly
SprzetNieruchomyWSali = Base.classes.SprzetNieruchomyWSali
GrupyDostepu = Base.classes.GrupyDostepu
Rozliczenia = Base.classes.Rozliczenia
UzytkownicyGrupyDostepu = Base.classes.UzytkownicyGrupyDostepu

session = Session(db.engine)
