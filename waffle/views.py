from django.shortcuts import render
from .models import WaffleVariety, Store
from django.shortcuts import get_object_or_404
from .forms import WaffleVarietyForm

# Create your views here.
def all_waffle(request):
    waffles = WaffleVariety.objects.all()
    return render(request, 'waffle/all_waffle.html', {'waffles': waffles})

def waffle_detail(request, waffle_id):
    waffle = get_object_or_404(WaffleVariety, pk=waffle_id)
    return render(request, 'waffle/waffle_detail.html', {'waffle':waffle})


def waffle_stores_view(request):
    stores = None
    if request.method =='POST':
        form = WaffleVarietyForm(request.POST)
        if form.is_valid():
            waffle_variety = form.cleaned_data['waffle_variety']
            stores = Store.objects.filter(waffle_varieties = waffle_variety)

    else:
        form = WaffleVarietyForm()
    
    return render (request,'waffle/waffle_stores.html', {'stores':stores, 'form': form})