#!bin/python
from flssql import db, models
import os.path

# my data
data = [
   {'sn':'c1',
    'vendor':'cisco',
    'device':'switch',
    'disc':'rack mount'
   },
   {'sn':'c2',
    'vendor':'cisco',
    'device':'router',
    'disc':'rack mount'
   },
   {'sn':'c4',
    'vendor':'cisco',
    'device':'access',
    'disc':'wall'
   },
   {'sn':'a5',
    'vendor':'arista',
    'device':'switch',
    'disc':'rack mount'
   },
   {'sn':'x7',
    'vendor':'sonicwall',
    'device':'vpn',
    'disc':'rack mount'
   }
 ]

for data in data:
    u = models.data(sn=data['sn'],vendor=data['vendor'],device=data['device'],disc=data['disc'])
    db.session.add(u)

db.session.commit()
