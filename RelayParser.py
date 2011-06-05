#import models.py
import urllib2, datetime, time
import sys

class RelayParser:

    def parse_file(self):
        f = open('prints', 'r')
        output = f.readlines()
        f.close()
	return output

    def lookup_fingerprint(self, fingerprint, search_date = "" ):
        # Perform an HTTP relay search with the fingerprint and scrape the page
	# Check to see whether a search_date is specified
	relay_search_page = ""
	if (len(search_date) > 0):
	    relay_search_url = "https://metrics.torproject.org/relay-search.html?search=" + fingerprint +  "+" + search_date
	    print "Date: " + search_date
	    relay_search_page = urllib2.urlopen(relay_search_url).read().split("\n")
	else: 
	    relay_search_url = "https://metrics.torproject.org/relay-search.html?search=" + fingerprint
	    print "No date"
            relay_search_page = urllib2.urlopen(relay_search_url).read().split("\n")

	for line in relay_search_page:   
	# Look for the first instance of valid-after, since that will be the most recent metric
	    if line.find("<tt>valid-after") != -1:
	        # Parse out the date which is enclosed by an <a> tag
	        date_start = line.find("\"_blank\">") + 9
		date_end = line.find("</a>")
	        date = line[date_start:date_end]
		parsed_date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
                # Make sure this last metric is within 5 hours of now
		if (time.mktime(parsed_date.timetuple()) + 5 * 60 * 60 > time.mktime(datetime.datetime.now().timetuple())):
		    print "fresh: " + fingerprint.strip()
		else:
		    print "old: " + fingerprint
		    return 0
	    elif line.find("w Bandwidth=") != -1:
	        # Parse out the bandwidth after the Bandwidth=
		bandwidth_start = line.find("w Bandwidth=") + 12
		bandwidth_end = line.find("</tt><br><tt>p ")
		bandwidth = line[bandwidth_start:bandwidth_end]
		print "Bandwidth " + bandwidth + "\n"
		return bandwidth
	return 0
    def main(self):
        fingerprints = self.parse_file()
	#Get the specified search date from the command line

	if (len(sys.argv) > 0): 
	    search_date = sys.argv[1]
	else:
	    search_date = ""
	
	totalbandwidth = 0
	for fingerprint in fingerprints:
		bandwidth = self.lookup_fingerprint(fingerprint, search_date) 
		totalbandwidth = totalbandwidth + int(bandwidth)
	print totalbandwidth
	
	        
if __name__ == "__main__":
    x = RelayParser()
    x.main()
