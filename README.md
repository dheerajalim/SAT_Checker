[![Build Status](https://travis-ci.org/dheerajalim/SAT_Checker.svg?branch=master)](https://travis-ci.org/dheerajalim/SAT_Checker)

# SAT_Checker
Satisfiability Checker for Propositional Satisfiability Problems(SAT)

# HOW TO USE
1. Run the file usinf SAT.py
2. Update cnf_instance for the cnf_instance file path
3. Update solution_file for the solution file path

# File format for Satisfiability Problems
##### The preamble. 
The preamble contains information about the instance. This
information is contained in lines. Each line begins with a single character
(followed by a space) that determines the type of line. These types are as
follows:
##### Comments : 
comment line give human-readable information about the
file and are ignored by programs. Comment lines appear at the
beginning of the preamble. Each line begins with a lower-case
character c
c This is an example of a comment line
##### Problem line: 
there is one problem line per input file. The problem line
must appear before any node or arc descriptor lines. For cnf instances,
the problem line has the following format, the problem line begins with
a lower-case character p

p FORMAT VARIABLES CLAUSES

The FORMAT field allows programs to determine the format that will
be expected, and should contain the word “cnf”. The VARIABLES field
contains an integer value specifying n, the number of variables in the
instance. The CLAUSES field contains an integer value specifying m,
the number of clauses in the instance. This line must occur as the last
line of the preamble.
#####  The CLAUSES . 
The clauses appear immediately after the problem
line. The variables are assumed to be numbered from 1 up to n. It is
not necessary that every variable appear in an instance. Each clause
will be represented by a sequence of number, each separated by
either a space, a tab, or a newline character. The non-negated version
of a variable i is represented by i; the negated version is represented
by -i.
Each clause is terminated by “0”. Unlike many formats that represent
the end of a clause by a new-line symbol, this format allows clauses to
be on multiple lines.

#####  Example:
(x 1 ∨ x 3 ∨ -x 4) ∧ (x 4) ∧ (x 2 ∨ -x 3)
A possible input file would be
c Example CNF format file
c
p cnf 4 3
1 3 -4 0
4 0
2 -3 0

#####  Output or solution files
Every algorithm or heuristic creates an output or solution file. This output file
should consist of one or more of the following lines, depending on the type
of algorithm and problem being solved.
#####  • Comment.
Comment line give human-readable information about the
file and are ignored by programs. Comment lines can appear
anywhere in the file. Each comment line begins with a lower-case
character c. Note that comment lines can be used to provide solution
information not otherwise available (i.e., computation time, number of
calculations).
c This is an example of a comment line
#####  • Variable Line
vV
The lower-case character v means that this is a variable line. The
value V is either a positive value i , which means that i should be set to
true or a negative value -i , implying it should be set to false.



