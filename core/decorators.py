from django.http import HttpResponse


def required_user(model):
    def decorator(view_function):
        def wrapper(request, *args, **kwargs):
            if model.user == request.user and model.user.is_authenticated:
                return view_function(request, *args, **kwargs)
            else:
                return HttpResponse('Access Denied!')
        return wrapper
    return decorator
