#
# INFORMATION about 454sim
#

454sim process standard FASTA either by command line argument or on standard in 
and will generate reads, one for each FASTA entry present in the file starting 
from the first base and until either the sequence ends or the simulated read 
ends (due to quality deteriorates or all flows have been spent).

As a consequence it is very useful to utilize a script which will generate 
fragments from a larger genome as is done in the preparation face with 454 
sequencing. We include a perl-script in all zip-files called “fragsim” 
which will produce fragments given an genome which could then be further 
feed through 454sim.

454sim takes a number of parameters visible via the --help flag:
-a   Processors to use count (default=8)
-n   Number of flows to simulate per sample (default=800)
-g   generation to simulate (available=GS,FLX,Ti, default=Ti)
-d   directory with generations (default=gen)
-o   output file (default=none specified)
-i   simulation info file (default=none written)


Typical run-line in a Linux environment:

./fragsim -c 1000000 -l 1000 genome.fasta | ./454sim -o genome.sff

or

./fragsim -c 1000000 -l 1000 genome.fasta > genome.fragments.fasta
./454sim -o genome.sff genome.fragments.fasta

or (compressing intermediate data)

./fragsim -c 1000000 -l 1000 genome.fasta | gzip > genome.fragments.fasta.gz
zcat genome.fragments.fasta.gz | ./454sim -o genome.sff

The above example will generation 1 million reads from genome.fasta and store 
the output in genome.sff (the first example will squash intermediate fragment 
output while the second/third will store the output in genome.fragments.fasta.)



#
# Generation files
#

The generation files are by default found in the gen folder. 454sim is shipped 
with a couple of generation files, for example ti.gen, which describes the the 
Roche Titantium 454 chemistry/instrument. A more detailed explanation of 
parameters and their values can be found in the included generations files, 
like the ti.gen file.


#
# Compiling
#

# gcc
make

# intel
make CC=intel

# gcc 32-bit (on 64-bit system, 32-bit is used by default on a 32-bit system)
make CC=gcc32



#
# Testing with test454sim
#

A test script is provided in order to perform simple testing of 454sim with 
default or custom parameters.

test454sim takes the following parameters:

-b <binary>          default = ./454sim
-d <output-details>  default = 2 [0 = simple, 1 = normal, 2 = detailed]
-f <fasta>           default = examples/example.fragments.fasta
-p <454sim-param>    default = ''                                               # these parameters are passed on to 454sim (use quotes)

-s <sff-out>         default = /tmp/454sim.test.sff
-n <info-out>        default = /tmp/454sim.test.sff.txt                         # this file is analysed


An example run just testing 454sim (on Linux with Perl in /usr/bin/perl):
./test454sim -d0

Detailed info of the GS chemistry with custom FASTA
./test454sim -d2 -f[my-fasta-file] -p'-gGS'

An example run testing 454sim (Windows version) using wine:
./test454sim -b'wine 454sim.exe'


