from django.core.exceptions import PermissionDenied



# def required_user(model):
#     def decorator(view_function):
#         def wrapper(request, *args, **kwargs):
#             entry_model = model.objects.get(pk=kwargs['pk'])
#             if entry_model.created_by_id != request.user.id:
#                 return HttpResponse('Access Denied!')
#             else:
#                 return view_function(request, *args, **kwargs)
#         return wrapper
#     return decorator


from designs.models import Designs


def user_is_entry_author(function):
    def wrapper(request, *args, **kwargs):
        design = Designs.objects.get(pk=kwargs['pk'])
        if design.created_by == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrapper
