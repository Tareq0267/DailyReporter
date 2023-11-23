from django.utils import timezone
from django.db import models
from django.db.models import Sum

class Cluster(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=255)
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Equipment(models.Model):
    name = models.CharField(max_length=255)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    is_running = models.BooleanField(default=True)

    def __str__(self):
        return self.name+' - '+self.area.name

class User(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE, null=True, blank=True)
    is_approver = models.BooleanField(default=False)

    def __str__(self):
        if self.cluster is None:
            return self.name+' - '+self.title
        else:
            return self.name+' - '+self.title+' ['+self.cluster.__str__()+']'
        

class VibrationalReading(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    remark = models.TextField()
    category = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    reading = models.FloatField(null=True, blank=True)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.equipment.name+' - '+self.category

class DailyReport(models.Model):
    vibrational_reading = models.ManyToManyField(VibrationalReading, null=True, blank=True, related_name='vibrational_reading')
    #HSE = models.IntegerField()  # Assuming HSE_id is an integer, adjust if it's a foreign key or different type
    prepared_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='prepared_reports')
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='reviewed_reports')
    #overall_progress_id = models.ForeignKey('OverallProgress', on_delete=models.SET_NULL, null=True,blank=True)  # Adjust if it's a foreign key
    report_no = models.CharField(max_length=255)
    date_time = models.DateTimeField(default=timezone.now)
    todays_activity = models.TextField()
    remarks = models.TextField()
    is_approved = models.BooleanField(default=False)
    is_submitted = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

    def __str__(self):
        return self.report_no+' - '+self.date_time.__str__()
    
class OverallProgress(models.Model):
    daily_update = models.ManyToManyField('DailyUpdate', verbose_name="daily_update")
    daily_report = models.ManyToManyField(DailyReport, verbose_name="daily_report")
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    

    def __str__(self):
        return self.month.__str__()+" - "+self.year.__str__()
        

class DailyUpdate(models.Model):
    day = models.IntegerField(blank=True, null=True)
    week = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    planning = models.IntegerField(blank=True, null=True)
    cumulative_planning = models.IntegerField(blank=True, null=True)
    percent_planning = models.FloatField(blank=True, null=True)
    actual = models.IntegerField(blank=True, null=True)
    proactive = models.IntegerField(blank=True, null=True)
    cumulative_actual = models.IntegerField(blank=True, null=True)
    percent_actual = models.FloatField(blank=True, null=True)
    equipment_visited = models.IntegerField(blank=True, null=True)
    cumulative_equipment_visited = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.date.__str__()
    
    def get_overall_progress(self):
        return self.overallprogress_set.all().get(month = self.date.month, year = self.date.year)
    
    def get_all_daily_updates(self):
        return self.get_overall_progress().daily_update.all().order_by('date')
    
    def get_cumulative_planning(self):
        return self.get_all_daily_updates().filter(date__lte = self.date).aggregate(Sum('planning'))['planning__sum']
        
    def get_planning_percentage(self):
        return self.planning/(self.get_all_daily_updates().last().get_cumulative_planning())*100
    
    def get_cumulative_actual(self):
        return self.get_all_daily_updates().filter(date__lte = self.date).aggregate(Sum('actual'))['actual__sum']

    def get_actual_percentage(self):
        return self.actual/(self.get_all_daily_updates().last().get_cumulative_actual())*100
    
    def get_cumulative_equipment_visited(self):
        return self.get_all_daily_updates().filter(date__lte = self.date).aggregate(Sum('equipment_visited'))['equipment_visited__sum']


    
class HSE(models.Model):
    daily_report = models.ForeignKey(DailyReport, on_delete=models.CASCADE)
    HSE_id = models.IntegerField()
    LTI = models.IntegerField()
    RWC = models.IntegerField()
    MTC = models.IntegerField()
    TRC = models.IntegerField()
    FAC = models.IntegerField()
    Highlights = models.TextField()

    def __str__(self):
        return self.HSE_id.__str__()+" - "+self.daily_report.report_no.__str__()+' - '+self.daily_report.date_time.__str__()+' - '

class Manhour(models.Model):
    daily_report = models.ForeignKey(DailyReport, on_delete=models.CASCADE)
    manpower = models.CharField(max_length=255)
    manhours = models.IntegerField()
    contractor = models.CharField(max_length=255)
    total_LTI = models.IntegerField()  # Assuming total_LTI is an integer, adjust if different

    def __str__(self):
        return self.daily_report.report_no+' - '+self.daily_report.date_time.__str__()+' - '+self.manpower

# Note: Adjust the field types and options according to the actual data types and constraints required.
