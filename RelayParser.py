#import models.py
import urllib2, datetime, time

class RelayParser:

    def parse_file(self):
        f = open('prints', 'r')
        output = f.readlines()
        f.close()
	return output

    def lookup_fingerprint(self, fingerprint):
        # Perform an HTTP relay search with the fingerprint and scrape the page
	relay_search_url = "https://metrics.torproject.org/relay-search.html?search=" + fingerprint
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
		    print "fresh: " + fingerprint
		else:
		    print "old: " + fingerprint
		break

    def main(self):
        fingerprints = self.parse_file()
	for fingerprint in fingerprints:
	    self.lookup_fingerprint(fingerprint)

if __name__ == "__main__":
    x = RelayParser()
    x.main()
