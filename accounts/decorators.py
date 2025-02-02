from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def user_type_required(allowed_types):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped(request, *args, **kwargs):
            if request.user.user_type not in allowed_types:
                messages.error(request, "Access denied. Invalid user type.")
                return redirect('accounts:dashboard')
            return view_func(request, *args, **kwargs)
        return wrapped
    return decorator