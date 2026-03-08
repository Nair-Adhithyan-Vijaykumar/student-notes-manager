from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm

# List all notes
def note_list(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/note_list.html', {'notes': notes})

# Create a new note
def note_create(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, 'notes/note_form.html', {'form': form, 'title': 'Add Note'})

# Edit an existing note
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, 'notes/note_form.html', {'form': form, 'title': 'Edit Note'})

# Delete a note
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})