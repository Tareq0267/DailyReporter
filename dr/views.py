from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Cluster, Area, Equipment, User, VibrationalReading, DailyReport, OverallProgress, Manhour

class ClusterListView(ListView):
    model = Cluster
    template_name = 'cluster_list.html'  

class AreaListView(ListView):
    model = Area
    template_name = 'area_list.html'

class EquipmentListView(ListView):
    model = Equipment
    template_name = 'equipment_list.html'

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class VibrationalReadingListView(ListView):
    model = VibrationalReading
    template_name = 'vibrational_reading_list.html'

class DailyReportListView(ListView):
    model = DailyReport
    template_name = 'daily_report_list.html'

class OverallProgressListView(ListView):
    model = OverallProgress
    template_name = 'overall_progress_list.html'

class ManhourListView(ListView):
    model = Manhour
    template_name = 'manhour_list.html'

class DailyReportDetailView(DetailView):
    model = DailyReport
    template_name = 'daily_report_detail.html'
    context_object_name = 'daily_report'

class DailyProgressDetailView(DetailView):
    model = OverallProgress
    template_name = 'overall_progress_detail.html'
    context_object_name = 'overall_progress'
    

