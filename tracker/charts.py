from tracker.models import Tracker
from django.db.models import Count
'''
class Charts(Plot):
    class ChartData():    
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


    data = ChartData.tracker_data()

    def tissueChart(request, chartID = 'tissueChart', chart_type = 'column', chart_height = 500):
	
		#renderTo is throwing a WSGIRequest error
        chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
			
        title = {"text": 'Tissue Distribution'}
		
        xAxis = {"categories": data['unique_tissue']} #distinct categories
        yAxis = {"title": {"text": 'count'}} #frequency per category
		
        plotOptions = {"column": {"groupPadding": '0', "pointPadding": '0', "borderWidth": '0'}}
		
        config = {"credits": {"enabled": 'false'}}

        series = [{"showInLegend": 'false', 
			"name": 'tissue', "data": data['count_tissue']}, 
			]
			
        results = {'chartID': chartID, 'chart': chart,
				   'series': series, 'title': title, 
				   'xAxis': xAxis, 'yAxis': yAxis, 
				   'plotOptions': plotOptions, 'config': config}		
		
        return results
		
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
			
        results = {'chartID': chartID, 'chart': chart,
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
			
        results = {'chartID': chartID, 'chart': chart,
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
			
        results = {'chartID': chartID, 'chart': chart,
				   'series': series, 'title': title, 
				   'xAxis': xAxis, 'yAxis': yAxis, 
				   'plotOptions': plotOptions, 'config': config}		
		
        return results

'''