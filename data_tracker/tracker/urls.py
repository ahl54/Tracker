from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from tracker import views
from tracker.filters import TrackerFilter
from tracker.models import Tracker
from tracker.tables import TrackerTable
from tracker.views import FilteredSingleTableView #, PlotView

urlpatterns = [
	url(r'^$', views.index, name = 'home'),
	url(r'^tracker/$', views.tracker, name = 'tracker'),
	url(r'^request/$', views.request, name = 'request'),
	url(r'^request/thanks.html/$', views.thanks, name = 'thanks'),
	url(r'^request/unsubscribe/(?P<uuid>[^/]+)/$', views.unsubscribe, name = 'unsubscribe'),
	url(r'^stats/$', views.stats, name = 'stats'),
	url(r'^about/$', views.about, name = 'about'),
	url(r'^login/$', views.login, name = 'login'),
	url(r'^login_valid.html/$', views.login_valid, name = 'login_valid'),
	url(r'^login_invalid.html/$', views.login_invalid, name = 'login_invalid'),
	url(r'^login_disabled.html/$', views.login_disabled, name = 'login_disabled'),
	url(r'^register/base_internal.html/$', views.base_internal, name = 'base_internal'),
	url(r'^logout/$', views.logout, name = 'logout'),
	url(r'^register/$', views.register, name = 'register'),
	url(r'^manage/$', views.manage, name = 'manage'),
	url(r'^loading/$', views.loading, name = 'loading'),
	url(r'^rawlist/$', views.rawlist, name='rawlist'),
	url(r'^staginglist/$', views.staginglist, name='staginglist'),
	url(r'^table/$', FilteredSingleTableView.as_view(
            model=Tracker,
            table_class=TrackerTable,
            template_name='table.html',
            filter_class=TrackerFilter
    ), name='filtered_view'
    ),
]
