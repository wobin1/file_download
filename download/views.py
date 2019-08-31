from django.shortcuts import render, redirect
from .models import Photo
from .models import Book, Music, Video
from .forms import BookModelForm

def index(request):
    photo = Photo.objects.all()
    context = {
        'photo': photo
    }
    return render(request, 'download/index.html', context)

def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'download/book_list.html', context)

def music(request):
    music = Music.objects.all()
    context = {
        'music': music
    }
    return render(request, 'download/music.html', context)

def book_upload(request):
    form = BookModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'download/book_upload.html', context)

def video(request):
    video = Video.objects.all()
    context = {
        'video': video
    }
    return render(request, 'download/video.html', context)