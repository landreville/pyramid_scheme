
def form_value(request, entity, attribute):
    """
    Return value from request params or the given entity.

    :param request: Pyramid request.
    :param entity: Instance to get attribute from if it isn't found in the request
        params.
    :param str attribute: Name of attribute to search for in the request params or
        on as an attribute of the given entity.
    """
    # Check for contains, because we want the request value even if it's empty
    if attribute in request.params:
        return request.params.get(attribute, '')
    if entity:
        # Don't provide a default value, because we want to make attribute typos clear
        return getattr(entity, attribute)
    return ''
