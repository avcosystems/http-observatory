from httpobs.scanner.local import scan
import sys
import json

if len(sys.argv) == 0:
	print("You must supply an endpoint argument")
	sys.exit(1)

if len(sys.argv) == 2:
	print("Scanning: '" + sys.argv[1] + "'")
	print(json.dumps(scan(sys.argv[1]), sort_keys=True, indent=2))
else:
	print("Scanning: '" + sys.argv[1] + "' http_port: '" + sys.argv[2] + "' https_port: '" + sys.argv[3] + "'")
	print(json.dumps(scan(sys.argv[1], https_port=sys.argv[2]), sort_keys=True, indent=2))
