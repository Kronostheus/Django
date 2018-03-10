from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Link, Vote, Comment

from .forms import LinkForm, CommentForm

# Create your views here.
def index(request):
    linkList = Link.objects.all()
    paginator = Paginator(linkList, 10)

    page = request.GET.get('page')
    links = paginator.get_page(page)

    context = {
        'links': links
    }

    return render(request, 'links/index.html', context)

def link_delete(request):
    link = Link.objects.get(pk)
    link.delete()
 

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def reply_comment(request, pk):
    parent = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.parent = parent
            comment.link = parent.link
            comment.submitter = request.user
            comment.save()
            return redirect('link_detail', pk=parent.link.pk)
    else:
        form = CommentForm()
    return render(request, 'links/link_comment.html', {'form': form})


def link_comment(request, pk):
    link = get_object_or_404(Link, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.link = link
            comment.submitter = request.user
            comment.save()
            return redirect('link_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'links/link_comment.html', {'form': form})


def link_create(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.rank_score = 0.0
            link.submitter = request.user
            link.save()
            return redirect('link_detail', pk=link.id)
    else:
        form = LinkForm()
    return render(request, 'links/link_form.html', {'form': form})

class LinkDetailView(DetailView):
    model = Link

class LinkUpdateView(UpdateView):
    model = Link
    form_class = LinkForm

class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy('home')