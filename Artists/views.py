from django.shortcuts import render, redirect
from Authentication. models import Artist
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import ArtistForm
from django.db import IntegrityError
# Create your views here.
@login_required
def artist_artwork(request):
    return HttpResponse('hi')

@login_required
def artist_profile(request):
    artist = Artist.objects.get(user=request.user)
    return render(request, 'Artists/artist_profile.html', {'artist': artist})


@login_required
def create_artist_profile(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            if hasattr(user, 'artist'):
                return HttpResponse("Profile already exists")
            try:
                artist = form.save(commit=False)
                artist.user = user
                artist.save()
                return redirect('artist_profile')
            except IntegrityError:
                
                return render(request, 'Artists/create_artist.html', {'form': form, 'error': 'Artist profile could not be created due to a database error.'})
    else:
        form = ArtistForm()
    return render(request, 'Artists/create_artist.html', {'form': form})
@login_required
def update_artist_profile(request):
    user = request.user
    artist_profile, created = Artist.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist_profile)
        if form.is_valid():
            form.save()
            return redirect('artist_profile')  # Redirect to a success page or profile page
    else:
        form = ArtistForm(instance=artist_profile)

    return render(request, 'Artists/update_artist_profile.html', {'form': form})
