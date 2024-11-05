from django.shortcuts import render

def home(request):
    return render(request, 'polls/home.html')  # Create a home.html template in your polls/templates/polls/ directory
