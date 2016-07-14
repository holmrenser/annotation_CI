#!/usr/bin/python
"""
"""

import gff_toolkit as gt

def main():
	fasta_file = 'test.fasta'
	gff_file = 'test.gff'
	gff = gt.parser(gff_file,fasta_file=fasta_file)
	for transcript in gff.getitems(featuretype='mRNA'):
		assert transcript.pep[0] == 'M'
		assert transcript.pep[-1] == '*'

if __name__ == '__main__':
	main(*sys.argv[1:])