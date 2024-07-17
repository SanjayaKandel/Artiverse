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
from Artworks.models import Artwork
from .models import Artist

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


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.is_admin:
                        messages.success(request, 'Welcome Admin!')
                        return redirect('user_dashboard')  
                    elif user.is_user:
                        messages.success(request, 'Logged in Successfully!')
                        return redirect('index')  
                    elif user.is_artist:
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


@login_required
def logout_view(request):
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

def admin(request):
    return render(request, 'Authentication/admin.html')

def user(request):
    return render(request, 'Home/index.html')

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
