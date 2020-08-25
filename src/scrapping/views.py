from django.shortcuts import render
import  datetime

def home(requesr):
	date = datetime.datetime.now().date()
	name = 'Dave'
	cont = {'date': date, 'name': name}
	return render(requesr, 'home.html', cont)