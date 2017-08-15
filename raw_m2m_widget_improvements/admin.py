from django.contrib import admin

from .models import ModelA
from .models import ModelB


class ModelAAdmin(admin.ModelAdmin):
    raw_id_fields = ('model_bs', 'model_b')

admin.site.register(ModelA, ModelAAdmin)
admin.site.register(ModelB)
