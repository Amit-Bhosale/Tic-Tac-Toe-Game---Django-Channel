from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.


def home(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        option = request.POST.get('option')
        room_code = request.POST.get('room_code')

        if option == '1':
            game = Game.objects.filter(room_code=room_code).first()
            print(game)
            if game is None:
                messages.success(request, "Room Code Note Found")
                return redirect('/')
            if game.is_over == True:
                messages.success(request, "Game Over")
                return redirect('/')
            game.game_apponent = user
            game.save()
        else:
            game = Game(game_creator=user, room_code=room_code)
            game.save()
            return redirect('/play/'+room_code+'?username='+user)
    return render(request, 'home.html')


def play(request, room_code):
    username = request.GET.get('username')
    context = {'room_code': room_code, 'username': username}
    return render(request, 'play.html',context)
