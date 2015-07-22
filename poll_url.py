#!/usr/bin/env python

import sys
import requests
import time

def url_status(url):
    response = requests.get(url, timeout=1)
    return response.status_code

def test_url(url):
    elapsed = 0
    while(elapsed < 10):
        status = url_status(url)
        if status == 200:
            print "Successfully returned 200"
            return sys.exit(0)
        else:
            print "Returned %s" % status
            time.sleep(1)
            elapsed = elapsed + 1
    print "Failed to return 200 status"
    return sys.exit(1)

test_url(sys.argv[1])
