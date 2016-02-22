from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from tracker import views
from tracker.filters import TrackerFilter
from tracker.models import Tracker
from tracker.tables import TrackerTable
from tracker.views import FilteredSingleTableView #, PlotView

urlpatterns = [
	url(r'^$', views.index, name = 'home'),
	url(r'^tracker/$', views.tracker, name = 'tracker'),
	url(r'^request/$', views.request, name = 'request'),
	url(r'^stats/$', views.stats, name = 'stats'),
	url(r'^request/thanks.html/$', views.thanks, name = 'thanks'),
	url(r'^about/$', views.about, name = 'about'),
	#this page was generated for testing matplotlib
	#url(r'^charts/$', views.simple, name = 'simple'),
	#this page was generated for testing highcharts
	#url(r'^data_plot/$', PlotView.as_view(template_name='data_plot.html'), name = 'plot'),
	#url(r'^data_plot/$', views.plot, name = 'plot'),
	#this page was generated for testing data tables without filtering
	#url(r'^template/$', views.simple_list, name = 'template'),
	url(r'^table/$', FilteredSingleTableView.as_view(
            model=Tracker,
            table_class=TrackerTable,
            template_name='table.html',
            filter_class=TrackerFilter
    ), name='filtered_view'
    ),
]

