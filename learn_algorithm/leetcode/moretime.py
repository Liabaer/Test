# -*- coding: utf-8 -*-

import hashlib
import hmac
import json
import time
import traceback
from datetime import datetime

import boto3
from flask import current_app

from common import constants

start_time = '2021.01.21 15:45:10'
end_time = '2021.01.21 21:04:10'

print((datetime.strptime(start_time, constants.DATE_TIME_FORMAT) - datetime.strptime(end_time,
                                                                                     constants.DATE_TIME_FORMAT)).total_seconds() / 60)
