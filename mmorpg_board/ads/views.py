from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .forms import AdForm
from django.core.paginator import Paginator

class AdListView(ListView):
    model = Ad
    template_name = 'ads/ad_list.html'
    context_object_name = 'ads'
    paginate_by = 10

class AdCreateView(LoginRequiredMixin, CreateView):
    model = Ad
    form_class = AdForm
    template_name = 'ads/ad_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)