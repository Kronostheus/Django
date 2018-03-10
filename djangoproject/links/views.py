from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Link, Vote, Comment

from .forms import LinkForm, CommentForm, VoteForm

# Create your views here.

# Home Page
def index(request):

    # Get all Links and Order them (descending by votes)
    linkList = Link.objects.all().order_by('-vote')

    # Pagination - Alter second argument to change number of links per page
    paginator = Paginator(linkList, 10)

    # Separating Links based on pagination arguments
    page = request.GET.get('page')
    links = paginator.get_page(page)

    context = {
        'links': links
    }

    return render(request, 'links/index.html', context)

def link_delete(request):
    link = Link.objects.get(pk)
    link.delete()
 
# Register - Sign Up
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            # Get username
            username = form.cleaned_data.get('username')

            # Get password
            raw_password = form.cleaned_data.get('password1')

            # Log In
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            # Redirect to home page
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Reply to Comment
def reply_comment(request, pk):

    # Get parent link
    parent = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            # Do not commit save (variables still need assignment)
            comment = form.save(commit=False)

            # Reply's parent comment
            comment.parent = parent

            # Associated link
            comment.link = parent.link

            # Commenter
            comment.submitter = request.user

            # Commit
            comment.save()
            return redirect('link_detail', pk=parent.link.pk)
    else:
        form = CommentForm()
    return render(request, 'links/link_comment.html', {'form': form})

# Comment on Link (top level)
def link_comment(request, pk):

    # Get associated link
    link = get_object_or_404(Link, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            # Do not commit save (variables still need assignment)
            comment = form.save(commit=False)

            # Associated link
            comment.link = link

            # Commenter
            comment.submitter = request.user

            # Commit
            comment.save()
            return redirect('link_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'links/link_comment.html', {'form': form})

# Create a link
def link_create(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)

        if form.is_valid():
            # Do not commit save (variables still need assignment)
            link = form.save(commit=False)

            # Default Updoots = 0
            link.rank_score = 0

            # Submitter
            link.submitter = request.user

            # Commit
            link.save()
            return redirect('link_detail', pk=link.id)
    else:
        form = LinkForm()
    return render(request, 'links/link_form.html', {'form': form})

# Handles the Updoots
def updoot(request):

    # Get form
    form = VoteForm(request.POST)

    # Get link
    link = get_object_or_404(Link, pk=form.data["link"])

    # Get voter
    user = request.user

    # How many times has this user updooted this link
    has_voted = Vote.objects.filter(voter=user, link=link)

    # Only updoot if user never updooted before
    if has_voted.count() == 0:
        # Has not voted this link -> allow updoot
        Vote.objects.create(voter=user, link=link)
    else:
        # User has changed his mind (had already voted) -> delete updoot
        has_voted[0].delete()
    return redirect('home')

# Link Page
class LinkDetailView(DetailView):
    model = Link

# Edit Page
class LinkUpdateView(UpdateView):
    model = Link
    # Use same form as Link creation 
    form_class = LinkForm

# Delete Page
class LinkDeleteView(DeleteView):
    model = Link
    # Return to home page after deletion successful
    success_url = reverse_lazy('home')