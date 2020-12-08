from django.shortcuts import render

# Create your views here.
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

            # 'can_delete': design.created_by_id == request.user.id,
            # 'can_edit': design.created_by_id == request.user.id,

            # 'can_comment': design.created_by_id != request.user.id,
        }

        return render(request, 'designs/design_details.html', context)
