from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Response
from django_filters.views import FilterView

class UserResponsesView(LoginRequiredMixin, ListView):
    model = Response
    template_name = 'responses/user_responses.html'
    filterset_class = ResponseFilter
    context_object_name = 'responses'

    def get_queryset(self):
        return Response.objects.filter(ad__author=self.request.user)

