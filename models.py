from django.jb import models

class Topic(models.Model):
  
  text = models.CharField(max_length = 200)
  date_added = models.DateTimeField(auto_now_add = True)
  
def _str_(self):
  
  return self.text
