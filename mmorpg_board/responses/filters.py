import django_filters
from .models import Response

class ResponseFilter(django_filters.FilterSet):
    ad = django_filters.ModelChoiceFilter(
        queryset=lambda request: Ad.objects.filter(author=request.user),
        label='Объявление'
    )

    class Meta:
        model = Response
        fields = ['ad']