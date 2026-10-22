from django.db import DatabaseError, connection
from django.shortcuts import redirect, render

from .models import Note


def index(request):
    error = ""
    if request.method == "POST":
        text = request.POST.get("text", "").strip()
        if text:
            Note.objects.create(text=text[:500])
        return redirect("index")
    try:
        notes = list(Note.objects.all()[:20])
    except DatabaseError as e:  # tables not created yet: run migrate
        notes, error = [], str(e).splitlines()[0]
    return render(request, "notes/index.html", {
        "notes": notes,
        "database": connection.vendor,
        "error": error,
    })
