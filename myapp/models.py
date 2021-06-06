from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CHOICE_CLASS = (
  ('1AC', 'Air-conditioned First class'),
  ('2AC', 'Air conditioned 2-tier'),
  ('3AC', 'Air conditioned 3-tier'),
  ('CC', 'AC- Chair Class'),
  ('SL', 'Sleeper Class'),
  )
  
class Train(models.Model):
  train_no = models.PositiveIntegerField()
  train_name = models.CharField(max_length=100)
  train_from = models.CharField(max_length=100)
  train_to = models.CharField(max_length=70)
  total_seats = models.PositiveIntegerField()
  available_seats = models.PositiveIntegerField()
  #seat_no = models.PositiveIntegerField(default=1)
  train_price = models.PositiveIntegerField()
  train_category = models.CharField(choices=CHOICE_CLASS, max_length=70)
  running_days = models.CharField(max_length=70)
  time_taken = models.CharField(max_length=70)
  
  def __str__(self):
    return str(self.id)
    
class BookTicket(models.Model):
  train = models.ForeignKey(Train, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)
  
  def __str__(self):
    return str(self.id)