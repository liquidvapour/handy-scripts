#!/usr/bin/env python

import sys
import urllib2
import time

def url_status(url):
    try:
        return urllib2.urlopen(url, None, 5).getcode()
    except urllib2.HTTPError as e:
        return e.code

def test_url(url, timeout=60, interval=5):
    elapsed = 0
    while(elapsed < timeout):
        status = url_status(url)
        if status == 200:
            print "Successfully returned 200"
            return sys.exit(0)
        else:
            print "Returned %s" % status
            time.sleep(interval)
            elapsed = elapsed + interval
    print "Failed to return 200 status"
    return sys.exit(1)

test_url(sys.argv[1])
