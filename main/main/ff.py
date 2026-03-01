from django.contrib.contenttypes.models import ContentType
from accounts.models import CustomUser
from shop.models import *  # Замените на ваши модели, если нужно
ContentType.objects.all().delete()
CustomUser.objects.all().delete()
exit()
