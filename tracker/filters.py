import django_filters
from tracker.models import Tracker

class TrackerFilter(django_filters.FilterSet):
    study_name = django_filters.CharFilter(lookup_type='contains')
    tissue = django_filters.CharFilter(lookup_type='contains')
    adult_or_pediatric = django_filters.CharFilter(lookup_type='contains')
    access = django_filters.CharFilter(lookup_type='contains')
    details = django_filters.CharFilter(lookup_type='contains')

    class Meta:
        model = Tracker
        fields = ['study_name', 'tissue', 'adult_or_pediatric', 'access', 'details']
        exclude =("id", "time", "requester_name", "email","accession","source","link","samples", "adult_or_pediatric", "citation", "priority", "trackerID")
        orderable = True
        attrs = {"class": "paleblue"}

