from django.contrib import admin

# Register your models here.
from .models.entity_catalog import EntityCatalog
from .models.company import Company

admin.site.register(EntityCatalog)
admin.site.register(Company)



