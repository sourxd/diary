from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from users.models import Notes


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
        'title': 'Список заметок',
        'notes': Notes.objects.filter(name=request.user),
    }
    return render(request, 'grades/notes.html', context)


@login_required
def add_note(request):
    if request.method == 'POST':
        new_notes = Notes(text=request.POST['note-text'], name=request.user)
        new_notes.save()
        return HttpResponseRedirect(reverse('notes'))
    context = {
        'title': 'Добавление заметки',
    }
    return render(request, 'grades/add_note.html', context)


def remove_note(request, note_id):
    note = Notes.objects.get(id=note_id, name=request.user)
    note.delete()
    return HttpResponseRedirect(reverse('notes'))