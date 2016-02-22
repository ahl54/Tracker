from django.shortcuts import render_to_response, render
from django.template import RequestContext, context, loader
from django.views.generic import TemplateView
from django.db.models import Count
from django.http import Http404
from django.http import HttpResponseRedirect
from django.utils import timezone
from .forms import TrackerForm
from tracker.models import Tracker, TrackerFilter
from django_tables2 import RequestConfig

def index(request):
    return render(request, 'tracker.html')
	
def about(request):
    return render(request, 'about.html')
	
def plot(request, chartID = 'chart_ID' , chart_type = 'column', chart_height = 500): #depreciated
    # total = Tracker.objects.count()
    # available = Tracker.objects.filter(trackerID='3').count()
    # citations = Tracker.objects.values('citation').distinct().count()
    # enroute = total - available

    # data = ChartData.tracker_data()

    # chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}  
    # title = {"text": 'Tissue Distribution'}
    # xAxis = {"title": {"text": 'Tissues'}, "categories": data['unique_tissue']}
    # yAxis = {"title": {"text": 'Counts'}}
    # series = [
        # {"name": 'Tissue', "data": data['count_tissue']}, 
    # ]

    # result = {"chartID": chartID, 'chart': chart,
        # 'series': series, 'title': title, 
        # 'xAxis': xAxis, 'yAxis': yAxis, 'total': total, 'available': available, 'enroute': enroute, 'citations': citations}
	
    return render(request, 'data_plot.html', result)

def stats(request):
    data = ChartData().tracker_data() #unbound method tracker_data() must be called with ChartData instance as first agument
	
    total = Tracker.objects.count()
    available = Tracker.objects.filter(trackerID='3').count()
    citations = Tracker.objects.values('citation').distinct().count()
    enroute = total - available
	
	### add any additional charts to generate to chart_names
    chart_names = ['tissue', 'details', 'adult_or_pediatric', 'access']
    attr_names = ['chart', 'title', 'xAxis', 'yAxis', 'credits', 'plotOptions', 'series']
	
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

	
    results = {"chart_names": chart_names, "attr_names": attr_names, "tags": tags, 'total': total, 'available': available, 'enroute': enroute, 'citations': citations} #, "script" : script}

    for chart_name in chart_names:
        chart_result = ChartData.makeChart(data, chartID = chart_name , chart_type = 'column', chart_height = 500)
        results = results.copy()
        results.update(chart_result)
	
    return render(request, 'stats.html', results)																																							
	
def tracker(request):
    objects = Tracker.objects.order_by('time')
    results = {'objects': objects}
    return render(request, 'tracker.html', results)

def thanks(request):
    return render(request, 'thanks.html')

def request(request):
	# if this is a POST request we need to process the form data
    if request.method == 'POST':
    # create a form instance and populate it with data from the request:
        form = TrackerForm(request.POST)
        #request.upload_handlers.insert(0, UploadProgressSessionHandler(request))
        if form.is_valid(): # check whether it's valid:
            post = form.save(commit=False) # process the data in form.cleaned_data as required
            post.time = timezone.now()
            post.save()
            # redirect to a new URL:
            return HttpResponseRedirect('thanks.html')
			
			#TO DO: Automated email alert sent at each step
			# subcription to update

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TrackerForm()
    return render(request, 'request.html', {'form': form})

def simple_list(request):

    #table = SimpleTable(queryset.order_by("tissue"))
    #table.paginate(page=request.GET.get('page', 1), per_page=25)
    #RequestConfig(request, paginate={"per_page": 25}).configure(table)
	#RequestConfig(request).configure(table)
    #return render(request,"template.html", {'table': table, 'queryset': queryset})

	if request.method == "GET":		
		queryset = Tracker.objects.select_related().all()
		f = TrackerFilter(request.GET, queryset=queryset)
		table = SimpleTable(f.qs)
		table.paginate(page=request.GET.get('page', 1), per_page=25)
		RequestConfig(request).configure(table)
		return render(request, 'template.html', {'table': table})

	
from crispy_forms.bootstrap import PrependedAppendedText, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button
from django_tables2 import SingleTableView
from tracker.filters import TrackerFilter
import os

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
        #self.filter.helper.field_template = 'table.html'

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
		
# TO DO: filtering function needs clear/reset context
    def get_context_data(self, **kwargs):
        context = super(FilteredSingleTableView, self).get_context_data(**kwargs)
        context['filter'] = self.filter
        #context['clear'] = self.clear 
        return context

		
class ChartData():
    chart_name = ''
	
    def tracker_data():
        data = {'tissue': [], 'adult_or_pediatric': [],
                'details': [], 'access': []}
				
        objects = Tracker.objects.all()

        for entry in objects:
            data['tissue'].append(entry.tissue)
            data['adult_or_pediatric'].append(entry.adult_or_pediatric)
            data['details'].append(entry.details)
            data['access'].append(entry.access)
		
		# x-axis categories of distinct values
        data['unique_tissue'] = list(Tracker.objects.values_list('tissue', flat=True).distinct())
        data['unique_adult_or_pediatric'] = list(Tracker.objects.values_list('adult_or_pediatric', flat=True).distinct())
        data['unique_access'] = list(Tracker.objects.values_list('access', flat=True).distinct())
        data['unique_details'] = list(Tracker.objects.values_list('details', flat=True).distinct())

		# y-axis counts of frequencies per values
        data['count_tissue'] = Tracker.objects.values_list('tissue').annotate(tissue_count=Count('tissue'))
        data['count_adult_or_pediatric'] = Tracker.objects.values_list('adult_or_pediatric').annotate(tissue_count=Count('adult_or_pediatric'))
        data['count_access'] = Tracker.objects.values_list('access').annotate(tissue_count=Count('access'))
        data['count_details'] = Tracker.objects.values_list('details').annotate(tissue_count=Count('details'))
		
        return data
	
    def makeChart(data, chartID = chart_name , chart_type = 'column', chart_height = 500):
		
        chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}  
        title = {"text": chartID + ' distribution'}
        xAxis = {"categories": data['unique_' + chartID]}
        yAxis = {"title": {"text": 'Count'}}
        credits = {"text": ''}
        plotOptions = {"column": {"groupPadding": '0', "pointPadding": '0', "borderWidth": '0'}}
        series = [
            {"showInLegend": 'false', "name": chartID, "data": data['count_' + chartID]}, 
        ]

        result = {chartID + 'chartID': chartID, chartID + 'chart': chart,
                  chartID +'series': series, chartID + 'title': title, 
                  chartID + 'xAxis': xAxis, chartID + 'yAxis': yAxis,
                  chartID + 'plotOptions': plotOptions, chartID + 'credits': credits}
		
        return result