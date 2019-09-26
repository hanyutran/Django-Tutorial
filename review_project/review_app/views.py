from django.shortcuts import render

def index(request):
    my_dict = {'insert_me':'Welcome to my Project!'}
    return render(request, 'review_app/index.html', context=my_dict)
