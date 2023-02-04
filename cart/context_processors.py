from .cart import Cart


def cart(request):
    return {'cart': Cart(request)}


"""
The cart context processor will be executed every time a template is rendered using Django’s
RequestContext. The cart variable will be set in the context of your templates.
"""
