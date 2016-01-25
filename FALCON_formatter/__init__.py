#!/usr/bin/env python

import sys, os, glob, argparse

def main():
	parser = argparse.ArgumentParser(description="Takes PacBio fastq/a files and formats them for use with FALCON")
	parser.add_argument('-w', metavar='INT', help="Hard-wrap lenth for fasta output [%(default)s]", default=80, type=int)
	parser.add_argument('-o', metavar='STR', help="Output path [%(default)s]", default='.', type=str)
	parser.add_argument('input', metavar='F', nargs="+", help="Fastq/a files or folders for formatting")
	args = parser.parse_args()
	fileList = []
	for inArg in args.input:
		if os.path.isdir(inArg):
			# Grab all files in folder
			fileList += glob.glob(os.path.join(inArg,"*"))
		else:
			fileList.append(inArg)
	# Dictionary of output files
	OF = {}
	# Iterate through the inputs and process only fasta
	# and fastq files.
	for infile in fileList:
		print("Processing: %s"%(infile))
		# determine if the file is fasta for fastq
		inext = os.path.splitext(infile)[1][1:]
		if inext in ('fasta','fa'):
			parseFasta(infile, OF, args.w, args.o)
		if inext in ('fastq','fq'):
			parseFastq(infile, OF, args.w, args.o)
		else:
			sys.exit("Bad file format: %s"%(infile))
	# Close files
	for k,v in OF.iteritems():
		v.close()

def parseFasta(infile, OF, wrap, outDest):
	fName = ''
	header = ''
	seqBuild = ''
	for line in open(infile,'r'):
		tmp = line.rstrip('\n')
		if tmp[0] == '>':
			if header and seqBuild:
				# Write sequence when new header is found
				writeFA(fName, header, seqBuild, OF, wrap)
			seqBuild = ''
			header = tmp
			# Generate file name from header
			fName = os.path.join(outDest, tmp[1:].split('/')[0]+'.fasta')
		else:
			seqBuild += tmp
	# Write final sequence
	writeFA(fName, header, seqBuild, OF, wrap)

def parseFastq(infile, OF, wrap, outDest):
	for header, seq in fqReader(infile):
		if header[0] != "@":
			print header, seq
			sys.exit("Bad fastq format: %s"%(infile))
		faHeader = '>%s'%(header[1:])
		fName = os.path.join(outDest, faHeader[1:].split('/')[0]+'.fasta')
		writeFA(fName, faHeader, seq, OF, wrap)

def fqReader(inFile):
	IF = open(inFile,'r')
	name1 = IF.readline().rstrip('\n')
	while name1:
		seq = IF.readline().rstrip('\n')
		name2 = IF.readline()
		qual = IF.readline()
		yield((name1,seq))
		name1 = IF.readline().rstrip('\n')
	IF.close()

def writeFA(fName, header, seq, OF, wrap):
	if fName not in OF:
		# If the file for this header doesn't already exist,
		# create it and use it.
		OF[fName] = open(fName,'w')
	# Hardwrap the fasta to 80 chr.
	splitSeq = '\n'.join([seq[i:i+wrap] for i in xrange(0, len(seq), wrap)])
	OF[fName].write("%s\n%s\n"%(header,splitSeq))

if __name__ == "__main__":
	main()
