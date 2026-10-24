# Codon Table Generator Project - Step 1: Initialization

# Codon Table Generator Project - Step 1: Initialization

# 1. Standard Genetic Code Dictionary (All 64 Codons)
codon_table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'Stop', 'TAG':'Stop',
    'TGC':'C', 'TGT':'C', 'TGA':'Stop', 'TGG':'W'
}

# 2. Accept DNA Input from User
# def get_valid_dna():
#     dna = input("Enter a DNA sequence: ").upper()
#     return dna

# 2 & 3. Accept and Validate DNA Input
def get_valid_dna():
    while True:
        dna = input("Enter a DNA sequence (e.g., ATGGCTTTTTAA): ").upper()
        if all(nucleotide in ['A', 'T', 'G', 'C'] for nucleotide in dna):
            return dna
        else:
            print("Invalid DNA sequence! Please use only A, T, G, and C.")

# 4, 5, 6, 7. Translate DNA into Codons and Amino Acids
# def translate_dna(dna):
#     codons = []
#     amino_acids = []

#     # Step through the sequence in steps of 3
#     for i in range(0, len(dna) - 2, 3):
#         codon = dna[i:i+3]
#         codons.append(codon)

#         amino_acid = codon_table.get(codon, 'Unknown')
#         amino_acids.append(amino_acid)

#     return codons, amino_acids          

# 4, 5, 6, 7. Translate DNA into Codons and Amino Acids
# def translate_dna(dna):
#     codons = []
#     amino_acids = []
#     start_codons = []

#     # Step through the sequence in steps of 3
#     for i in range(0, len(dna) - 2, 3):
#         codon = dna[i:i+3]
#         codons.append(codon)

#         amino_acid = codon_table.get(codon, 'Unknown')
#         amino_acids.append(amino_acid)

#         # Identify start codons
#         if codon == 'ATG':
#             start_codons.append(codon)

#     return codons, amino_acids, start_codons

# 4, 5, 6, 7. Translate DNA into Codons and Amino Acids
# def translate_dna(dna):
#     codons = []
#     amino_acids = []
#     start_codons = []
#     stop_codons = []

#     # Step through the sequence in steps of 3
#     for i in range(0, len(dna) - 2, 3):
#         codon = dna[i:i+3]
#         codons.append(codon)

#         amino_acid = codon_table.get(codon, 'Unknown')
#         amino_acids.append(amino_acid)

#         # Identify start and stop codons
#         if codon == 'ATG':
#             start_codons.append(codon)
#         elif amino_acid == 'Stop':
#             stop_codons.append(codon)

#     return codons, amino_acids, start_codons, stop_codons

# 4, 5, 6, 7. Translate DNA into Codons and Amino Acids
def translate_dna(dna):
    codons = []
    amino_acids = []
    start_codons = []
    stop_codons = []

    # Step through the sequence in steps of 3
    for i in range(0, len(dna) - 2, 3):
        codon = dna[i:i+3]
        codons.append(codon)

        amino_acid = codon_table.get(codon, 'Unknown')
        amino_acids.append(amino_acid)

        # Identify start and stop codons
        if codon == 'ATG':
            start_codons.append(codon)
        elif amino_acid == 'Stop':
            stop_codons.append(codon)

    # Handle incomplete codons at the end
    remainder = len(dna) % 3
    if remainder != 0:
        print(f"Note: Ignored {remainder} extra trailing nucleotide(s) at the end.")

    return codons, amino_acids, start_codons, stop_codons


