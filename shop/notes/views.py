from django.shortcuts import render, redirect
from notes.forms import AddNoteForm
from notes.models import Note


def notes(request):
    notes = Note.objects.all()
    return render(request, "notes.html", {"notes": notes})


def add_notes(request):
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            Note.objects.create(
                title=form.cleaned_data["title"],
                comment=form.cleaned_data["comment"],
            )
            return redirect("/notes/")
    else:
        form = AddNoteForm()
    return render(request, "add_notes.html", {"form": form})
