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
                          %escape(value)
                        )
        return mark_safe('<center>%s</center>'
                      %escape(value)
                    )

class TrackerTable(tables.Table):
    study_name = tables.Column()
    tissue = tables.Column()
    link = GlyphColumn()
    cbio_link = GlyphColumn()
    adult_or_pediatric = tables.Column()
    details = tables.Column()
    trackerID = tables.TemplateColumn ('{{ record.trackerID }}')

    tr_class=tables.Column(visible=False, empty_values=())
    def render_tr_class(self, value):
        if value == 'trackerID':
            return 'highlight'

    class Meta:
        model = Tracker
        exclude =("uuid", "id", "time", "requester_name", "email", "accession", "details", "trackerID", "priority", "confirmation", "subscription", "summary")
        orderable = True
        attrs = {"class": "paleblue"}
