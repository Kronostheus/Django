from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Link, Vote

from .forms import LinkForm

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

class LinkCreateView(CreateView):
    model = Link
    form_class = LinkForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.rank_score = 0.0
        f.submitter = self.request.user
        f.save()
        return super(LinkCreateView, self).form_valid(form)

class LinkDetailView(DetailView):
    model = Link

class LinkUpdateView(UpdateView):
    model = Link
    form_class = LinkForm

class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy('home')