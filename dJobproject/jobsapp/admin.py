from django.contrib import admin
from jobsapp.models import Hydjobs,Punejobs,Bangalorejobs
# Register your models here.

class  HydjobsAdmin(admin.ModelAdmin):
    list_display=['date','title','eligibility','address','email','phonenumber']
    
class  PunejobsAdmin(admin.ModelAdmin):
    list_display=['date','title','eligibility','address','email','phonenumber']

class  BangalorejobsAdmin(admin.ModelAdmin):
    list_display=['date','title','eligibility','address','email','phonenumber']




admin.site.register(Hydjobs,HydjobsAdmin)
admin.site.register(Punejobs,PunejobsAdmin)
admin.site.register(Bangalorejobs,BangalorejobsAdmin)


