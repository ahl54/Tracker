from django.db import models
from django.contrib import admin
from tracker.subscribe import Subscribe
from django.forms import CharField
from django.core import validators
from django.core.validators import RegexValidator
from django.core.validators import validate_email
import django_tables2 as tables
from django_filters import ChoiceFilter
from django.utils.safestring import mark_safe
from django.utils.html import escape
from datetime import datetime
from django.utils import timezone
from django.apps import AppConfig
import uuid
from django.utils.encoding import python_2_unicode_compatible
import django_filters
from django.contrib.auth.models import Group, User, AbstractBaseUser, BaseUserManager
from s3direct.fields import S3DirectField

# Create your models here.

## CHOICE FIELD DEFINITIONS

AGE_CHOICES = (
    ('Unknown', 'Unknown'),
    ('Adult', 'Adult'),
    ('Pediatric', 'Pediatric'),
    ('Both', 'Both'),
)

ACCESS_CHOICES = (
    ('Unknown', 'Unknown'),
    ('Open', 'Open'),
    ('Restricted', 'Restricted'),
)

TRACKERID_CHOICES = (
    ('0', 'Requested'),
    ('1', 'Downloaded'),
    ('2', 'Staged'),
    ('3', 'Database'),
    ('4', 'CbioPortal'),
    ('5', 'Cavatica'),
)

CONFIRMATION_CHOICES = (
    ('0', 'None'),
    ('1', 'Email me a confirmation of my request'),
)

SUBSCRIPTION_CHOICES = (
    ('0', 'None'),
    ('1', 'Email me when my request is available'),
    ('2', 'Email me at every step along the request'),
)

SUMMARY_CHOICES = (
    ('0', 'None'),
    ('1', 'Email me a weekly summary of Data Tracker requests'),
    ('2', 'Email me a monthly summary of Data Tracker requests'),
)

# Admin defined groups here
GROUP_CHOICES = (
    ('0', 'PRIVATE'),
    ('1', 'CBTTC'),
    ('2', 'SU2C'),
    ('3', 'PNOC'),
    ('9', 'PUBLIC'),
)

LEVEL_CHOICES = (
    ('0', 'L1 Data: FASTQ'),
    ('1', 'L2 Data: VCF, BAM'),
    ('2', 'L3 Data: Processed data'),
)

ENDPT_CHOICES = (
    ('0', 'Data goes to both Cavatica and cBioPortal'),
    ('1', 'Data goes to cBioPortal only'),
    ('2', 'Data goes to Cavatica only'),
)

# Tracker model
@python_2_unicode_compatible
class Tracker(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.IntegerField(default=uuid.uuid1)
    time = models.DateTimeField(default=datetime.now)
    requester_name = models.CharField(max_length=245) #, help_text='Jane Smith')
    email = models.EmailField()
    accession = models.CharField(max_length=200, blank=True) #, help_text='EGA-0000000')
    description = models.CharField(max_length=345) #, help_text='TCGA Invasive Breast Carcinoma')
    source = models.CharField(max_length=245, blank=True) #, help_text='Childrens Hospital of Philadelpia')
    study_link = models.URLField(max_length=245, blank=True) #, help_text='https://www.cbttc.org')
    s3_link = models.URLField(max_length=245, blank=True)
    cbio_link = models.URLField(max_length=245)
    samples = models.IntegerField(default=0)
    cancer_type = models.CharField(max_length=245, blank=True) #, help_text='breast carcinoma')
    sample_type = models.CharField(max_length=245, blank=True) # patient, xenograft, cellline, germline
    adult_or_pediatric = models.CharField(max_length=50, choices=AGE_CHOICES, default='Unknown')
    PMID = models.IntegerField(null=True, blank=True) #, help_text='121326')
    citation = models.CharField(max_length=245, blank=True) #, help_text='John, et. al. Nature 2016')
    specimen_type = models.CharField(max_length=245, blank=True, help_text='tissue, cell line, or xenograft')
    details = models.CharField(max_length=245, blank=True) #, help_text='WTS, WGS, WES, RNA-Seq')
    access = models.CharField(max_length=10, choices=ACCESS_CHOICES, default='Unknown')
    priority = models.IntegerField(default=0, blank=True) #, help_text='0-none, 1-low, 2-medium, 3-high')
    trackerID = models.CharField(max_length=11, choices=TRACKERID_CHOICES, default='0')
    endpt = models.CharField(max_length=254, choices=ENDPT_CHOICES, default='0')
    group = models.CharField(max_length=245, choices=GROUP_CHOICES, default='9', help_text='PNOC, CBTTC, SU2C, PUBLIC')
    level = models.CharField(max_length=230, choices=LEVEL_CHOICES, default='0')
    confirmation = models.CharField(max_length=100, choices=CONFIRMATION_CHOICES, default='0')
    subscription = models.CharField(max_length=100, choices=SUBSCRIPTION_CHOICES, default='0')
    summary = models.CharField(max_length=100, choices=SUMMARY_CHOICES, default='0')
    # TODO auto generate dataset_name from source, cancer abbrv,
    dataset_name = models.CharField(max_length=345, blank=True)

    #link to S3 bucket to be added
    __original_trackerID = None
    __original_time = None

    def __str__(self):
        #return "{0}, {1}".format(self.dataset_name, self.L1) #join tuples using this
        return u"%s" % (self.dataset_name)

    def has_changed(instance, field):
        if not instance.pk:
            return False
        old_value = instance.__class__._default_manager.filter(pk=instance.pk).values(field).get()[field]
        return not getattr(instance, field) == old_value

    # Saves the model Tracker object original state to check for a field change signal later
    def __init__(self, *args, **kwargs):
        super(Tracker, self).__init__(*args, **kwargs)
        self.__original_trackerID = self.trackerID #for subscription implementation
        self.__original_time = self.time #for summmary implementation

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if not self.id:
            i = Tracker.objects.all().order_by('-id')[0]
            self.id = i.id+1
        if self.trackerID != self.__original_trackerID: #trackerID was updated
            #if has_changed(Tracker, trackerID) == True:
            #subscribe(self.trackerID, self.subscription)
            notify()
        super(Tracker, self).save(force_insert, force_update, *args, **kwargs)
        self.__original_trackerID = self.trackerID

    class TrackerConfig(AppConfig):
        name = 'Tracker'
        verbose_name = 'Tracker_name'

        def ready(self):
            from .forms import TrackerForm
            from .models import Tracker

    class Meta:
        app_label = 'tracker'
        ordering = ('-id', 'time', 'priority')


# Custom manager for TrackerUser
class TrackerUserManager(BaseUserManager):
    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)
    """
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email,
          is_staff=is_staff, is_active=True,
          is_superuser=is_superuser, last_login=now,
          date_joined=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
        """
class TrackerGroup(models.Model):
    """
        Group object that can be associated with tags and users on a many to many relationship
    """
    group = models.OneToOneField(Group, on_delete=models.CASCADE, related_name='group_id')
    members = models.ManyToManyField(User, through='TrackerUser')
    description = models.CharField(max_length=500, blank=True)
    #permissions = models.ManyToManyField() #TODO Implement custom permissions as a class
    access_link = models.URLField(max_length=3000, blank=True) #institute's link to data access committee

    def __unicode__(self):
        return u"%s" % (self.group) #add rest of fields here

class TrackerProject(models.Model):

    """ Project object matches projects and permissions whitelist from SBG """

    name = models.CharField(max_length=45)
    members = models.ManyToManyField(User, through='TrackerUser')

    class Meta:
            permissions = (
                ( "can_write", "Can write to project" ),
                ( "can_read", "Can read the project" ),
                ( "can_execute", "Can execute on project"),
                ( "can_copy", "Can copy to project"),
            )

    def __unicode__(self):
        return u"%s" % (self.name)

class TrackerUser(AbstractBaseUser):
    """
        An extension of Django's built-in user class to associate many to many user to group relationships
    """
    id = models.AutoField(primary_key=True)
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='tracker_TrackerUser_user_id' )
    TrackerGroup = models.ForeignKey(TrackerGroup, related_name='User')
    TrackerProject = models.ForeignKey(TrackerProject)
    User = models.ForeignKey(User)
    username = models.CharField(max_length=45)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=False, db_index=True)

    is_superuser = models.BooleanField(default=0)
    is_staff = models.BooleanField(default=0)
    is_active = models.BooleanField(default=1)

    can_write = models.BooleanField(default=0)
    can_read = models.BooleanField(default=0)
    can_execute = models.BooleanField(default=0)
    can_copy = models.BooleanField(default=0)

    date_joined = models.DateTimeField(default=datetime.now)
    # TODO Make user to groups relationship many to many to groups
    # Does this cause a circular dependency if there's already a many to many field in TrackerGroup?
    objects = TrackerUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __unicode__(self):
        return u"%s" % (self.username) #add rest of fields here

    class Meta:
        db_table = 'auth_user'

# class SubTracker(Tracker)
### Depreciated
### Create a data type (WGS, WES, RNA, Transcriptome) based "subtracker" model here
### SubTracker is an subclass of Tracker that contains
### we need to share project sub data types (make a tabbed tracker view for projects, data types)
### Consider using generated sub filter tabs to display relevant information

class Document(models.Model):
    idtracker_document = models.IntegerField(primary_key=True)
    docfile = models.FileField(upload_to='downloads/%Y_%m_%d')
    filetype = models.CharField(max_length=25)

class S3Direct(models.Model):
    docfile = S3DirectField(dest='files')

class TrackerFilter(django_filters.FilterSet):
    adult_or_pediatric = ChoiceFilter(choices=AGE_CHOICES)
    access = ChoiceFilter(choices=ACCESS_CHOICES)
    trackerID = ChoiceFilter(choices=TRACKERID_CHOICES)
    groups = ChoiceFilter(choices=GROUP_CHOICES)

    class Meta:
        model = Tracker
        fields = ['dataset_name', 'cancer_type', 'adult_or_pediatric', 'group', 'access', 'details', 'accession']
        orderable = True
        attrs = {"class": "paleblue"}

## TODO Create a class for auto generating our format from the request and annotating meta files and generating case lists
