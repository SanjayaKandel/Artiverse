from django.shortcuts import render, redirect,get_object_or_404
from django.core.paginator import Paginator
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login,logout
from Artworks .models import Artwork
from .models import Artist
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'Authentication/register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('user_dashboard')
            elif user is not None and user.is_user:
                login(request, user)
                return redirect('index')
            elif user is not None and user.is_artist:
                login(request, user)
                return redirect('artist')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'Authentication/login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'Authentication/admin.html')


def user(request):
    return render(request,'Home/index.html')

@login_required
def artist(request):
    creator = request.user

    try:
        artist = Artist.objects.get(user=creator)
    except Artist.DoesNotExist:
        return redirect('create_artist_profile')

    arts = Artwork.objects.filter(artist=creator)
    paginator = Paginator(arts, 5) 
    page_number = request.GET.get('page')
    paginated_arts = paginator.get_page(page_number)
    
    context = {
        'artist': artist,
        'arts': paginated_arts,
    }
    return render(request, 'Artists/artist_dashboard.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('login_view')
