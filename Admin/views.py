from django.shortcuts import render, get_object_or_404
from .models import Exhibition
import datetime
from django.shortcuts import render, redirect
from .forms import ExhibitionForm
from django.contrib.auth.decorators import login_required
from User . models import Visitor
@login_required
def add_exhibition(request):
    if request.method == 'POST':
        form = ExhibitionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('exhibition_list')
    else:
        form = ExhibitionForm()
    return render(request, 'Admin/add_exhibition.html', {'form': form})

@login_required
def exhibition_list(request):
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
    
def exhibition_detail(request, exhibition_id):
    exhibition = get_object_or_404(Exhibition, id=exhibition_id)
    return render(request, 'User/exhibition_detail.html', {'exhibition': exhibition})
