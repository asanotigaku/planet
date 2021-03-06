#!/usr/bin/env python3

import sys
import os
import subprocess
#import sksat

def usage():
	print('usage> ./render.py fmt.pov startnum fnum')

def main(argc, argv):
	if argc != 5:
		usage()
		return
	
	povfmt	= argv[1]
	startnum= int(argv[2])
	fnum	= int(argv[3])
	out_interval = int(argv[4])
	
	for i in range(startnum, fnum):
		cmd = 'povray '
		cmd += povfmt
		cmd = cmd % i
#		cmd += ' | grep num:'
		subprocess.call(cmd, shell=True)
		print('num:\r' + str(i))
		if (i % out_interval) == 0:
#			cmd = '~/python/slack/sksat_bot/post.py simulation \"' + 'render:' + str(i) + '\"'
#			os.system(cmd)
			pass

if __name__ == '__main__':
	argc = len(sys.argv)
	argv = sys.argv
	main(argc, argv)

