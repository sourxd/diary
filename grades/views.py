from django.shortcuts import render


def index(request):
    context = {
        'title': 'School Diary'
    }
    return render(request, 'grades/index.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'grades/contacts.html', context)


