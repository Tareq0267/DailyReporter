from django.urls import path
from . import views
from .views import ClusterListView, AreaListView, EquipmentListView, UserListView, VibrationalReadingListView, DailyReportListView, OverallProgressListView, ManhourListView, DailyReportDetailView, DailyProgressDetailView

urlpatterns = [
    path('cluster/', ClusterListView.as_view()),
    path('area/', AreaListView.as_view()),
    path('equipment/', EquipmentListView.as_view()),
    path('user/', UserListView.as_view()),
    path('vibrational_reading/', VibrationalReadingListView.as_view()),
    path('daily_reports/', DailyReportListView.as_view()),
    path('overall_progress/', OverallProgressListView.as_view()),
    path('manhour/', ManhourListView.as_view()),
    path('daily_report/<int:pk>/', DailyReportDetailView.as_view()),
    path('daily_progress/<int:pk>/', DailyProgressDetailView.as_view()),
]