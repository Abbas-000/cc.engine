from builtins import object
from webob.exc import HTTPNotFound, HTTPMethodNotAllowed

from cc.license import by_code

def _make_safe(decorator, original):
    """
    Copy the function data from the old function to the decorator.
    """
    decorator.__name__ = original.__name__
    decorator.__dict__ = original.__dict__
    decorator.__doc__ = original.__doc__
    return decorator


def get_license(controller):
    def new_controller_func(request, *args, **kwargs):
        license = by_code(
            request.matchdict['code'],
            jurisdiction=request.matchdict.get('jurisdiction'),
            version=request.matchdict.get('version'))
        if not license:
            return HTTPNotFound()

        return controller(request, license=license, *args, **kwargs)

    return _make_safe(new_controller_func, controller)


class RestrictHttpMethods(object):
    """
    A decorator to restrict which methods are allowed on this controller.

    EG:
      @RestrictHttpMethods('GET', 'PUT')
      def my_view(request):
    """
    def __init__(self, *allowed_methods):
        self.allowed_methods = allowed_methods

    def __call__(self, controller):
        def new_controller_func(request, *args, **kwargs):
            if request.method not in self.allowed_methods:
                return HTTPMethodNotAllowed()

            return controller(request, *args, **kwargs)

        return _make_safe(new_controller_func, controller)
