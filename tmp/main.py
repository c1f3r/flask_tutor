# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from flask import Flask
from flask import request

import MySQLdb as mdb
app = Flask(__name__)


@app.route('/')
def index():
    wmsteh = mdb.connect(host='localhost', user='root', passwd='ak3nat3r',
                         db='wmsteh', charset='utf8')
    termoprinter = mdb.connect(host='localhost', user='root',
                               passwd='ak3nat3r', db='termoprinter',
                               charset='utf8')
    with wmsteh:
        cur = wmsteh.cursor()
        cur.execute('''SELECT
                       pp.product_price,
                       p.product_name
                       FROM jos_vm_product AS p
                       INNER JOIN jos_vm_product_price AS pp
                       ON p.product_id=pp.product_id''')

        for i in xrange(cur.rowcount):
            row = cur.fetchone()
            # ter_cur = termoprinter.cursor()
            # ter_cur.execute()
            print row[0], row[1]
    return 'Hello!'


if __name__ == "__main__":
    app.run(debug=True)