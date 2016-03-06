#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from datetime import datetime
from pymongo import MongoClient
import ast



client = MongoClient()
client = MongoClient('mongodb://162.243.122.37:27017/')
db=client.tinyjumbo
print db.google.find_one()


