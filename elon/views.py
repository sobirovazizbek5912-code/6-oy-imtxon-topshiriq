from django.shortcuts import render,redirect, get_object_or_404
from .models import Elon, Category

def home(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')

    if category_id:
        elons = Elon.objects.filter(category_id=category_id)
    else:
        elons = Elon.objects.all()

    return render(request, 'home.html', {
        'elons': elons,
        'categories': categories
    })


def elon_detail(request, id):
    elon = get_object_or_404(Elon, id=id)
    return render(request, 'detail.html', {'elon': elon})


def create_elon(request):
    if request.method == 'POST':
        form = Elon(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Elon()

    return render(request, 'create.html', {'form': form})


def update_elon(request, id):
    elon = get_object_or_404(Elon, id=id)

    if request.method == 'POST':
        form = Elon(request.POST, request.FILES, instance=elon)
        if form.is_valid():
            form.save()
            return redirect('detail', id=elon.id)
    else:
        form = Elon(instance=elon)

    return render(request, 'update.html', {'form': form})


def delete_elon(request, id):
    elon = get_object_or_404(Elon, id=id)

    if request.method == 'POST':
        elon.delete()
        return redirect('home')

    return render(request, 'delete.html', {'elon': elon})