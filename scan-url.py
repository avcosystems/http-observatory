from httpobs.scanner.local import scan
import sys
import pprint

if len(sys.argv) == 0:
	pprint.pprint("You must supply an endpoint argument")
	sys.exit()

if len(sys.argv) == 2:
	pprint.pprint("Scanning: '" + sys.argv[1] + "'")
	pprint.pprint(scan(sys.argv[1]))
else:
	pprint.pprint("Scanning: '" + sys.argv[1] + "' http_port: '" + sys.argv[2] + "' https_port: '" + sys.argv[3] + "'")
	pprint.pprint(scan(sys.argv[1], https_port=sys.argv[2]))
