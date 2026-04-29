from django.shortcuts import get_object_or_404, redirect, render
from .models import Elon, Category
from .models import Comment
from .forms import ElonForm

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
        form = ElonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ElonForm()

    return render(request, 'create.html', {'form': form})


def update_elon(request, id):
    elon = get_object_or_404(Elon, id=id)

    if request.method == 'POST':
        form = ElonForm(request.POST, request.FILES, instance=elon)
        if form.is_valid():
            form.save()
            return redirect('detail', id=elon.id)
    else:
        form = ElonForm(instance=elon)

    return render(request, 'update.html', {'form': form})


def delete_elon(request, id):
    elon = get_object_or_404(Elon, id=id)

    if request.method == 'POST':
        elon.delete()
        return redirect('home')

    return render(request, 'delete.html', {'elon': elon})


def add_comment(request, elon_id):
    elon = get_object_or_404(Elon, id=elon_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')

        Comment.objects.create(
            elon=elon,
            name=name,
            text=text
        )

        return redirect('detail', id=elon.id)


def update_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    if request.method == 'POST':
        comment.name = request.POST.get('name')
        comment.text = request.POST.get('text')
        comment.save()
        return redirect('detail', id=comment.elon.id)

    return render(request, 'update_comment.html', {'comment': comment})


def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    elon_id = comment.elon.id
    comment.delete()
    return redirect('detail', id=elon_id)


def add_comment(request, elon_id):
    elon = get_object_or_404(Elon, id=elon_id)

    if request.method == 'POST':
        Comment.objects.create(
            elon=elon,
            user=request.user if request.user.is_authenticated else None,
            name=request.POST.get('name'),
            text=request.POST.get('text')
        )

    return redirect('detail', id=elon.id)


def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.user == comment.user or request.user.is_superuser:
        elon_id = comment.elon.id
        comment.delete()
        return redirect('detail', id=elon_id)

    return redirect('detail', id=comment.elon.id)
