Script for removing missing data-only columns from multple sequence alignments. You have to use it in a directory that contains all three files `aln_parsing.py`, `aln_writing.py` and `remove_empty_columns.py`. 
```
usage: remove_empty_columns.py <alignment_file_name> <input_file_format> <data_type>

positional arguments:
  alignment_file_name   Alignment in FASTA, PHYLIP, or NEXUS format.
  {fasta,phylip,nexus,phylip-int,nexus-int}
                        File format for the output alignment.
  {dna,aa}              Alignment data type (dna or aa).

optional arguments:
  -h, --help            show this help message and exit
```
