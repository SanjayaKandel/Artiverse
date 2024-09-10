from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from Artworks.models import Artwork
from Authentication . models import Artist
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from . forms import AdminProfileForm
from . models import AdminProfile
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseForbidden
from User . models import Visitor, BillingAddress
import datetime
def is_admin(user):
    return user.is_admin

# @login_required
# @user_passes_test(is_admin)
# def custom_admin(request):
    
#     return render(request, 'customadmin/admin.html')

@login_required
@user_passes_test(is_admin)
def view_artwork(request):
    user = request.user
    try:
        admin = AdminProfile.objects.get(user=user)
    except AdminProfile.DoesNotExist:
        admin = None
    artworks = Artwork.objects.all()
    exhibitions = Exhibition.objects.all()
    paginator = Paginator(artworks, 20)  # Show 20 artworks per page
    page_number = request.GET.get('page')
    paginated_artworks = paginator.get_page(page_number)
    
    return render(request, 'customadmin/update_artwork.html', {'artworks': paginated_artworks, 'admin':admin,'exhibitions':exhibitions})

@login_required
@user_passes_test(is_admin)
def manage_user(request):
    user = request.user
    try:
        admin = AdminProfile.objects.get(user=user)
    except AdminProfile.DoesNotExist:
        admin = None
    users= Visitor.objects.all()
    paginator = Paginator(users, 20)  # Show 20 artworks per page
    page_number = request.GET.get('page')
    paginated_artworks = paginator.get_page(page_number)
    
    return render(request, 'customadmin/manage_user.html', {'users': paginated_artworks, 'admin':admin,})
@login_required
@user_passes_test(is_admin)
def manage_artist(request):
    user = request.user
    try:
        admin = AdminProfile.objects.get(user=user)
    except AdminProfile.DoesNotExist:
        admin = None
    artists= Artist.objects.all()
    paginator = Paginator(artists, 20)  # Show 20 artworks per page
    page_number = request.GET.get('page')
    paginated_artworks = paginator.get_page(page_number)
    
    return render(request, 'customadmin/manage_artist.html', {'artists': paginated_artworks, 'admin':admin,})

#         <----------Delete data---------->


@login_required
@user_passes_test(is_admin)
def delete_artist(request, id):
    user = get_object_or_404(Artist, pk=id)
    #admin check
    if not request.user.is_admin:
        return HttpResponseForbidden("<div style='text-align: center; font-size: 24px; color:red;'>404 Error !! <br> You are not authorized to delete Artist Data.</div>")
    
    if request.method == 'POST':
        user.delete()
        messages.success(request, f"Artist '{user.name}' deleted successfully!")  # Fixed message to refer to user
        return redirect('manage_artist')  # Redirect should be inside POST check
        
    return render(request, 'confirm_delete.html', {'user': user})  # Consider adding a confirmation page


@login_required
@user_passes_test(is_admin)
def delete_user(request, id):
    user = get_object_or_404(Visitor, pk=id)
    #admin check
    if not request.user.is_admin:
        return HttpResponseForbidden("<div style='text-align: center; font-size: 24px; color:red;'>404 Error !! <br> You are not authorized to delete User Data.</div>")
    
    if request.method == 'POST':
        user.delete()
        messages.success(request, f"User '{user.name}' deleted successfully!")  # Fixed message to refer to user
        return redirect('manage_user')  # Redirect should be inside POST check
        
    return render(request, 'confirm_delete.html', {'user': user})  # Consider adding a confirmation page


@csrf_exempt
@login_required
@user_passes_test(is_admin)
def delete_artwork(request, artwork_id):
    if request.method == 'POST':
        artwork = get_object_or_404(Artwork, id=artwork_id)

        if artwork:
            # Email sent to artist
            send_mail(
                subject='Your artwork has been deleted',
                message=f'Dear @{artwork.artist},\n\n'
                        f'We regret to inform you that your artwork titled "{artwork.title}" has been removed from Artiverse. This decision was made to ensure the safety and compliance of our platform with our terms and conditions.\n'
                        'Please understand that this action is part of our commitment to maintaining a secure and respectful community for all users.\n Should you have any questions or need further assistance, we are here to help.'
                        'Thank you for your understanding and cooperation.\n\n'
                        'Thank you for your understanding and cooperation.\n\n'
                        'Warm regards,\nThe Artiverse Team',
                from_email='artiverseverify@gmail.com',
                recipient_list=[artwork.artist.email],
                fail_silently=False,
            )

            # Delete the artwork
            artwork.delete()
            messages.success(request, 'Artwork deleted successfully')
    return redirect('view_artwork')

@csrf_exempt
@login_required
@user_passes_test(is_admin)
def admin_profile(request):
    user = request.user
    try:
        admin = AdminProfile.objects.get(user=user)
    except AdminProfile.DoesNotExist:
        admin = None
    
    return render(request, 'customadmin/admin_profile.html', { 'admin':admin,})

@csrf_exempt
@login_required
@user_passes_test(is_admin)
def create_admin_profile(request):
    user = request.user
    try:
        admin = AdminProfile.objects.get(user=user)
    except AdminProfile.DoesNotExist:
        admin = None

    if request.method == 'POST':
        admin_form = AdminProfileForm(request.POST, request.FILES, instance=admin)
        if admin_form.is_valid():
            user=request.user
            if hasattr(user,'admin'):
                return JsonResponse("Profile already existed!!")
            try:
                admin = admin_form.save(commit=False)
                admin.user=user
                admin.save()
                messages.success(request, 'Profile Created Successfully!')
                return redirect('admin_dashboard')
            except IntegrityError:
                return render(request, 'customadmin/create_admin_profile.html', {
                    'form': admin_form,
                    'error': 'Profile could not be created due to a database error.'
                })
    else:
        admin_form = AdminProfileForm(instance=admin)

    return render(request,'customadmin/create_admin_profile.html',
                  {
                      'form': admin_form,
                  })

# <----------View Pages for Admin section----------->
@login_required
@user_passes_test(is_admin)
def artwork_view_admin(request, id):
    try:
        admin = AdminProfile.objects.get(user=request.user)
    except AdminProfile.DoesNotExist:
        admin = None

    artwork = get_object_or_404(Artwork, id=id)
    artist = artwork.artist

    # Fetch all artworks by the artist
    artist_artworks = Artwork.objects.filter(artist=artist)

    context = {
        'artist': artist,
        'artwork': artwork,
        'admin': admin,
        'artist_artworks': artist_artworks, 
    }
    return render(request, 'customadmin/viewpages/artwork_view_admin.html', context)

@login_required
@user_passes_test(is_admin)
def user_view_admin(request, id):
    try:
        admin = AdminProfile.objects.get(user=request.user)
    except AdminProfile.DoesNotExist:
        admin = None

    user = get_object_or_404(Visitor, id=id)
    billing=get_object_or_404(BillingAddress, id=id)

    context = {
        'user': user,
        'billing':billing,
        'admin': admin,

    }
    return render(request, 'customadmin/viewpages/user_view_admin.html', context)
@csrf_exempt
@login_required
@user_passes_test(is_admin)
def artist_view_admin(request, id):
    try:
        admin = AdminProfile.objects.get(user=request.user)
    except AdminProfile.DoesNotExist:
        admin = None

    user = get_object_or_404(Artist, id=id)

    context = {
        'user': user,

        'admin': admin,

    }
    return render(request, 'customadmin/viewpages/artist_view_admin.html', context)


# View for creating an exhibition
from Artworks.models import Exhibition
from Artworks.forms import ExhibitionForm
@csrf_exempt
@login_required
@user_passes_test(is_admin)
def create_exhibition(request):
    try:
        admin = AdminProfile.objects.get(user=request.user)
    except AdminProfile.DoesNotExist:
        admin = None
    if request.method == 'POST':
        form = ExhibitionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('exhibition_list')  # Redirect to a page listing exhibitions or another desired page
    else:
        form = ExhibitionForm()
    
    artworks = Artwork.objects.all()  # Fetch all artworks for adding to exhibition
    return render(request, 'customadmin/create_exhibition.html', {'form': form, 'artworks': artworks, 'admin':admin})

# View for adding an artwork to an exhibition
@csrf_exempt
@login_required
@user_passes_test(is_admin)
def add_to_exhibition(request):
    if request.method == 'POST':
        artwork_id = request.POST.get('artwork_id')
        exhibition_id = request.POST.get('exhibition_id')
        artwork = get_object_or_404(Artwork, id=artwork_id)
        exhibition = get_object_or_404(Exhibition, id=exhibition_id)
        
        # Add artwork to the exhibition
        exhibition.artworks.add(artwork)
        exhibition.save()

        messages.success(request, f'{artwork.title} added to {exhibition.title} successfully!')
        return redirect('exhibition_list')  # Redirect to the manage artwork page

@csrf_exempt
@login_required
def exhibition_list(request):
    user=request.user
    try:
        profile = AdminProfile.objects.get(user=user)
    except AdminProfile.DoesNotExist:
        pass
    today = datetime.date.today()
    current_exhibitions = Exhibition.objects.filter(start_date__lte=today, end_date__gte=today)
    upcoming_exhibitions = Exhibition.objects.filter(start_date__gt=today)
    print(current_exhibitions)
    print(upcoming_exhibitions)
    return render(request, 'customadmin/exhibition_list.html', {
        'current_exhibitions': current_exhibitions,
        'upcoming_exhibitions': upcoming_exhibitions,
        'admin':profile
    })
    
from django.shortcuts import get_object_or_404
from Artworks.models import Exhibition, Artwork

@login_required
def exhibition_details(request, exhibition_id):
    try:
        admin = AdminProfile.objects.get(user=request.user)
    except AdminProfile.DoesNotExist:
        admin = None
    # Retrieve the exhibition by its id
    exhibition = get_object_or_404(Exhibition, id=exhibition_id)
    artworks = exhibition.artworks.all()  # Assuming `artworks` is the related name in Exhibition model
    paginator = Paginator(artworks, 20)  # Show 20 artworks per page
    page_number = request.GET.get('page')
    paginated_artworks = paginator.get_page(page_number)
    
    # Get the artworks associated with this exhibition

    # Pass the exhibition and its artworks to the template
    return render(request, 'customadmin/viewpages/exhibition_details.html', {
        'exhibition': exhibition,
        'artworks': paginated_artworks,
        'admin':admin
    })

    