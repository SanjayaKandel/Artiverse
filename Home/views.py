from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404,redirect, get_list_or_404
from Artworks.models import Artwork
from User. models import Visitor
from Authentication.models import User, Artist
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from . models import CartItem


# Create your views here.

def index(request):
    latest_arts = Artwork.objects.order_by('-year_created')[:6]
    user = request.user
    profile = None
    if user.is_authenticated:
        try:
            profile = Visitor.objects.get(user=user)
        except Visitor.DoesNotExist:
            pass

    context = {
        'arts': latest_arts,
        'profile': profile
    }

    return render(request, 'Home/index.html', context)

@login_required
def explore(request):
    query = request.GET.get('query', '')
    medium = request.GET.get('medium', '')
    style = request.GET.get('style', '')
    price_range_min = request.GET.get('price_range_min', '')
    price_range_max = request.GET.get('price_range_max', '')
    genre = request.GET.get('genre', '')
    user = request.user
    profile = None

    try:
        profile = Visitor.objects.get(user=user)
    except Visitor.DoesNotExist:
        pass

    arts = Artwork.objects.all()

    if query:
        arts = arts.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    if medium:
        arts = arts.filter(medium=medium)

    if style:
        arts = arts.filter(style=style)

    if genre:
        arts = arts.filter(genre=genre)

    if price_range_min and price_range_max:
        arts = arts.filter(price__range=(price_range_min, price_range_max))
    elif price_range_min:
        arts = arts.filter(price__gte=price_range_min)
    elif price_range_max:
        arts = arts.filter(price__lte=price_range_max)

    paginator = Paginator(arts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Prepare a list to store each artwork with artist details
    artworks_with_artist = []

    for artwork in page_obj:
        artist_id = None
        artist_name = ""
        artist_profile_pic = ""

        if artwork.artist:
            # Retrieve artist details from the associated User and Artist models
            artist_user = artwork.artist
            if artist_user.is_artist:
                artist_profile = Artist.objects.get(user=artist_user)
                artist_name = artist_profile.name
                artist_id = artist_profile.id  # Extract artist_id
                if artist_profile.profile_picture:
                    artist_profile_pic = artist_profile.profile_picture.url

        # Append artwork details along with artist details to the list
        artworks_with_artist.append({
            'artwork': artwork,
            'artist_id': artist_id,
            'artist_name': artist_name,
            'artist_profile_pic': artist_profile_pic,
        })

    context = {
        'arts': artworks_with_artist,
        'page_no': page_obj,
        'profile': profile,
    }

    return render(request, 'Home/explore.html', context)


@login_required

def search(request):
    query = request.GET.get('query', '')
    medium = request.GET.get('medium', '')
    style = request.GET.get('style', '')
    price_range_min = request.GET.get('price_range_min', '')
    price_range_max = request.GET.get('price_range_max', '')
    genre = request.GET.get('genre', '')
    
    user = request.user
    profile = None
    try:
        profile = Visitor.objects.get(user=user)
    except Visitor.DoesNotExist:   
        pass
    
    result = Artwork.objects.all()
    
    if query:
        result = result.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    if medium:
        result = result.filter(medium=medium)

    if style:
        result = result.filter(style=style)

    if genre:
        result = result.filter(genre=genre)

    if price_range_min and price_range_max:
        result = result.filter(price__range=(price_range_min, price_range_max))
    elif price_range_min:
        result = result.filter(price__gte=price_range_min)
    elif price_range_max:
        result = result.filter(price__lte=price_range_max)
        
    paginator = Paginator(result, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Prepare a list to store each artwork with artist details
    artworks_with_artist = []

    for artwork in page_obj:
        artist_id = None
        artist_name = ""
        artist_profile_pic = ""

        if artwork.artist:
            # Retrieve artist details from the associated User and Artist models
            artist_user = artwork.artist
            if artist_user.is_artist:
                artist_profile = Artist.objects.get(user=artist_user)
                artist_name = artist_profile.name
                artist_id = artist_profile.id  # Extract artist_id
                if artist_profile.profile_picture:
                    artist_profile_pic = artist_profile.profile_picture.url

        # Append artwork details along with artist details to the list
        artworks_with_artist.append({
            'artwork': artwork,
            'artist_id': artist_id,
            'artist_name': artist_name,
            'artist_profile_pic': artist_profile_pic,
        })

    context = {
        'arts': artworks_with_artist,
        'result':result,
        'query': query,
        'medium':medium,
        'style':style,
        'genre':genre,
        'price_range_min':price_range_min,
        'price_range_max':price_range_max,
        'profile':profile
    }
    return render(request, 'Home/search.html', context)


@login_required
def artist_list(request):
    artists = Artist.objects.all()
    user = request.user
    profile = None
    try:
        profile = Visitor.objects.get(user=user)
    except Visitor.DoesNotExist:
        pass
    return render(request, 'Home/artist_list.html', {'artists': artists, 'profile': profile})


def about_page(request):
    user = request.user
    profile = None
    if user.is_authenticated:
        try:
            profile = Visitor.objects.get(user=user)
        except Visitor.DoesNotExist:
            pass
    
    customer_count = Visitor.objects.count()
    artist_count = Artist.objects.count()
    user_count = User.objects.count()
    artwork_count = Artwork.objects.count()
    
    context = {
        'profile': profile,
        'customer_count': customer_count,
        'artist_count': artist_count,
        'user_count': user_count,
        'artwork_count': artwork_count,
    }
    
    return render(request, 'Home/about.html', context)


@login_required
def add_to_cart(request, artwork_id):
    artwork = get_object_or_404(Artwork, id=artwork_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, artwork=artwork)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    response_data = {
        'item_name': artwork.title,  # Assuming artwork has a 'name' field
        'cart_count': CartItem.objects.filter(user=request.user).count()
    }
    
    return JsonResponse(response_data)

@login_required
def cart_view(request):
    user=request.user
    profile = None
    try:
        profile = Visitor.objects.get(user=user)
    except Visitor.DoesNotExist:
        pass
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)
    context={
        'cart_items': cart_items, 
        'total_price': total_price,
        'profile':profile
        }
    return render(request, 'Home/cart.html', context)
@login_required
def delete_item(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id)
    item.delete()
    return JsonResponse({'message': 'Item deleted successfully'})

