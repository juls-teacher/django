import logging
import os
from django.http import HttpResponse
from django.conf import settings

logger = logging.getLogger(__name__)


def index(request):
    if request.GET.get("param"):
        logger.info(f' My custom var= {settings.MY_CUSTOM_VARIABLE}')
        logger.info(f' My env var= {settings.MY_ENV_VARIABLE}')
        logger.info(f' My param = {request.GET.get("param")}')

    if int(os.getenv(key='FIRST_PARAM')) == 2023:
        logger.info(f'second variable  {os.getenv(key="SECOND_PARAM")}')
    else:
        logger.info(f'third variable {os.getenv(key="THIRD_PARAM")}')
    return HttpResponse("Shop index view")
