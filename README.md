# Codon Table Generator
A Python program to generate a codon table, validate DNA sequences, and translate them into amino acids using the standard genetic code.


# Codon Table Generator & NCBI Integration

A robust Python-based bioinformatics tool designed to validate DNA sequences, translate them into amino acids using the standard genetic code, extract Open Reading Frames (ORFs), and fetch live genomic data directly from the NCBI GenBank database.

---

## Features
- **DNA Validation**: Automatically filters and validates sequences to ensure only valid nucleotides (`A`, `T`, `G`, `C`) are processed.
- **Standard Genetic Code Translation**: Maps all 64 codons to their respective amino acids, complete with Start (`ATG`) and Stop (`TAA`, `TAG`, `TGA`) codon detection.
- **Open Reading Frame (ORF) Extraction**: Scans sequences to isolate and translate complete ORFs from start to finish.
- **NCBI GenBank Integration**: Connects live to the NCBI API (`Entrez efetch`) to fetch real biological sequences using accession numbers (e.g., human chromosome regions, viral genomes).
- **Color-Coded Terminal UI**: Outputs a clean, property-coded table grouping amino acids by their chemical properties (Hydrophobic, Polar, Basic, Acidic, and Stop) using ANSI terminal styling.

---

## Project Structure
- `codon_project.py`: The core Python script containing input validation, the 64-codon dictionary, NCBI API connection, translation logic, and ORF scanning.
- `README.md`: Project documentation and usage guide.

---

## How It Works
1. **Input Selection**: Users can choose to input a custom DNA sequence manually or fetch a live sequence from the NCBI database via an Accession ID.
2. **Translation Engine**: The program steps through the DNA sequence in triplets (codons), references the standard genetic code dictionary, and lists the mapped amino acids.
3. **ORF & Codon Analysis**: It detects start (`ATG`) and stop codons, tracks the totals, and formats the output into an easy-to-read, color-coded table.

---

## How to Run

1. Ensure you have **Python** installed on your system.
2. Clone or download this repository to your local machine.
3. Open your terminal (or VS Code Git Bash) inside the project folder.
4. Run the script:
   ```bash
   python codon_project.py