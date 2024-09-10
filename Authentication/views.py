from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetForm, CustomSetPasswordForm, CustomPasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from allauth.account.utils import send_email_confirmation
from django.contrib import messages
from allauth.account.views import ConfirmEmailView
from .forms import SignUpForm, LoginForm
from Artworks.models import Artwork, Exhibition
from .models import Artist
from User . models import Visitor
from django.contrib.auth import get_user_model
from .backends import CaseInsensitiveModelBackend
from django.utils.timezone import now
from customadmin.models import AdminProfile

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account until email is verified
            user.save()
            key = send_email_confirmation(request, user)
            
            msg = 'User created. Please check your email for verification instructions.'
            
            # Reverse the URL with the `key` argument
            url = reverse('verify_email', kwargs={'key': key})
            
            # Redirect to the verification URL
            messages.success(request, 'Registered Successfully!')
            return redirect(url)
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'Authentication/register.html', {'form': form, 'msg': msg})

#Admin register
def admin_register(request):
    msg=None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_admin = True
            user.is_active = False 
            user.save()
            key = send_email_confirmation(request, user)
            
            msg = 'User created. Please check your email for verification instructions.'
            
            # Reverse the URL with the `key` argument
            url = reverse('verify_email', kwargs={'key': key})
            messages.success(request, 'Admin registered successfully')
            return redirect(url) 
    else:
        form = SignUpForm()
    return render(request, 'Authentication/admin_register.html', {'form': form, 'msg':msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            username_or_email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Specify the backend explicitly
            backend = 'Authentication.backends.CaseInsensitiveModelBackend'
            user = authenticate(request, username=username_or_email, password=password, backend=backend)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    if hasattr(user, 'is_admin') and user.is_admin:
                        messages.success(request, 'Welcome Admin!')
                        return redirect('admin_dashboard')
                    elif hasattr(user, 'is_user') and user.is_user:
                        messages.success(request, 'Logged in Successfully!')
                        return redirect('index')
                    elif hasattr(user, 'is_artist') and user.is_artist:
                        messages.success(request, 'Logged in Successfully!', extra_tags='login')
                        return redirect('artist')
                else:
                    msg = 'Please verify your email address to activate your account.'
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating form'

    return render(request, 'Authentication/login.html', {'form': form, 'msg': msg})

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

def user(request):
    return render(request, 'Home/index.html')

@login_required
def custom_admin(request):
    user = request.user

    try:
        admin = AdminProfile.objects.get(user=user)
    except AdminProfile.DoesNotExist:
        return redirect('create_admin')

    total_artworks = Artwork.objects.count()
    total_artists = Artist.objects.count()
    total_users = Visitor.objects.count()
    total_exhibitions = Exhibition.objects.count()

    # Get the 5 most recent visitors
    visitors = Visitor.objects.all().order_by('-user__date_joined')[:5]

    # Get the 5 most recent artists
    artists = Artist.objects.all().order_by('-user__date_joined')[:5]

    # Prepare data for each visitor
    visitor_data = []
    for visitor in visitors:
        if visitor.user.date_joined:
            time_since_registration = now() - visitor.user.date_joined
            seconds = time_since_registration.total_seconds()

            if seconds < 60:
                time_since_registration_formatted = f"{int(seconds)} sec"
            elif seconds < 3600:
                minutes = seconds // 60
                time_since_registration_formatted = f"{int(minutes)} min"
            elif seconds < 86400:
                hours = seconds // 3600
                time_since_registration_formatted = f"{int(hours)} hrs"
            elif seconds < 604800:
                days = seconds // 86400
                time_since_registration_formatted = f"{int(days)} days"
            elif seconds < 2592000:
                weeks = seconds // 604800
                time_since_registration_formatted = f"{int(weeks)} wk"
            else:
                months = seconds // 2592000
                time_since_registration_formatted = f"{int(months)} mon"
        else:
            time_since_registration_formatted = "Registration date not available"

        visitor_data.append({
            'name': visitor.name if visitor.name else visitor.user.username,
            'message': 'User Registered!!',
            'time_since_registration': time_since_registration_formatted,
            'profile_picture': visitor.profile_picture.url if visitor.profile_picture else '{images/layout_img/default.png}',
            'bio': visitor.biography,
            'occupation': visitor.occupation,
        })

    # Prepare data for each artist
    artist_data = []
    for artist in artists:
        if artist.user.date_joined:
            time_since_registration = now() - artist.user.date_joined
            seconds = time_since_registration.total_seconds()

            if seconds < 60:
                time_since_registration_formatted = f"{int(seconds)} sec"
            elif seconds < 3600:
                minutes = seconds // 60
                time_since_registration_formatted = f"{int(minutes)} min"
            elif seconds < 86400:
                hours = seconds // 3600
                time_since_registration_formatted = f"{int(hours)} hrs"
            elif seconds < 604800:
                days = seconds // 86400
                time_since_registration_formatted = f"{int(days)} days"
            elif seconds < 2592000:
                weeks = seconds // 604800
                time_since_registration_formatted = f"{int(weeks)} wk"
            else:
                months = seconds // 2592000
                time_since_registration_formatted = f"{int(months)} mon"
        else:
            time_since_registration_formatted = "Registration date not available"

        artist_data.append({
            'name': artist.name if artist.name else artist.user.username,
            'message': 'Artist Registered!!',
            'time_since_registration': time_since_registration_formatted,
            'profile_picture': artist.profile_picture.url if artist.profile_picture else 'images/layout_img/default.png',
            'bio': artist.biography,
        })

    context = {
        'total_artworks': total_artworks,
        'total_artists': total_artists,
        'total_users': total_users,
        'visitor_data': visitor_data,
        'artist_data': artist_data, 
        'admin': admin,
        'total_exhibition':total_exhibitions
    }
    return render(request, 'customadmin/admin.html', context)

@login_required
def logout_view(request):
    if request.method=='POST':
        messages.success(request, 'Logged out Successfully!')
        logout(request)
        return redirect('login_view')

class VerifyEmail(ConfirmEmailView):
    template_name = 'Authentication/verify_email.html'
    success_url = '/'

    def post(self, *args, **kwargs):
        response = super().post(*args, **kwargs)
        user = self.request.user
        user.is_active = True
        user.save()
        return response

class CustomConfirmEmailView(ConfirmEmailView):
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.confirm(self.request)
        user = self.object.email_address.user
        user.is_active = True
        user.save()
        return redirect(reverse_lazy('verify_email_success'))


# Pass reset views

class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'account/email/password_reset_email.html'
    subject_template_name = 'account/email/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')
    form_class = CustomPasswordResetForm

class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('login_view')
    form_class = CustomSetPasswordForm

  
# Password change views
class CustomPasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('user_profile')
    form_class = CustomPasswordChangeForm

    def form_valid(self, form):
        messages.success(self.request, 'Password Changed Successfully')
        return super().form_valid(form)
