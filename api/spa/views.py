from django.shortcuts import render

def spa_home(request):
    return render(request, 'home.html')
