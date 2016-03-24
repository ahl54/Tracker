import django_tables2 as tables
from django_tables2.columns import TemplateColumn
from tracker.models import Tracker
from django.utils.safestring import mark_safe
from django.utils.html import escape


# Custom rendering for images to replace links
class GlyphColumn(tables.Column):
    def render(self, value):
        if value != '-':
            return mark_safe('<center><a href=%s><span class="glyphicon glyphicon-share-alt"></span></a></center>'
                          %escape(value.lower())
                        )
        return mark_safe('<center>%s</center>'
                      %escape(value.lower())
                    )

class TrackerTable(tables.Table):
    dataset_name = tables.Column()
    description = tables.Column()
    cancer_type = tables.Column()
    study_link = GlyphColumn()
    cbio_link = GlyphColumn()
    s3_link = GlyphColumn()
    adult_or_pediatric = tables.Column()
    details = tables.Column()
    trackerID = tables.TemplateColumn ('{{ record.trackerID }}')

    tr_class=tables.Column(visible=False, empty_values=())
    def render_tr_class(self, value):
        if value == 'trackerID':
            return 'highlight'

    class Meta:
        model = Tracker
        exclude =("dataset_name", "uuid", "id", "time", "requester_name", "email", "accession", "details", "trackerID", "PMID", "citation", "priority", "confirmation", "subscription", "summary", "s3_link", "endpt", "level", "technology", "vendor")
        orderable = True
        attrs = {"class": "paleblue"}
