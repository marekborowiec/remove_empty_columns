#! /usr/bin/env python3

# script to remove alignment columns containing only missing data by Marek Borowiec

import argparse

import psutil

import aln_parsing, aln_writing

parser = argparse.ArgumentParser(usage='remove_empty_columns.py <alignment_file_name> <input_file_format> <data_type')

parser.add_argument(
    'alignment_file_name',
    type = str,
    help = 'Alignment in FASTA, PHYLIP, or NEXUS format.'
    )

parser.add_argument(
    'input_file_format',
    type = str,
    help = 'File format for the output alignment.',
    choices = ['fasta', 'phylip', 'nexus', 'phylip-int', 'nexus-int'],    
    )

parser.add_argument(
    'data_type',
    type = str,
    help = 'Alignment data type (dna or aa).',
    choices = ['dna', 'aa'],    
    )

args = parser.parse_args()
alignment_file_name = args.alignment_file_name
input_file_format = args.input_file_format
data_type = args.data_type
aln_tuple = aln_parsing.parse_alignment(
    alignment_file_name, input_file_format
)
aln_name, aln_dict = aln_tuple

no_sites = len(list(aln_dict.values())[0])
print(f'Alignment {alignment_file_name} has {no_sites} sites.')

missing_column_indexes = []
for index in range(no_sites):
	column = [sequence[index] for sequence in aln_dict.values()]
	uniques = set(column)
	if len(uniques) == 1 and ('-' in uniques or '?' in uniques):
		# site contains only missing characters
		print(f'Site {index+1} contains only missing data.')
		missing_column_indexes.append(index)

new_aln_dict = {}
for taxon, sequence in aln_dict.items():
	new_sequence = ''.join([character for index, character in enumerate(sequence) if index not in missing_column_indexes])
	new_aln_dict[taxon] = new_sequence

output_file_name = f'reduced-{alignment_file_name}'
aln_writing.write_alignment_file(new_aln_dict, input_file_format, output_file_name, data_type)
print(f'Wrote alignment {output_file_name} without columns containing missing data only.')