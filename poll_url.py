#!/usr/bin/env python

import sys
import urllib
import time

def url_status(url):
    return urllib.urlopen(url).getcode()

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
