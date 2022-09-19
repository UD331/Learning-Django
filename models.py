from django.jb import models

class Topic(models.Model):
  
  text = models.CharField(max_length = 200)
  date_added = models.DateTimeField(auto_now_add = True)
  
 class Entry(models.Model): 
  
  topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
  text = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    verbose_name_plural = 'entries'
 
  def _str_(self):
  
    return self.text[:50] + "..."
