from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Page


def home(request):
    pages = Page.objects.exclude(content = "")
    return render(request, "note/home.html", {"pages": pages})

def create_page(request):
    page = Page.objects.create()
    return redirect("page", page_uuid = page.uuid)

def page(request, page_uuid):
    page = get_object_or_404(Page, uuid=page_uuid)
    if request.method == 'POST':
        page.title = request.POST.get('title', page.title)
        page.content = request.POST.get('content', page.content)
        if page.title.strip() or page.content.strip():
            page.title = page.title
            page.content = page.content
            page.save()
        else:
            page.delete()
            return redirect("home")
        return redirect("home")
    return render(request, "note/page.html", {"page": page})

def delete_page(request, page_uuid):
    page = get_object_or_404(Page, uuid=page_uuid)
    page.delete()
    return redirect("home")
