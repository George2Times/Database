#! /usr/bin/python
import sys
import os


# does not work
def main(ip_start, ip_end):
	start = ip_start.split(".")
	end = ip_end.split(".")

	for lastGroup in range( int(start[3]), int(end[3]) ):
		ip = "%s.%s.%s.%s" % (start[0],start[1],start[2],lastGroup)
		os.system('host %s' % (ip))


if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
