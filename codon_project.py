# # Codon Table Generator Project - Step 1: Initialization

# # Codon Table Generator Project - Step 1: Initialization

# # 1. Standard Genetic Code Dictionary (All 64 Codons)
# codon_table = {
#     'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
#     'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
#     'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
#     'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
#     'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
#     'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
#     'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
#     'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
#     'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
#     'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
#     'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
#     'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
#     'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
#     'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
#     'TAC':'Y', 'TAT':'Y', 'TAA':'Stop', 'TAG':'Stop',
#     'TGC':'C', 'TGT':'C', 'TGA':'Stop', 'TGG':'W'
# }

# # 2. Accept DNA Input from User
# # def get_valid_dna():
# #     dna = input("Enter a DNA sequence: ").upper()
# #     return dna

# # 2 & 3. Accept and Validate DNA Input
# def get_valid_dna():
#     while True:
#         dna = input("Enter a DNA sequence (e.g., ATGGCTTTTTAA): ").upper()
#         if all(nucleotide in ['A', 'T', 'G', 'C'] for nucleotide in dna):
#             return dna
#         else:
#             print("Invalid DNA sequence! Please use only A, T, G, and C.")

# # 4, 5, 6, 7. Translate DNA into Codons and Amino Acids
# # def translate_dna(dna):
# #     codons = []
# #     amino_acids = []

# #     # Step through the sequence in steps of 3
# #     for i in range(0, len(dna) - 2, 3):
# #         codon = dna[i:i+3]
# #         codons.append(codon)

# #         amino_acid = codon_table.get(codon, 'Unknown')
# #         amino_acids.append(amino_acid)

# #     return codons, amino_acids          

# # 4, 5, 6, 7. Translate DNA into Codons and Amino Acids
# # def translate_dna(dna):
# #     codons = []
# #     amino_acids = []
# #     start_codons = []

# #     # Step through the sequence in steps of 3
# #     for i in range(0, len(dna) - 2, 3):
# #         codon = dna[i:i+3]
# #         codons.append(codon)

# #         amino_acid = codon_table.get(codon, 'Unknown')
# #         amino_acids.append(amino_acid)

# #         # Identify start codons
# #         if codon == 'ATG':
# #             start_codons.append(codon)

# #     return codons, amino_acids, start_codons

# # 4, 5, 6, 7. Translate DNA into Codons and Amino Acids
# # def translate_dna(dna):
# #     codons = []
# #     amino_acids = []
# #     start_codons = []
# #     stop_codons = []

# #     # Step through the sequence in steps of 3
# #     for i in range(0, len(dna) - 2, 3):
# #         codon = dna[i:i+3]
# #         codons.append(codon)

# #         amino_acid = codon_table.get(codon, 'Unknown')
# #         amino_acids.append(amino_acid)

# #         # Identify start and stop codons
# #         if codon == 'ATG':
# #             start_codons.append(codon)
# #         elif amino_acid == 'Stop':
# #             stop_codons.append(codon)

# #     return codons, amino_acids, start_codons, stop_codons

# # 4, 5, 6, 7. Translate DNA into Codons and Amino Acids
# # def translate_dna(dna):
# #     codons = []
# #     amino_acids = []
# #     start_codons = []
# #     stop_codons = []

# #     # Step through the sequence in steps of 3
# #     for i in range(0, len(dna) - 2, 3):
# #         codon = dna[i:i+3]
# #         codons.append(codon)

# #         amino_acid = codon_table.get(codon, 'Unknown')
# #         amino_acids.append(amino_acid)

# #         # Identify start and stop codons
# #         if codon == 'ATG':
# #             start_codons.append(codon)
# #         elif amino_acid == 'Stop':
# #             stop_codons.append(codon)

# #     # Handle incomplete codons at the end
# #     remainder = len(dna) % 3
# #     if remainder != 0:
# #         print(f"Note: Ignored {remainder} extra trailing nucleotide(s) at the end.")

# #     return codons, amino_acids, start_codons, stop_codons

# # 8. Run and Display Output in Formatted Format
# if __name__ == "__main__":
#     print("=== Codon Table Generator ===")
#     user_dna = get_valid_dna()

#     codons, amino_acids, starts, stops = translate_dna(user_dna)

#     print("\n--- Results ---")
#     print("Codons      :", "-".join(codons))
#     print("Amino acids :", " - ".join(amino_acids))
#     print("Start codon :", ", ".join(starts) if starts else "None found")
#     print("Stop codon  :", ", ".join(stops) if stops else "None found")

# """
# Project Name: Codon Table Generator
# Author: Mahalakshmi
# Description: Translates DNA sequences into amino acids and detects start/stop codons.
# """

# import urllib.request
# import urllib.error

# # 1. Standard Genetic Code Dictionary (All 64 Codons)
# codon_table = {
#     'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
#     'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
#     'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
#     'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
#     'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
#     'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
#     'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
#     'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
#     'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
#     'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
#     'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
#     'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
#     'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
#     'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
#     'TAC':'Y', 'TAT':'Y', 'TAA':'Stop', 'TAG':'Stop',
#     'TGC':'C', 'TGT':'C', 'TGA':'Stop', 'TGG':'W'
# }

# # 2. Fetch Sequence from NCBI Database via Accession ID
# def fetch_ncbi_sequence(accession_id):
#     url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id={accession_id}&rettype=fasta&retmode=text"
#     try:
#         print(f"Fetching sequence {accession_id} from NCBI database...")
#         with urllib.request.urlopen(url) as response:
#             fasta_data = response.read().decode('utf-8')
#             lines = fasta_data.strip().split('\n')
#             # Join all lines except the header line
#             sequence = "".join([line.strip() for line in lines if not line.startswith(">")])
#             return sequence.upper()
#     except urllib.error.URLError as e:
#         print(f"Error fetching from NCBI: {e.reason}")
#         return None

# # 3. Accept and Validate DNA Input
# def get_valid_dna():
#     choice = input("Do you want to (1) Enter manually or (2) Fetch from NCBI Database? Enter 1 or 2: ").strip()
    
#     if choice == '2':
#         acc_id = input("Enter NCBI Accession ID (e.g., NC_001422 or J01415): ").strip()
#         raw_dna = fetch_ncbi_sequence(acc_id)
#         if not raw_dna:
#             print("Falling back to manual entry.")
#             return get_valid_dna()
#         # Clean and validate the fetched sequence
#         clean_dna = "".join([n for n in raw_dna if n in ['A', 'T', 'G', 'C']])
#         return clean_dna
#     else:
#         while True:
#             dna = input("Enter a DNA sequence (e.g., ATGGCTTTTTAA): ").upper()
#             if all(nucleotide in ['A', 'T', 'G', 'C'] for nucleotide in dna):
#                 return dna
#             else:
#                 print("Invalid DNA sequence! Please use only A, T, G, and C.")

# # 4, 5, 6, 7. Translate DNA into Codons and Amino Acids
# def translate_dna(dna):
#     codons = []
#     amino_acids = []
#     start_codons = []
#     stop_codons = []
    
#     for i in range(0, len(dna) - 2, 3):
#         codon = dna[i:i+3]
#         codons.append(codon)
        
#         amino_acid = codon_table.get(codon, 'Unknown')
#         amino_acids.append(amino_acid)
        
#         if codon == 'ATG':
#             start_codons.append(codon)
#         elif amino_acid == 'Stop':
#             stop_codons.append(codon)
            
#     remainder = len(dna) % 3
#     if remainder != 0:
#         print(f"Note: Ignored {remainder} extra trailing nucleotide(s) at the end.")
        
#     return codons, amino_acids, start_codons, stop_codons

# # 8. Run and Display Output Format
# if __name__ == "__main__":
#     print("=== Codon Table Generator & NCBI Integration ===")
#     user_dna = get_valid_dna()
    
#     if user_dna:
#         codons, amino_acids, starts, stops = translate_dna(user_dna)
        
#         print(f"\n--- Results (Total Nucleotides: {len(user_dna)}) ---")
#         # Print only the first 20 codons if the sequence is very long so the screen doesn't flood
#         display_limit = 20
#         print(f"Codons (showing first {display_limit} max):", "-".join(codons[:display_limit]))
#         print(f"Amino acids :", " - ".join(amino_acids[:display_limit]))
#         print("Start codons found:", len(starts))
#         print("Stop codons found :", len(stops))

"""
Project Name: Codon Table Generator & NCBI Integration
Author: Mahalakshmi
Description: Translates DNA sequences into amino acids and displays results in a formatted table.
"""

import urllib.request
import urllib.error

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

# 2. Fetch Sequence from NCBI Database via Accession ID
def fetch_ncbi_sequence(accession_id):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id={accession_id}&rettype=fasta&retmode=text"
    try:
        print(f"Fetching sequence {accession_id} from NCBI database...")
        with urllib.request.urlopen(url) as response:
            fasta_data = response.read().decode('utf-8')
            lines = fasta_data.strip().split('\n')
            sequence = "".join([line.strip() for line in lines if not line.startswith(">")])
            return sequence.upper()
    except urllib.error.URLError as e:
        print(f"Error fetching from NCBI: {e.reason}")
        return None

# 3. Accept and Validate DNA Input
def get_valid_dna():
    choice = input("Do you want to (1) Enter manually or (2) Fetch from NCBI Database? Enter 1 or 2: ").strip()
    
    if choice == '2':
        acc_id = input("Enter NCBI Accession ID (e.g., NC_001422 or NC_000007.14): ").strip()
        raw_dna = fetch_ncbi_sequence(acc_id)
        if not raw_dna:
            print("Falling back to manual entry.")
            return get_valid_dna()
        clean_dna = "".join([n for n in raw_dna if n in ['A', 'T', 'G', 'C']])
        return clean_dna
    else:
        while True:
            dna = input("Enter a DNA sequence (e.g., ATGGCTTTTTAA): ").upper()
            if all(nucleotide in ['A', 'T', 'G', 'C'] for nucleotide in dna):
                return dna
            else:
                print("Invalid DNA sequence! Please use only A, T, G, and C.")

# 4. Translate DNA into Codons and Amino Acids
def translate_dna(dna):
    codons = []
    amino_acids = []
    start_codons = []
    stop_codons = []
    
    for i in range(0, len(dna) - 2, 3):
        codon = dna[i:i+3]
        codons.append(codon)
        
        amino_acid = codon_table.get(codon, 'Unknown')
        amino_acids.append(amino_acid)
        
        if codon == 'ATG':
            start_codons.append(codon)
        elif amino_acid == 'Stop':
            stop_codons.append(codon)
            
    remainder = len(dna) % 3
    if remainder != 0:
        print(f"Note: Ignored {remainder} extra trailing nucleotide(s) at the end.")
        
    return codons, amino_acids, start_codons, stop_codons

# 5. Run and Display Output as a Table
if __name__ == "__main__":
    print("=== Codon Table Generator & Table View ===")
    user_dna = get_valid_dna()
    
    if user_dna:
        codons, amino_acids, starts, stops = translate_dna(user_dna)
        
        print(f"\n--- Translation Results Summary ---")
        print(f"Total Nucleotides : {len(user_dna)}")
        print(f"Start codons found: {len(starts)}")
        print(f"Stop codons found : {len(stops)}")
        
        print("\n--- Codon to Amino Acid Table (First 15 Codons) ---")
        print(f"{'Index':<6} | {'Codon':<6} | {'Amino Acid':<12}")
        print("-" * 32)
        
        # Display up to the first 15 codons in a neat table format
        limit = min(15, len(codons))
        for i in range(limit):
            print(f"{i+1:<6} | {codons[i]:<6} | {amino_acids[i]:<12}")
            
        if len(codons) > 15:
            print(f"... and {len(codons) - 15} more codons.")