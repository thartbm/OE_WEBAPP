from django.http import JsonResponse
#Removed the usage of it, doesn't affect code if deleted
class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    
#     def render_to_json_response(self, context, **response_kwargs):
#         print("context = " + context)
#         data = json.dumps(context)
#         response_kwargs['content_type'] = 'application/json'
#         return HttpResponse(data, **response_kwargs)
    
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response
 
    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        print(form.cleaned_data)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response  