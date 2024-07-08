from django.shortcuts import render, get_object_or_404, redirect
from .models import Artwork, Wishlist
from Authentication. models import Artist
from . forms import ArtworkForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.http import JsonResponse
# Create your views here.
@login_required
def artwork_create(request):
    if not request.user.is_artist and not request.user.is_staff:
        return HttpResponseForbidden("<div style='text-align: center; font-size: 24px;'>404 Error !! <br> You are not authorized to create artworks.</div>")
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.artist = request.user
            artwork.save()
            messages.success(request, f"Artwork '{artwork.title}' created successfully!")
            return redirect('artist')
    else:
        form = ArtworkForm()
    artist = Artist.objects.get(user=request.user)
    context = {
        'form': form,
        'artist': artist, 
    }
    return render(request, 'Artists/artwork.html', context)
@login_required
def artwork_update(request, id):
    artwork = get_object_or_404(Artwork, pk=id)
    if not (request.user == artwork.artist or request.user.is_staff):
         return HttpResponseForbidden("<div style='text-align: center; font-size: 24px;'>404 Error !! <br> You are not authorized to update artworks.</div>")
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            return redirect('artist')
    else:
        form = ArtworkForm(instance=artwork)
    artist = Artist.objects.get(user=request.user)

    context = {
        'form': form,
        'artist': artist,
        'arts':artwork
    }
    return render(request, 'Artists/edit_artwork.html', context)

@login_required
def artwork_delete(request, id):
    artwork = get_object_or_404(Artwork, pk=id)
    if not (request.user == artwork.artist or request.user.is_admin):
         return HttpResponseForbidden("<div style='text-align: center; font-size: 24px; color:red;'>404 Error !! <br> You are not authorized to delete artworks.</div>")
    if request.method == 'POST':
        artwork.delete()
    return redirect('artist')


def art_details(request, id):
    artwork = get_object_or_404(Artwork, pk=id)
    context = {
        'artwork': artwork
    }
    return render(request, 'Artworks/view_artwork.html', context)


@login_required
def toggle_wishlist(request, id):
    artwork = get_object_or_404(Artwork, id=id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    if artwork in wishlist.artworks.all():
        wishlist.artworks.remove(artwork)
        added = False
    else:
        wishlist.artworks.add(artwork)
        added = True

    return JsonResponse({'added': added})

@login_required
def wishlist_view(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlisted_artworks = wishlist.artworks.all()
    context = {
        'wishlisted_artworks': wishlisted_artworks
    }
    return render(request, 'User/user_profile.html', context)