from django.db import models
from django import forms
from django.forms import MultiValueField, CharField
from django.core import validators
from django.core.validators import RegexValidator
from django.core.validators import validate_email
import django_tables2 as tables
from django_filters import ChoiceFilter
from django.utils.safestring import mark_safe
from django.utils.html import escape
from datetime import datetime

#TO DO: Form defaults within text area
#TO DO: Form verification in-line error messages	
#TO DO: implement uniqueID associated with each request, implement tracking search bar
#TO DO: display progress bars within same view as table
#TO DO: Automatic email message subscription, sends notification once available

# Create your models here.

	
#CHOICE FIELD DEFINITIONS

AGE_CHOICES = (
	('Unknown', 'Unknown'),
	('Adult', 'Adult'),
	('Pediatric', 'Pediatric'),
	('Both', 'Both'),
)
					  
ACCESS_CHOICES = (
    (0, 'Unknown'),
    (1, 'Open'),
    (2, 'Restricted'),
)

TRACKERID_CHOICES = (
    ('Requested', 'Requested'),
    ('Staged', 'Staged'),
    ('Database', 'Database'),
    ('Application', 'Application'),
)	


	#uniqueID = models.IntegerField()								  
class Tracker(models.Model):
    time = models.DateTimeField(default=datetime.now, blank=True)
    requester_name = models.CharField(max_length=3000)
    email = models.EmailField(max_length=254)
    accession = models.CharField(max_length=200)
    study_name = models.CharField(max_length=3000)
    source = models.CharField(max_length=3000)
    link = models.URLField(max_length=3000)
    samples = models.IntegerField()
    tissue = models.CharField(max_length=3000)
    adult_or_pediatric = models.CharField(max_length=7, choices=AGE_CHOICES, default=0)
    citation = models.CharField(max_length=3000)
    PMID = models.IntegerField()    
    details = models.CharField(max_length=3000)
    access = models.CharField(max_length=10, choices=ACCESS_CHOICES, default=0)
    priority = models.IntegerField(default=0)
    trackerID = models.IntegerField(default=0)
    #progress = models.CharField(max_length=11, choices=TRACKERID_CHOICES, default=0)


#TO DO: Display progress by color code
class ProgressColumn(tables.Column):
		
    def render_progress(self, value, record):
        if self.record == '3':
            self.attrs ={"td": {"color": "DeepSkyBlue"}}
            #self.attrs = {"class": "color_" + value}
        elif self.record == '2':
            self.attrs ={"td": {"color": "SandyBrown"}}
            #self.attrs = {"class": "color_" + value}
        elif self.record == '1':
            self.attrs ={"td": {"color": "Red"}}
            #self.attrs = {"class": "color_" + value}
        else:
            self.attrs ={"td": {"color": "Blue"}}	
            #self.attrs = {"class": "color_" + value}
        return value


# if (objects.status = 0):
	# return render(value + 'Requested')
# elif (objects.trackerID = 1):
	# return render(value + 'Staged')
# elif (objects.trackerID = 2):
	# return render(value + 'Database')
# else:
	# return render(value + 'Available')

				
        #return "<div class='progress-bar' role='progressbar' style='width:50%'>Staging Area</div>"
        ##return render(mark_safe(value + '<progress value="10" max="100"></progress>'))
        #return mark_safe("<div class='progress-bar' role='progressbar' style='width:50%'>Staging Area</div>" % escape(value))
        #return mark_safe("<div class='progress-bar' role='progressbar' style='width:50%'><p>{{ obj.study_name }} in staging area</p></div>")
     #render_progress.allow_tags = True		

# TODO filtering function needs reset
import django_filters

class TrackerFilter(django_filters.FilterSet):
    adult_or_pediatric = ChoiceFilter(choices=AGE_CHOICES)
    access = ChoiceFilter(choices=ACCESS_CHOICES)
    trackerID = ChoiceFilter(choices=TRACKERID_CHOICES)
	
    class Meta:
        model = Tracker
        fields = ['tissue', 'adult_or_pediatric', 'details', 'access', 'trackerID']
        orderable = True
        attrs = {"class": "paleblue"}
