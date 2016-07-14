#!/usr/bin/python
"""
"""

import sys
import gff_toolkit as gt

fasta_file = 'test.fasta'
gff_success = 'test_success.gff'
gff_fail = 'test_fail.gff'

def test1():
	for gff_file in (gff_success,gff_fail):
		gff = gt.parser(gff_file,fasta_file=fasta_file)
		for transcript in gff.getitems(featuretype='mRNA'):
			if transcript.pep[0] != 'M':
				print gff_file
				print transcript.pep
				print transcript
				raise Exception('Wrong start')
			if transcript.pep[-1] != '*':
				print gff_file
				print transcript.pep
				print transcript
				raise Exception('Wrong stop')

def test2():
	assert True

if __name__ == '__main__':
	test1()
	test2()