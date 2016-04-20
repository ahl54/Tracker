import django_filters
from tracker.models import Tracker

class TrackerFilter(django_filters.FilterSet):
    #dataset_name = django_filters.CharFilter(lookup_type='contains')
    cancer_type = django_filters.CharFilter(lookup_type='contains')
    adult_or_pediatric = django_filters.CharFilter(lookup_type='contains')
    access = django_filters.CharFilter(lookup_type='contains')
    details = django_filters.CharFilter(lookup_type='contains')
    accession = django_filters.CharFilter(lookup_type='contains')

    class Meta:
        model = Tracker
        fields = ['cancer_type', 'adult_or_pediatric', 'access', 'details', 'accession', "source"]
        exclude =("id", "time", "requester_name", "email", "study_link", "cbiolink", "s3_link", "samples", "adult_or_pediatric", "citation", "priority", "trackerID")
        orderable = True
        attrs = {"class": "paleblue"}
