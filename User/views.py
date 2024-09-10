from django.shortcuts import render, redirect, get_object_or_404
from . models import Visitor
from django.contrib.auth.decorators import login_required
from .forms import VisitorForm
from django.db import IntegrityError
from . forms import BillingAddressForm
from . models import BillingAddress
from Artworks . models import Wishlist
from Authentication . models import Artist
from Artworks .models import Artwork
from django.contrib import messages
from Home . models import CartItem, OrderedItem
from django.core.paginator import Paginator
import datetime

# Create your views here.

@login_required
def artist_profile_view(request, artist_id):
    user=request.user
    cart_item_count = 0
    try:
        profile = Visitor.objects.get(user=user)
        cart_item_count = CartItem.objects.filter(user=user).count()
    except Visitor.DoesNotExist:
        pass
    artist = get_object_or_404(Artist, id=artist_id)
    arts = Artwork.objects.filter(artist=artist.user).order_by('-year_created')[:4]
    artworks = []
    for art in arts:
        artworks.append({
            'id': art.id,
            'title': art.title,  
            'image': art.image.url if art.image else None,  
            
        })

    context = {
        'artist': artist,
        'arts': artworks, 
        'art_count': arts.count(),
        'art_details': 'art_details', 
        'profile':profile,
        'cart_item_count':cart_item_count
    }
    return render(request, 'User/artist_profile_view.html', context)


@login_required
def create_user(request):
    user = request.user
    try:
        visitor = Visitor.objects.get(user=user)
    except Visitor.DoesNotExist:
        visitor = None
    
    try:
        billing_address = BillingAddress.objects.get(user=user)
    except BillingAddress.DoesNotExist:
        billing_address = None

    if request.method == 'POST':
        visitor_form = VisitorForm(request.POST, request.FILES, instance=visitor)
        billing_form = BillingAddressForm(request.POST, request.FILES, instance=billing_address)
        if visitor_form.is_valid() and billing_form.is_valid():
            try:
                visitor = visitor_form.save(commit=False)
                if not visitor.user:
                    visitor.user = user
                visitor.save()
                billing_address = billing_form.save(commit=False)
                if not billing_address.user:
                    billing_address.user = user
                billing_address.save()
                messages.success(request, 'Profile Created Successfully!')
                return redirect('user_profile')
            except IntegrityError:
                return render(request, 'User/create_user.html', {
                    'visitor_form': visitor_form,
                    'billing_form': billing_form,
                    'error': 'Profile could not be created due to a database error.'
                })
    else:
        visitor_form = VisitorForm(instance=visitor)
        billing_form = BillingAddressForm(instance=billing_address)

    return render(request, 'User/create_user.html', {
        'visitor_form': visitor_form,
        'billing_form': billing_form
    })

@login_required
def update_user(request):
    user = request.user
    try:
        visitor = Visitor.objects.get(user=user)
    except Visitor.DoesNotExist:
        visitor = None

    if request.method == 'POST':
        form = VisitorForm(request.POST, request.FILES, instance=visitor)
        if form.is_valid():
            try:
                if visitor:
                    form.save()  
                else:
                    visitor = form.save(commit=False)
                    visitor.user = user
                    visitor.save()  
                messages.success(request, 'Profile Updated Successfully!')
                return redirect('user_profile') 
            except IntegrityError:
                return render(request, 'User/update_user.html', {'form': form, 'error': 'Visitor profile could not be created due to a database error.'})
    else:
        form = VisitorForm(instance=visitor)

    return render(request, 'User/update_user.html', {'form': form})

@login_required(login_url='login_view')
def user_profile(request):
    user = request.user
    wishlist, created = Wishlist.objects.get_or_create(user=user)
    wishlisted_artworks = wishlist.artworks.all()
    
    cart_item_count = 0
    try:
        profile = Visitor.objects.get(user=user)
        cart_item_count = CartItem.objects.filter(user=user).count()
    except Visitor.DoesNotExist:
        return redirect('create_user')
    try:
        orders = OrderedItem.objects.filter(user=user)
    except OrderedItem.DoesNotExist:
        pass
    
    try:
        billing_address = BillingAddress.objects.get(user=user)
    except BillingAddress.DoesNotExist:
        billing_address = None

    context = {
        'profile': profile,
        'billing': billing_address,
        'orders': orders,
        'wishlisted_artworks': wishlisted_artworks,
        'cart_item_count': cart_item_count
    }
    return render(request, 'User/user_profile_page.html', context)

@login_required
def billing_address(request):
    user = request.user
    try:
        billing_address = BillingAddress.objects.get(user=user)
    except BillingAddress.DoesNotExist:
        billing_address = None

    if request.method == 'POST':
        form = BillingAddressForm(request.POST, instance=billing_address)
        if form.is_valid():
            billing_address = form.save(commit=False)
            billing_address.user = user
            billing_address.save()
            messages.success(request, 'Billing address updated Successfully!')
            return redirect('user_profile') 
    else:
        form = BillingAddressForm(instance=billing_address)

    return render(request, 'User/billing_det.html', {'form': form})

@login_required
def exhibition(request):
    user=request.user
    try:
        profile = Visitor.objects.get(user=user)
    except Visitor.DoesNotExist:
        pass
    today = datetime.date.today()
    current_exhibitions = Exhibition.objects.filter(start_date__lte=today, end_date__gte=today)
    upcoming_exhibitions = Exhibition.objects.filter(start_date__gt=today)
    print(current_exhibitions)
    print(upcoming_exhibitions)
    return render(request, 'User/exhibition.html', {
        'current_exhibitions': current_exhibitions,
        'upcoming_exhibitions': upcoming_exhibitions,
        'profile':profile
    })
    
from django.shortcuts import get_object_or_404
from Artworks.models import Exhibition, Artwork

@login_required
def view_exhibitions(request, exhibition_id):
    try:
        admin = Visitor.objects.get(user=request.user)
    except Visitor.DoesNotExist:
        admin = None
    # Retrieve the exhibition by its id
    exhibition = get_object_or_404(Exhibition, id=exhibition_id)
    artworks = exhibition.artworks.all()  # Assuming `artworks` is the related name in Exhibition model
    paginator = Paginator(artworks, 10) 
    page_number = request.GET.get('page')
    paginated_artworks = paginator.get_page(page_number)
    
    # Get the artworks associated with this exhibition

    # Pass the exhibition and its artworks to the template
    return render(request, 'User/view_exhibitions.html', {
        'exhibition': exhibition,
        'artworks': paginated_artworks,
        'profile':admin
    })
    
@login_required
def ordered_items(request):
    user = request.user
    wishlist, created = Wishlist.objects.get_or_create(user=user)
    wishlisted_artworks = wishlist.artworks.all()
    
    cart_item_count = 0
    try:
        profile = Visitor.objects.get(user=user)
        cart_item_count = CartItem.objects.filter(user=user).count()
    except Visitor.DoesNotExist:
        return redirect('create_user')
    try:
        orders = OrderedItem.objects.filter(user=user)
    except OrderedItem.DoesNotExist:
        pass
    
    try:
        billing_address = BillingAddress.objects.get(user=user)
    except BillingAddress.DoesNotExist:
        billing_address = None

    context = {
        'profile': profile,
        'billing': billing_address,
        'orders': orders,
        'wishlisted_artworks': wishlisted_artworks,
        'cart_item_count': cart_item_count
    }
    return render(request,'User/ordered_items.html',context)


@login_required
def favourites_list(request):
    user = request.user
    wishlist, created = Wishlist.objects.get_or_create(user=user)
    wishlisted_artworks = wishlist.artworks.all()
    
    cart_item_count = 0
    try:
        profile = Visitor.objects.get(user=user)
        cart_item_count = CartItem.objects.filter(user=user).count()
    except Visitor.DoesNotExist:
        return redirect('create_user')
    try:
        orders = OrderedItem.objects.filter(user=user)
    except OrderedItem.DoesNotExist:
        pass
    
    try:
        billing_address = BillingAddress.objects.get(user=user)
    except BillingAddress.DoesNotExist:
        billing_address = None

    context = {
        'profile': profile,
        'billing': billing_address,
        'orders': orders,
        'wishlisted_artworks': wishlisted_artworks,
        'cart_item_count': cart_item_count
    }
    
    return render(request,'User/favourites_list.html',context)



    