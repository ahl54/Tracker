# model imports
from django.shortcuts import render_to_response, render
from django.template import RequestContext, context, loader
from django.views.generic import TemplateView
from django.http import Http404,HttpResponseRedirect, HttpResponse
# summary statistics properties imports
from django.utils import timezone
from django.db.models import Count
from collections import Counter
# form imports
from .forms import TrackerForm, LoginForm, RegisterForm, TrackerUserCreationForm
from tracker.models import Tracker, TrackerFilter
from django_tables2 import RequestConfig
# filter imports
from crispy_forms.bootstrap import PrependedAppendedText, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button
from django_tables2 import SingleTableView
from tracker.filters import TrackerFilter
# email and subscription imports
from django.core.mail import send_mail
from django.contrib.auth.models import User, Group
# login authenication
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.handlers.modwsgi import check_password
from django.contrib.auth.decorators import login_required
from django.conf import settings
# session
from django.contrib.sessions.models import Session
from datetime import datetime

# Views for each page are created below with functions implemented

def index(request):
    return render(request, 'tracker.html', {'base': base, 'GOOGLE_ANALYTICS_PROPERTY_ID': GOOGLE_ANALYTICS_PROPERTY_ID})

LOGIN_URL = '/login.html'
base = 'base.html'
GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-73248809-3'


def login(request):
    base = base_config(request)
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form is not None:
            email = request.POST.get('email')
            username = email
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    request.session['authenticated'] = True
                    base = base_config(request)
                    return render(request, 'login_valid.html',{'form': form, 'base': base, 'GOOGLE_ANALYTICS_PROPERTY_ID': GOOGLE_ANALYTICS_PROPERTY_ID, 'user': user})
                else:
                    return render(request, 'login_disabled.html')
            else:
                print "Invalid login details: {0}, {1}".format(username, password)
                return render(request, 'login_invalid.html', {'form': form, 'base': base, 'GOOGLE_ANALYTICS_PROPERTY_ID': GOOGLE_ANALYTICS_PROPERTY_ID})
    else:
        form = LoginForm()
        base = 'base.html'
    return render(request, 'login.html', {'form': form, 'base': base, 'GOOGLE_ANALYTICS_PROPERTY_ID': GOOGLE_ANALYTICS_PROPERTY_ID})

def login_invalid(request):
    return render(request, 'login_invalid.html')

def login_disabled(request):
    return render(request, 'login_disabled.html')

def login_valid(request):
    return render(request, 'login_valid.html')

#@login_required(redirect_field_name=LOGIN_URL)
def logout(request):
    auth.logout(request)
    request.session['authenticated'] = False
    base = base_config(request)
    return render(request, 'logout.html', {'base': base, 'GOOGLE_ANALYTICS_PROPERTY_ID': GOOGLE_ANALYTICS_PROPERTY_ID})

def register(request):
    base = base_config(request)
    if request.method == 'POST':
        form = TrackerUserCreationForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user_id = models.IntegerField(primary_key=True)
            #TODO need user_id to auto increment here
            post.save()
            registered = True
            return render(request, 'login.html',{'form': form, 'base': base, 'GOOGLE_ANALYTICS_PROPERTY_ID': GOOGLE_ANALYTICS_PROPERTY_ID})
    else:
        form = TrackerUserCreationForm()
    return render(request, 'register.html', {'form': form, 'base': base, 'GOOGLE_ANALYTICS_PROPERTY_ID': GOOGLE_ANALYTICS_PROPERTY_ID})

@login_required(redirect_field_name=LOGIN_URL)
def base_internal(request):
    return render(request, 'base_internal.html')

## TODO MEDIUM PRIORITY Create manage action view within the tabs
## Low priority view a user's specific requests
## Med priority be able to create groups, add and share functions implemented here
## Low Low priority sharing via social media

#@login_required(redirect_field_name=LOGIN_URL)
def manage(request):
    base = base_config(request)
    email=request.user
    objects = Tracker.objects.filter(email=email)
    results = {'objects': objects, 'base': base, 'GOOGLE_ANALYTICS_PROPERTY_ID': GOOGLE_ANALYTICS_PROPERTY_ID}
    return render(request, 'manage.html', results)

@login_required(redirect_field_name=LOGIN_URL)
def unsubscribe(request):
    base = 'base_internal.html'
    # if clicked onto this unique page from an unsubscribe link in an email
    # TODO write unsubscribe action to pass the uuid into url and update the model for that entry to both summary 0 and subscription 0
    return render(request, 'unsubscribe.html', {'base': base, 'GOOGLE_ANALYTICS_PROPERTY_ID': GOOGLE_ANALYTICS_PROPERTY_ID})

def stats(request):
    base = base_config(request)


    chart_data = ChartData()
    data = chart_data.tracker_data()

    total = Tracker.objects.count()
    cbio = Tracker.objects.filter(trackerID='4').count()
    cavatica = Tracker.objects.filter(trackerID='5').count()
    available = cbio + cavatica
    citations = Tracker.objects.values('citation').distinct().count()
    enroute = total - available

	### add any additional charts to generate to chart_names
    chart_names = ['tissue', 'details', 'adult_or_pediatric', 'access']
    attr_names = ['chart', 'title', 'xAxis', 'yAxis', 'plotOptions', 'credits', 'series']

	#generate variable tags for javascript mapping by concatenating chart_names to attributes
    tags = []
    for chart_name in chart_names:
        for attr in attr_names:
             tags.append(chart_name + attr)

	### this block generates highchart javascripts for charts, this is not implemented yet

    # script = ''
    # for chart_name in chart_names:
        # header = "$(document).ready(function() {\n$(" + chart_name + ").highcharts({\n"
        # script = script + header
        # for attr in attr_names:
            # content = "        " + attr + ': {{ ' + chart_name + attr + "|safe }},\n"
            # script = script + content
        # script = script + "		});\n	});" +'\n'


    results = {'base': base, "chart_names": chart_names, "attr_names": attr_names, "tags": tags, 'total': total, 'cbio': cbio, 'cavatica': cavatica, 'available': available, 'enroute': enroute, 'citations': citations}

    for chart_name in chart_names:
        chart_result = chart_data.makeChart(data, chartID = chart_name , chart_type = 'column', chart_height = 500)
        results = results.copy()
        results.update(chart_result)

    return render(request, 'stats.html', results)

def tracker(request):
    #order from most recent requests
    base = base_config(request)
    objects = Tracker.objects.all()
    results = {'objects': objects, 'base': base, 'GOOGLE_ANALYTICS_PROPERTY_ID': GOOGLE_ANALYTICS_PROPERTY_ID}
    return render(request, 'tracker.html', results)# results)

def thanks(request):

    base = base_config(request)

    # Sends a summary of the request to the admin
    email = Email()
    email.admin_confirm()

    # adds the request and their email to a subscription group
    # You must create an account to subscribe to your requests!

    ## TODO provide a separate registration form for logged in users,
    # If not registered and requesting, just put a message about link to register to be able to subscribe to trackers

    # "Please login or register to subscribe to email updates for your request."
    #email.addSubscriptions()

    # Sends an email to the requester using the latest request to check for a confirmation
    latest_obj = Tracker.objects.all().order_by('-id')[0]
    if int(latest_obj.confirmation) == 1:
        email.confirm()

    return render(request, 'thanks.html', {'base': base})

def request(request):

    base = base_config(request)
    print(base)

	# if this is a POST request we need to process the form data
    if request.method == 'POST':
    # create a form instance and populate it with data from the request:
        form = TrackerForm(request.POST)
        if form.is_valid(): # check whether it's valid:
            post = form.save(commit=False) # process the data in form.cleaned_data as required
            post.time = timezone.now()
            post.save()

            # redirect to a new URL:
            return HttpResponseRedirect('thanks.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TrackerForm()
    return render(request, 'request.html', {'form': form, 'base': base})

# TODO Low priority: Create a user_request form for users who are authenticated already
# Include group management options within an extended request form
# thus users don't have to configure or edit a request they already sent

def about(request):
    base = base_config(request)
    return render(request, 'about.html', {'base': base})

class FilteredSingleTableView(SingleTableView):
    filter_class = None

    def get_table_data(self):
        self.filter = TrackerFilter(
            self.request.GET,
            queryset=super(FilteredSingleTableView, self).get_table_data(),
        )
        self.filter.helper = FormHelper()
        self.filter.helper.form_id = 'id_filterForm'
        self.filter.helper.form_class = 'form-inline'
        self.filter.helper.form_method = 'get'
        self.filter.helper.form_tag = True

        self.filter.helper.layout = Layout(
            'tissue',
            'adult_or_pediatric',
            'details',
            'access',
            FormActions(
                Submit('submit_filter', 'Filter', css_class='btn-primary'),
                Button('clear', 'Clear', css_class='btn-sm')
            )
        )

        return self.filter

    def get_context_data(self, **kwargs):
        context = super(FilteredSingleTableView, self).get_context_data(**kwargs)
        context['filter'] = self.filter
        try:
            base = base_config(self.request)
        except:
            print(base_config(self.request))
        context['base'] = base
        #context['clear'] = self.clear # TODO filtering function needs reset
        return context

class ChartData():
    chart_name = ''
    chart_height = ''

    def tracker_data(self):
        data = {'tissue': [], 'adult_or_pediatric': [],
                'sample_type': [], 'access': []}

        objects = Tracker.objects.all()

        for entry in objects:
            data['tissue'].append(entry.tissue)
            data['adult_or_pediatric'].append(entry.adult_or_pediatric)
            data['sample_type'].append(entry.sample_type)
            data['access'].append(entry.access)
            data['tissue'] = [dat.encode('UTF-8') for dat in data['tissue']]

	# x-axis categories of distinct values
        tissue_ct = Counter([dat.encode('UTF-8') for dat in Tracker.objects.values_list('tissue', flat=True)])
        aop_ct = Counter([dat.encode('UTF-8') for dat in Tracker.objects.values_list('adult_or_pediatric', flat=True)])
        access_ct = Counter([dat.encode('UTF-8') for dat in Tracker.objects.values_list('access', flat=True)])
        details_ct = Counter([dat.encode('UTF-8') for dat in Tracker.objects.values_list('sample_type', flat=True)])


        data['unique_tissue'] = tissue_ct.keys()
        data['unique_adult_or_pediatric'] = aop_ct.keys()
        data['unique_access'] = access_ct.keys()
        data['unique_details'] = details_ct.keys()

	# y-axis counts of frequencies per values
        data['count_tissue'] = dict(tissue_ct).items()
        data['count_adult_or_pediatric'] = dict(aop_ct).items()
        data['count_access'] = dict(access_ct).items()
        data['count_details'] = dict(details_ct).items()

        return data

    def makeChart(self, data, chartID = chart_name , chart_type = 'column', chart_height = chart_height):

        chart = {"renderTo": chartID, "type": chart_type, "height": chart_height}
        title = {"text": chartID + ' distribution'}
        xAxis = {"categories": data['unique_' + chartID]}
        yAxis = {"title": {"text": 'Count'}}
        credits = {"text":''}
        plotOptions = {"column": {"groupPadding": '0', "pointPadding": '0', "borderWidth": '0'}}
        series = [
            {"showInLegend": 'false', "name": chartID, "data": data['count_' + chartID]},
        ]

        result = {chartID + 'chartID': chartID, chartID + 'chart': chart,
                  chartID +'series': series, chartID + 'title': title,
                  chartID + 'xAxis': xAxis, chartID + 'yAxis': yAxis,
                  chartID + 'plotOptions': plotOptions, chartID + 'credits': credits}

        return result

class Email():

    def admin_confirm(self):
        latest_obj = Tracker.objects.all().order_by('-id')[0]
        admin = 'cbttc.cbio@gmail.com'
        admin2 = 'lua1@email.chop.edu'

        body = 'Request Summary \n\n'
        for property, value in vars(latest_obj).iteritems():
            body = body + property + ": " + str(value) + '\n'
        body = body

        send_mail('New Request from Data Tracker', body, admin2, [admin2])

    def confirm(self):
        latest_obj = Tracker.objects.all().order_by('-id')[0]
        admin = 'cbttc.cbio@gmail.com'
        recipient = str(latest_obj.email)

        body = 'Below are details from your request. \n\n'

        for property, value in sorted(vars(latest_obj).iteritems()):
            if not(property.startswith('_')):
                body = body + property + ": " + str(value) + '\n'

        body = body + '\n'
        temp_url = '127.0.0.1:8000/tracker/request/unsubscribe' # TODO change this when you bypass the firewall
        #you need to parse uuid onto the url for a unique, one time token for the recipient to unsubscribe only once
        unsubscribe = "<a href =" + temp_url + ">Unsubscribe</a>" # TODO figure out why html_message invalidates the body of the message
        send_mail('Data Tracker Request Confirmation', body, admin, [recipient], fail_silently=False) #, html_message=unsubscribe) add the unsubscribe function when you implement the unsubscribe action

    def addSubscriptions(self):

        latest_obj = Tracker.objects.filter(trackerID = 0).order_by('-id')[0]
        subscriber = int(latest_obj.subscription)
        summary = int(latest_obj.summary)

        # check if the user exists already
        try:
            user = User.objects.get(username=name)
        except:
            try:
                user = request.user
            except:
                print("The user does not exist!")
                # You must create an account to subscribe to your requests! Please register
            #name = str(latest_obj.requester_name)
            #email = str(latest_obj.email)
            #password = str(latest_obj.password)
            # redirect to register and pass fields here
            #user = User.objects.create_user(name, email, password)
            #user.save()
            # we update their supscription for this request only
            # adds the user to  a request specific subscription

        if subscriber == 1:
            available_group = Group.objects.get(name='available')
            available_group.user_set.add(user)
            if summary == 1:
                weekly_group = Group.objects.get(name='weekly')
                weekly_group.user_set.add(user)
            elif summary == 2:
                monthly_group = Group.objects.get(name='monthly')
                monthly_group.user_set.add(user)
        elif subscriber == 2:
            step_group = Group.objects.get(name='steps')
            step_group.user_set.add(user)
            if summary == 1:
                weekly_group = Group.objects.get(name='weekly')
                weekly_group.user_set.add(user)
            elif summary == 2:
                monthly_group = Group.objects.get(name='monthly')
                monthly_group.user_set.add(user)
        else:
            if summary == 1:
                weekly_group = Group.objects.get(name='weekly')
                weekly_group.user_set.add(user)
            elif summary == 2:
                monthly_group = Group.objects.get(name='monthly')
                monthly_group.user_set.add(user)
            else:
                no_group = Group.objects.get(name='unsubscribers')
                no_group.user_set.add(user)

# Custom session configurations: authenticate flag, base flag, other sessions specific attributes here
def base_config(request):
    if 'authenticated' not in request.session:
        request.session['authenticated'] = True # set the key
    authenticated = request.session['authenticated']
    if authenticated:
        base='base_internal.html'
    else:
        base='base.html'
    return base
