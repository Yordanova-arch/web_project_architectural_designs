from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from core.cleaned_up_files import cleaned_up_files
from core.decorators import required_user
from designs.forms import CreateDesignForm
from designs.models import Designs


def list_designs(request):
    designs = Designs.objects.all()
    for design in designs:
        design.can_delete = design.created_by_id == request.user.id
        design.can_edit = design.created_by_id == request.user.id

    context = {
        'designs': designs,
        'current_page': 'list_designs',


    }
    return render(request, 'designs/list_designs.html', context)


def details_design(request, pk):
    design = Designs.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'design': design,


            'can_delete': design.created_by_id == request.user.id,
            'can_edit': design.created_by_id == request.user.id,

        }

        return render(request, 'designs/design_details.html', context)


@login_required
def create_design(request):
    if request.method == "GET":
        form = CreateDesignForm()
        context = {

            'form': form,
            'current_page': 'create_designs'
        }
        return render(request, 'designs/design_create.html', context)
    else:
        form = CreateDesignForm(request.POST, request.FILES)
        if form.is_valid():
            design = form.save(commit=False)
            design.created_by_id = request.user.id
            design.save()

            return redirect('list designs')
        context = {

            'form': form,
            'current_page': 'create_designs'
        }
        return render(request, 'designs/design_create.html', context)


@login_required
@required_user(model=Designs)
def delete_design(request, pk):
    design = Designs.objects.get(pk=pk)
    # to delete only owner
    if design.created_by_id != request.user.id:
        return redirect('index')
    if request.method == "GET":

        context = {
            'design': design,

        }
        return render(request, 'designs/design_delete.html', context)
    else:

        design.delete()
        return redirect('list designs')


@login_required
@required_user(model=Designs)
def edit_design(request, pk):
    design = Designs.objects.get(pk=pk)
    if request.method == "GET":
        form = CreateDesignForm(instance=design)
        context = {
            'design': design,
            'form': form
        }
        return render(request, 'designs/design_edit.html', context)
    else:

        old_image = design.image
        old_image_floor_one = design.image_floor_one
        old_image_floor_two = design.image_floor_two
        form = CreateDesignForm(request.POST, request.FILES, instance=design)
        if form.is_valid():
            # When  chаnge your images, delete the old images from media
            if old_image:
                cleaned_up_files(old_image.path)
            if old_image_floor_one:
                cleaned_up_files(old_image_floor_one)
            if old_image_floor_two:
                cleaned_up_files(old_image_floor_two)
            form.save()
            return redirect('list designs')
        context = {
            'design': design,
            'form': form
        }
        return render(request, 'designs/design_edit.html', context)
