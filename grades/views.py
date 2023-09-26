from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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

@login_required
def notes(request):
    context = {
        'title': 'Список заметок'
    }
    return render(request, 'grades/notes.html', context)

@login_required
def add_note(request):
    context = {
        'title': 'Добавление заметки'
    }
    return render(request, 'grades/add_note.html', context)
