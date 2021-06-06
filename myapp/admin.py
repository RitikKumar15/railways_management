from django.contrib import admin
from .models import Train, BookTicket

# Register your models here.
@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
  list_display = ['id', 'train_no', 'train_name', 'train_from', 'train_to', 'total_seats', 'available_seats', 'train_price', 'train_category', 'running_days', 'time_taken']

@admin.register(BookTicket)
class BookTicketAdmin(admin.ModelAdmin):
  list_display = ['id', 'train', 'user', 'quantity']