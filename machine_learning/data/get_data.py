# coding: utf-8

import os
for year in range(2012, 2013):
    for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                  'Sep', 'Oct', 'Nov', 'Dec']:
        url = ("http://www.seek.com.au/content/media/EmploymentIndex/"
               "SEEK_AU_EI_Data_%s%s.xlsx" % (month, year))
        os.system("wget %s" % url)

import glob
valid_files = filter(
    lambda x: os.system("file %s|grep HTML" % x), glob.glob("*.xlsx"))
for file in valid_files:
    os.system("catdoc -a {0} > {0}.csv".format(file))
for file in valid_files:
    os.system("./xlsx2csv.py {0} |tail -n +2> {0}.csv".format(file))
