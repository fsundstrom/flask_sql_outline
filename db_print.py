#!bin/python
from flssql import db, models
import os.path

qu = models.data.query.all()



for u in qu:
      print(u.id,u.sn,u.vendor,u.device,u.disc)
