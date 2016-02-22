import django_tables2 as tables
from django_tables2.columns import TemplateColumn
from tracker.models import Tracker, ProgressColumn

class TrackerTable(tables.Table):
    study_name = tables.Column()
    tissue = tables.Column()
    adult_or_pediatric = tables.Column()
    details = tables.Column()
    #trackerID = tables.TemplateColumn ('{{ record.trackerID }}')
	#trackerID = tables.TemplateColumn('attrs={"id": "color_" + {{ record.trackerID }}}')
    trackerID = ProgressColumn()
	
    tr_class=tables.Column(visible=False, empty_values=())
    def render_tr_class(self, value):
        if value == 'trackerID':
            return 'highlight'
	
    class Meta:
        model = Tracker
        exclude =("id", "time", "requester_name", "email","accession","source","link","samples", "adult_or_pediatric", "PMID", "citation", "priority", "access")
        orderable = True
        attrs = {"class": "paleblue"}