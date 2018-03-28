import os
import requests
import json
import re
import pprint
from flask import request, abort, render_template
from app import app, db, models
import config


# create index page
#########################
@app.route('/')
def index():
 
  # we are getting the info provied by flask for the conneciton 
  # ref http://werkzeug.pocoo.org/docs/wrappers/#werkzeug.wrappers.BaseRequest.remote_addr

  # get remote ip
  ip = request.environ['REMOTE_ADDR']
  head = request.headers
 
  # retirm template with info 
  return render_template("index.html", lookup_ip=ip, headers=head)

## show DB
##################

@app.route('/shdb')
@app.route('/shdb/<int:page>',methods=['GET', 'POST'])
def showdb(page=1):
    data = models.data.query.paginate(page, POSTS_PER_PAGE, False)
    return render_template('showdb.html',
                           title='Show DB',
                           data=data,
                           env=os.environ)

## Form for data import
########################

@flssql.route('/importCSV')
def form():
    return """
        <html>
            <body>
                <h1>Import CSV</h1>

                <form action="/readCSV" method="post" enctype="multipart/form-data">
                    <input type="file" name="data_file" />
                    <input type="submit" />
                </form>
            </body>
        </html>
    """


@flssql.route('/readCSV', methods=["POST"])
def transform_view():
    f = request.files['data_file']
    if not f:
        return "No file"

    # get data from form
    stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
    stuff = csv_input = csv.reader(stream)
    # add to DB
    x=0
    for ary in csv_input:
       u = models.data(sn=ary[0],vendor=ary[1],device=ary[2],disc=ary[3])
       db.session.add(u)
       x += 1
    db.session.commit()
    return render_template('CSVdone.html',
                           title='CSV_Loaded',
                           env=os.environ,
                           x=x,
                           data=stuff)





####################################################################################
# Private methods, helpers and error handlers                                      #
####################################################################################

# default error handler
@app.errorhandler(400)
def bad_request(error):
  return "Bad request: %s" % error, 400

