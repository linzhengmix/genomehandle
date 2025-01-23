import pandas as pd
import sys

def process_archaea_tsv(input_file, output_file):
    # Read the TSV file
    data = pd.read_csv(input_file, sep="\t")

    # Extract the ID part after GCA_ or GCF_
    data['ID'] = data['Assembly Accession'].str.extract(r'^(GCA_|GCF_)(\d+\.\d+)$')[1]

    # Define the order of Assembly Levels
    assembly_level_order = ["Complete Genome", "Chromosome", "Scaffold", "Contig"]

    # Remove duplicate rows based on the extracted ID
    filtered_data = data.drop_duplicates(subset='ID', keep='first').drop(columns='ID')

    # Group by Taxonomic ID and select rows based on Assembly Level and Total Sequence Length
    final_data = filtered_data.sort_values(
        by=['Organism Taxonomic ID', 'Assembly Level', 'Assembly Stats Total Sequence Length'],
        key=lambda col: col.map(lambda x: assembly_level_order.index(x) if x in assembly_level_order else len(assembly_level_order))
    ).drop_duplicates(subset='Organism Taxonomic ID', keep='first')

    # Write the filtered data back to a new TSV file
    final_data.to_csv(output_file, sep="\t", index=False)

# Example usage
# process_archaea_tsv("C:/Users/mixsz/Desktop/Archaea.tsv", "C:/Users/mixsz/Desktop/Filtered_Archaea.tsv")

def main():
    if len(sys.argv) != 3:
        print("Usage: process_archaea <input_file> <output_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    process_archaea_tsv(input_file, output_file)

if __name__ == "__main__":
    main()
