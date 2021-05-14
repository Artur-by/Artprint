from django.contrib import admin

# Register your models here.
from .models import Pricepillow
admin.site.register(Pricepillow)

from .models import Colorpillow
admin.site.register(Colorpillow)

from .models import Sizepillow
admin.site.register(Sizepillow)

from .models import Side
admin.site.register(Side)
