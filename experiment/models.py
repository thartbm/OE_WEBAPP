from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.urlresolvers import reverse
import os


def experiment_directory_path(instance, filename):
    """ Returns the directory path to the experiment folder"""
    return os.path.join(instance.experiment.home_directory, "{0}".format(filename))
    
class Experiment(models.Model):
    """
    Builds the experiment model that will store javascript code to display to their corresponding experiment page.
    """
    date_uploaded = models.DateTimeField(_('date uploaded'), default=timezone.now) 
    name = models.CharField(_("Experiment Name"), unique=True, max_length=100, null=False, blank = False)
# #file = models.FileField(upload_to=user_directory_path, null=True, blank=True) #May not need this...
    js_Code = models.TextField(_("JS Experiment Code"), blank=True, null=True)
    js_Code_Header = models.TextField(_("JS Header Code"), blank=True, null=True) # The JS code entered in the header of the HTML
    is_Published = models.BooleanField(_("Published"), default=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    created_By = models.CharField(max_length=50)
    home_directory = models.CharField(max_length=150)
    query = models.CharField(max_length=1000)
    # in a way having the table creation is redundant because what was needed is 
    # to build tables based on final experiment, tables may be created differently
    # from the beginning of the experiment to end...
    # in a way I could have just initialized a model when exp. is created.
     
     
    def __str__(self):
        """
            Returns the name of the experiment in string
        """    
        return self.name
    
    def get_absolute_url(self):
        return reverse("experiment:exp_detail", kwargs={'pk':self.pk})
     
# class Question(models.Model):
#     """
#         The model that holds each question of the form used by each experiment
#     """
#     question = models.CharField(max_length=128)
#     experiment = models.ManyToManyField(Experiment)
# 
# class Answer(models.Model):
#     """
#         The model that holds the answers related to the questions
#     """
#     question = models.ForeignKey(Question)
#     answer = models.CharField(max_length=20)
    
    
class Attachment(models.Model):
    experiment = models.ForeignKey(Experiment, verbose_name=_('Experiment'))
    file = models.FileField(_('Attachment'), upload_to=experiment_directory_path, null=False)
    
    def __str__(self):
        """
        Returns the name of the experiment in string
        """    
        return self.filename()
    
    def filename(self):
        return os.path.basename(self.file.name)
    
    def fullDelete(self):
        storage = self.file.storage
        path = self.file.path
        storage.delete(path) #delete file from disk
    
def display_text_file(self):
    self.open() # reset the pointer of file, needs if you need to read file more than once, in a request.
    return self.read().replace('\n', '<br>')


# The reason for including a trial class is to better handle the anonymous users, and maybe regular users as well.
# Every experiment shall hold the table name
class Trial(models.Model):
    anon_user = models.CharField(null=False, max_length=50, blank=False)
    experiment = models.ForeignKey(Experiment) 
    #participant = models.ForeignKey(settings.AUTH_USER_MODEL)
    table_name = models.CharField(null=False, max_length=50, blank=False) #is 50 too big?
    trial_number = models.PositiveIntegerField(default=0)
    date_of_trial = models.DateTimeField(_('date uploaded'), default=timezone.now) 
    
    class Meta():
        index_together = [['table_name']]
   
    def save(self, *args, **kwargs):
        self.trial_number = self.trial_number + 1
        return super(Trial, self).save(*args, **kwargs)
    
# class Data(models.Model):
#     trial = models.ForeignKey(Trial) 
#     DATA_CHOICES = (
#         ('FLO', 'Float'),
#         ('INT', 'Integer' ),
#         ('CHAR', 'Chars'), # characters up to 255
#         ('STR', 'String'), # characters larger than 255
#         ('DAT', 'Date'),
#         ('BOOL', 'Boolean'),
#         ('DUR', 'Duration'),
#         )
#     dataType = models.CharField(_('Data Type'), max_length = 5,choices=DATA_CHOICES, blank='false')
#     
#     class Meta:
#         abstract = True
#         
# class IntData(Data):
#     value = models.IntegerField(_('Data Value'), blank='false')
#     
# class FloatData(Data):
#     value = models.FloatField(_('Data Value'), blank='false')
#     
# class CharsData(Data):
#     value = models.CharField(_('Data Value'), max_length=255, blank='false')
#     
# class StrData(Data):
#     value = models.TextField(_('Data Value'), blank='false')    
#     
# class DateData(Data):
#     value = models.DateField(_('Data Value'), blank='false')    
# 
# class BooleanData(Data):
#     value = models.BooleanField(_('Data Value'), blank='false')  
# 
# class DurationData(Data):
#     value = models.DurationField(_('Data Value'), blank='false')  


         
     
