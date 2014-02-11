# This script will look for common sharepoint directories and files 
# mainly _vti_pvt/users.pwd and /authors.pwd

#https://www.defcon.org/images/defcon-11/dc-11-presentations/dc-11-Shannon/presentations/dc-11-shannon.pdf

import sys
import os
import httplib
import urlparse
import argparse
import urllib2

# Create command line parser to take user input
parser = argparse.ArgumentParser(description = 'Analyze Sharepoint URL for vulns')
parser.add_argument('url', type = str, help = 'Enter base url eg. www.example.com/')
args = parser.parse_args()

SP_URL = args.url

print SP_URL

# Check if URL resolves

print "Checking if URL exists.."

try:
    url_response = urllib2.urlopen(SP_URL).read()
except urllib2.HTTPError, e:
    print "HTTP Error " + str(e.code) + ". Make sure to enter a valid URL"
    sys.exit(1)
except urllib2.URLError, e:
    print "URL Error " + str(e.args)
    sys.exit(1)

print SP_URL + "is valid"

# Check for _vti_bin, _vti_pvt, and _vti_layouts

def urlcheck (SP_URL):
    dirs_to_check = ['_vti_bin' ,'_vti_layouts' ,'_vti_pvt']
    for x in dirs_to_check:
        print x
        url = SP_URL + "/" +x
        print url
        try:
            url_success = urllib2.urlopen(url)
            status = url_success.getcode()
            print status
        except: 
            print "That didnt work"

# Main function

if __name__ == '__main__':
    print urlcheck(SP_URL)
