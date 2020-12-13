from django.http import HttpResponse


def required_user(model):
    def decorator(view_function):
        def wrapper(request, *args, **kwargs):
            if model.created_by_id != request.user.id:
                return HttpResponse('Access Denied!')
            else:
                return view_function(request, *args, **kwargs)
        return wrapper
    return decorator
