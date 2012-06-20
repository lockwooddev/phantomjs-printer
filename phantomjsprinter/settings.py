from django.conf import settings

 
TMP_STORAGE_FOLDER = getattr(settings, 'PRINTER_TMP_STORAGE_FOLDER', "/tmp")
TOKEN_NAME = getattr(settings, 'PRINTER_TOKEN_NAME', 'printer_token')
TOKEN_VALUE = getattr(settings, 'PRINTER_TOKEN_VALUE', "mysecret")