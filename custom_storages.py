from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

# class S3CustomStorage(S3BotoStorage):
#     def _normalize_name(self, name):
#         """
#         Get rid of this crap: http://stackoverflow.com/questions/12535123/django-storages-and-amazon-s3-suspiciousoperation
#         """
#         return name

class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3BotoStorage):
        location = settings.MEDIAFILES_LOCATION
