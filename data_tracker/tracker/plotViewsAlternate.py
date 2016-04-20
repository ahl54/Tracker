'''		
### render multiple charts per page
class PlotView(TemplateView):

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
        data['unique_aop'] = list(Tracker.objects.values_list('adult_or_pediatric', flat=True).distinct())
        data['unique_access'] = list(Tracker.objects.values_list('access', flat=True).distinct())
        data['unique_details'] = list(Tracker.objects.values_list('details', flat=True).distinct())

		# y-axis counts of frequencies per values
        data['count_tissue'] = Tracker.objects.values_list('tissue').annotate(tissue_count=Count('tissue'))
        data['count_aop'] = Tracker.objects.values_list('adult_or_pediatric').annotate(tissue_count=Count('adult_or_pediatric'))
        data['count_access'] = Tracker.objects.values_list('access').annotate(tissue_count=Count('access'))
        data['count_details'] = Tracker.objects.values_list('details').annotate(tissue_count=Count('details'))
			
        return data

    def plot(request, chartID = 'chartID', chart_type = 'line', chart_height = 500):
        data = PlotView.tracker_data()

        chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}  
        title = {"text": 'Tissue Distribution'}
        xAxis = {"title": {"text": 'Tissues'}, "categories": data['unique_tissue']}
        yAxis = {"title": {"text": 'Data'}}
        series = [
            {"name": 'Tissue', "data": data['count_tissue']}, 
            ]

        return render(request, 'data_plot.html', {'chartID': chartID, 'chart': chart,
														'series': series, 'title': title, 
														'xAxis': xAxis, 'yAxis': yAxis})
			
'''			
'''		
    def plot(request, chartID = 'chartID', chart_type = 'line', chart_height = 500):
        data = tracker_data()

        chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}  
        title = {"text": 'tissue Distribution'}
        xAxis = {"title": {"text": 'Serial Number'}, "categories": data['unique_tissue']}
        yAxis = {"title": {"text": 'Data'}}
        series = [
            {"name": 'tissue', "data": data['count_tissue']}, 
            ]

        return render(request, 'data_plot.html', {'chartID': chartID, 'chart': chart,
                                                    'series': series, 'title': title, 
                                                    'xAxis': xAxis, 'yAxis': yAxis})
'''


	
'''	
    def tissueChart(request, chartID = 'ChartID', chart_type = 'column', chart_height = 500):
	
		#renderTo is throwing a WSGIRequest error
        tissue_chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
			
        tissue_title = {"text": 'Tissue Distribution'}
		
        tissue_xAxis = {"categories": data['unique_tissue']} #distinct categories
        tissue_yAxis = {"title": {"text": 'count'}} #frequency per category
		
        tissue_plotOptions = {"column": {"groupPadding": '0', "pointPadding": '0', "borderWidth": '0'}}
		
        tissue_config = {"credits": {"enabled": 'false'}}

        tissue_series = [{"showInLegend": 'false', 
			"name": 'tissue', "data": data['count_tissue']}, 
			]
			
        results = {'ChartID': chartID, 'tissue_chart': chartID,
				   'tissue_series': series, 'tissue_title': title, 
				   'tissue_xAxis': xAxis, 'tissue_yAxis': yAxis, 
				   'tissue_plotOptions': plotOptions, 'tissue_config': config}		
		
        return (request, 'data_plot.html', results)
	
    def detailChart(request, chartID = 'detailChart', chart_type = 'column', chart_height = 500):
        chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
			
        title = {"text": 'Study Type Distribution'}
		
        xAxis = {"categories": data['unique_detail']} #distinct categories
        yAxis = {"title": {"text": 'count'}} #frequency per category
		
        plotOptions = {"column": {"groupPadding": '0', "pointPadding": '0', "borderWidth": '0'}}
		
        config = {"credits": {"enabled": 'false'}}

        series = [{"showInLegend": 'false', 
			"name": 'detail', "data": data['count_detail']}, 
			]
			
        results = {'detailChart': chartID, 'chart': chart,
				   'series': series, 'title': title, 
				   'xAxis': xAxis, 'yAxis': yAxis, 
				   'plotOptions': plotOptions, 'config': config}		
		
        return results

    def aopChart(data, chartID = 'aopChart', chart_type = 'column', chart_height = 500):
        chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
			
        title = {"text": 'Adult vs Pediatric Distribution'}
		
        xAxis = {"categories": data['unique_aop']} #distinct categories
        yAxis = {"title": {"text": 'count'}} #frequency per category
		
        plotOptions = {"column": {"groupPadding": '0', "pointPadding": '0', "borderWidth": '0'}}
		
        config = {"credits": {"enabled": 'false'}}

        series = [{"showInLegend": 'false', 
			"name": 'aop', "data": data['count_aop']}, 
			]
			
        results = {'aopChart': chartID, 'chart': chart,
				   'series': series, 'title': title, 
				   'xAxis': xAxis, 'yAxis': yAxis, 
				   'plotOptions': plotOptions, 'config': config}		
		
        return results
		
    def accessChart(chartID = 'accessChart', chart_type = 'column', chart_height = 500):
        chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
			
        title = {"text": 'Access Distribution'}
		
        xAxis = {"categories": data['unique_access']} #distinct categories
        yAxis = {"title": {"text": 'count'}} #frequency per category
		
        plotOptions = {"column": {"groupPadding": '0', "pointPadding": '0', "borderWidth": '0'}}
		
        config = {"credits": {"enabled": 'false'}}

        series = [{"showInLegend": 'false', 
			"name": 'access', "data": data['access_detail']}, 
			]
			
        results = {'accessChart': chartID, 'chart': chart,
				   'series': series, 'title': title, 
				   'xAxis': xAxis, 'yAxis': yAxis, 
				   'plotOptions': plotOptions, 'config': config}		
		
        return results

    #def plot(request):
	
        result_tissue = tissueChart(request)
        result_details = detailsChart(request)
        result_aop = aopChart(request)
        result_access = accessChart(request)
	
        results = result_tissue
		
		#TO DO find what the contents of results are and why they aren't valid template tags
		#check json.dump()
		#check if results are formatted incorrectly (python 'u list vs json list)
		#try the django debug toolbar to step through your variables
		#comment it all out and try it again a different way
		
        return render(request, 'data_plot.html', results)
	
    def get_context_data(self, **kwargs):
        ctx = super(PlotView, self).get_context_data(**kwargs)
        ctx['ctx'] = ctx
        return ctx
		
		#{'view': <tracker.views.PlotView object at 0x03C33FF0>, 'ctx': {...}}
'''				