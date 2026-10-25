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

# """
# Project Name: Codon Table Generator & NCBI Integration
# Author: Mahalakshmi
# Description: Translates DNA sequences into amino acids and displays results in a formatted table.
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
#             sequence = "".join([line.strip() for line in lines if not line.startswith(">")])
#             return sequence.upper()
#     except urllib.error.URLError as e:
#         print(f"Error fetching from NCBI: {e.reason}")
#         return None

# # 3. Accept and Validate DNA Input
# def get_valid_dna():
#     choice = input("Do you want to (1) Enter manually or (2) Fetch from NCBI Database? Enter 1 or 2: ").strip()
    
#     if choice == '2':
#         acc_id = input("Enter NCBI Accession ID (e.g., NC_001422 or NC_000007.14): ").strip()
#         raw_dna = fetch_ncbi_sequence(acc_id)
#         if not raw_dna:
#             print("Falling back to manual entry.")
#             return get_valid_dna()
#         clean_dna = "".join([n for n in raw_dna if n in ['A', 'T', 'G', 'C']])
#         return clean_dna
#     else:
#         while True:
#             dna = input("Enter a DNA sequence (e.g., ATGGCTTTTTAA): ").upper()
#             if all(nucleotide in ['A', 'T', 'G', 'C'] for nucleotide in dna):
#                 return dna
#             else:
#                 print("Invalid DNA sequence! Please use only A, T, G, and C.")

# # 4. Translate DNA into Codons and Amino Acids
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

# # 5. Run and Display Output as a Table
# if __name__ == "__main__":
#     print("=== Codon Table Generator & Table View ===")
#     user_dna = get_valid_dna()
    
#     if user_dna:
#         codons, amino_acids, starts, stops = translate_dna(user_dna)
        
#         print(f"\n--- Translation Results Summary ---")
#         print(f"Total Nucleotides : {len(user_dna)}")
#         print(f"Start codons found: {len(starts)}")
#         print(f"Stop codons found : {len(stops)}")
        
#         print("\n--- Codon to Amino Acid Table (First 15 Codons) ---")
#         print(f"{'Index':<6} | {'Codon':<6} | {'Amino Acid':<12}")
#         print("-" * 32)
        
#         # Display up to the first 15 codons in a neat table format
#         limit = min(15, len(codons))
#         for i in range(limit):
#             print(f"{i+1:<6} | {codons[i]:<6} | {amino_acids[i]:<12}")
            
#         if len(codons) > 15:
#             print(f"... and {len(codons) - 15} more codons.")

# """
# Project Name: Codon Table Generator & NCBI Integration
# Author: Mahalakshmi
# Description: Translates DNA sequences and displays results in a colorful, property-coded table.
# """

# import urllib.request
# import urllib.error

# # ANSI Color Codes for Terminal Styling
# RESET = "\033[0m"
# BOLD = "\033[1m"
# GREEN = "\033[92m"   # Hydrophobic / Non-polar
# BLUE = "\033[94m"    # Polar
# YELLOW = "\033[93m"  # Special / Start / Stop
# RED = "\033[91m"     # Stop Codons / Acidic
# CYAN = "\033[96m"    # Basic

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

# # Helper function to assign colors to amino acids
# def get_colored_amino_acid(aa):
#     if aa == 'Stop':
#         return f"{RED}{BOLD}Stop{RESET}"
#     elif aa in ['I', 'L', 'V', 'F', 'M', 'W', 'A', 'P']:
#         return f"{GREEN}{aa}{RESET}"  # Hydrophobic (Green)
#     elif aa in ['S', 'T', 'Y', 'N', 'Q', 'C']:
#         return f"{BLUE}{aa}{RESET}"   # Polar (Blue)
#     elif aa in ['K', 'R', 'H']:
#         return f"{CYAN}{aa}{RESET}"   # Basic (Cyan)
#     elif aa in ['D', 'E']:
#         return f"{YELLOW}{aa}{RESET}" # Acidic (Yellow)
#     else:
#         return aa

# # 2. Fetch Sequence from NCBI Database
# def fetch_ncbi_sequence(accession_id):
#     url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id={accession_id}&rettype=fasta&retmode=text"
#     try:
#         print(f"Fetching sequence {accession_id} from NCBI database...")
#         with urllib.request.urlopen(url) as response:
#             fasta_data = response.read().decode('utf-8')
#             lines = fasta_data.strip().split('\n')
#             sequence = "".join([line.strip() for line in lines if not line.startswith(">")])
#             return sequence.upper()
#     except urllib.error.URLError as e:
#         print(f"Error fetching from NCBI: {e.reason}")
#         return None

# # 3. Accept and Validate DNA Input
# def get_valid_dna():
#     choice = input("Do you want to (1) Enter manually or (2) Fetch from NCBI Database? Enter 1 or 2: ").strip()
    
#     if choice == '2':
#         acc_id = input("Enter NCBI Accession ID (e.g., NC_001422 or NC_000007.14): ").strip()
#         raw_dna = fetch_ncbi_sequence(acc_id)
#         if not raw_dna:
#             print("Falling back to manual entry.")
#             return get_valid_dna()
#         clean_dna = "".join([n for n in raw_dna if n in ['A', 'T', 'G', 'C']])
#         return clean_dna
#     else:
#         while True:
#             dna = input("Enter a DNA sequence (e.g., ATGGCTTTTTAA): ").upper()
#             if all(nucleotide in ['A', 'T', 'G', 'C'] for nucleotide in dna):
#                 return dna
#             else:
#                 print("Invalid DNA sequence! Please use only A, T, G, and C.")

# # 4. Translate DNA into Codons and Amino Acids
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

# # 5. Run and Display Output as a Colorful Table
# if __name__ == "__main__":
#     print(f"{BOLD}=== Colorful Codon Table Generator & NCBI Integration ==={RESET}")
#     user_dna = get_valid_dna()
    
#     if user_dna:
#         codons, amino_acids, starts, stops = translate_dna(user_dna)
        
#         print(f"\n{BOLD}--- Translation Results Summary ---{RESET}")
#         print(f"Total Nucleotides : {len(user_dna)}")
#         print(f"Start codons found: {len(starts)}")
#         print(f"Stop codons found : {len(stops)}")
        
#         print(f"\n{BOLD}--- Color-Coded Translation Table (First 15 Codons) ---{RESET}")
#         print(f"{'Index':<6} | {'Codon':<6} | {'Amino Acid':<18}")
#         print("-" * 38)
        
#         limit = min(15, len(codons))
#         for i in range(limit):
#             colored_aa = get_colored_amino_acid(amino_acids[i])
#             # Extra padding spaces handled cleanly for ANSI escape sequences
#             print(f"{i+1:<6} | {codons[i]:<6} | {colored_aa}")
            
#         if len(codons) > 15:
#             print(f"... and {len(codons) - 15} more codons.")
        
#         print(f"\n{BOLD}Color Legend:{RESET} {GREEN}Hydrophobic{RESET} | {BLUE}Polar{RESET} | {CYAN}Basic{RESET} | {YELLOW}Acidic{RESET} | {RED}Stop{RESET}")

# """
# Project Name: Codon Table Generator & NCBI Integration
# Author: Mahalakshmi
# Description: Translates DNA sequences and extracts/displays complete Open Reading Frames (ORFs) with property color-coding.
# """

# import urllib.request
# import urllib.error

# # ANSI Color Codes for Terminal Styling
# RESET = "\033[0m"
# BOLD = "\033[1m"
# GREEN = "\033[92m"   # Hydrophobic / Non-polar
# BLUE = "\033[94m"    # Polar
# YELLOW = "\033[93m"  # Special / Start / Stop
# RED = "\033[91m"     # Stop Codons / Acidic
# CYAN = "\033[96m"    # Basic

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

# # Helper function to assign colors to amino acids
# def get_colored_amino_acid(aa):
#     if aa == 'Stop':
#         return f"{RED}{BOLD}Stop{RESET}"
#     elif aa in ['I', 'L', 'V', 'F', 'M', 'W', 'A', 'P']:
#         return f"{GREEN}{aa}{RESET}"  # Hydrophobic (Green)
#     elif aa in ['S', 'T', 'Y', 'N', 'Q', 'C']:
#         return f"{BLUE}{aa}{RESET}"   # Polar (Blue)
#     elif aa in ['K', 'R', 'H']:
#         return f"{CYAN}{aa}{RESET}"   # Basic (Cyan)
#     elif aa in ['D', 'E']:
#         return f"{YELLOW}{aa}{RESET}" # Acidic (Yellow)
#     else:
#         return aa

# # 2. Fetch Sequence from NCBI Database
# def fetch_ncbi_sequence(accession_id):
#     url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id={accession_id}&rettype=fasta&retmode=text"
#     try:
#         print(f"Fetching sequence {accession_id} from NCBI database...")
#         with urllib.request.urlopen(url) as response:
#             fasta_data = response.read().decode('utf-8')
#             lines = fasta_data.strip().split('\n')
#             sequence = "".join([line.strip() for line in lines if not line.startswith(">")])
#             return sequence.upper()
#     except urllib.error.URLError as e:
#         print(f"Error fetching from NCBI: {e.reason}")
#         return None

# # 3. Accept and Validate DNA Input
# def get_valid_dna():
#     choice = input("Do you want to (1) Enter manually or (2) Fetch from NCBI Database? Enter 1 or 2: ").strip()
    
#     if choice == '2':
#         acc_id = input("Enter NCBI Accession ID (e.g., NC_001422 or NC_000007.14): ").strip()
#         raw_dna = fetch_ncbi_sequence(acc_id)
#         if not raw_dna:
#             print("Falling back to manual entry.")
#             return get_valid_dna()
#         clean_dna = "".join([n for n in raw_dna if n in ['A', 'T', 'G', 'C']])
#         return clean_dna
#     else:
#         while True:
#             dna = input("Enter a DNA sequence (e.g., ATGGCTTTTTAA): ").upper()
#             if all(nucleotide in ['A', 'T', 'G', 'C'] for nucleotide in dna):
#                 return dna
#             else:
#                 print("Invalid DNA sequence! Please use only A, T, G, and C.")

# # 4. Translate DNA into Codons and Amino Acids
# def translate_dna(dna):
#     codons = []
#     amino_acids = []
    
#     for i in range(0, len(dna) - 2, 3):
#         codon = dna[i:i+3]
#         codons.append(codon)
#         amino_acid = codon_table.get(codon, 'Unknown')
#         amino_acids.append(amino_acid)
            
#     return codons, amino_acids

# # 5. Extract Open Reading Frames (ORFs: ATG to Stop)
# def find_orfs(codons, amino_acids):
#     orfs = []
#     current_orf_codons = []
#     current_orf_aas = []
#     in_orf = False
    
#     for codon, aa in zip(codons, amino_acids):
#         if codon == 'ATG' and not in_orf:
#             in_orf = True
#             current_orf_codons = [codon]
#             current_orf_aas = [aa]
#         elif in_orf:
#             current_orf_codons.append(codon)
#             current_orf_aas.append(aa)
#             if aa == 'Stop':
#                 orfs.append((current_orf_codons, current_orf_aas))
#                 in_orf = False
#                 current_orf_codons = []
#                 current_orf_aas = []
#     return orfs

# # 6. Run and Display Colorful ORF Tables
# if __name__ == "__main__":
#     print(f"{BOLD}=== Bioinformatics ORF & Color-Coded Table Generator ==={RESET}")
#     user_dna = get_valid_dna()
    
#     if user_dna:
#         codons, amino_acids = translate_dna(user_dna)
#         orfs = find_orfs(codons, amino_acids)
        
#         print(f"\n{BOLD}--- Sequence Summary ---{RESET}")
#         print(f"Total Nucleotides : {len(user_dna)}")
#         print(f"Total Codons      : {len(codons)}")
#         print(f"Complete ORFs Found: {len(orfs)}")
        
#         if orfs:
#             print(f"\n{BOLD}--- Displaying First Complete Open Reading Frame (ORF) ---{RESET}")
#             first_orf_codons, first_orf_aas = orfs[0]
#             print(f"ORF Length: {len(first_orf_codons)} codons ({len(first_orf_codons)*3} base pairs)\n")
            
#             print(f"{'Index':<6} | {'Codon':<6} | {'Amino Acid':<18}")
#             print("-" * 38)
            
#             for i in range(len(first_orf_codons)):
#                 colored_aa = get_colored_amino_acid(first_orf_aas[i])
#                 print(f"{i+1:<6} | {first_orf_codons[i]:<6} | {colored_aa}")
#         else:
#             print(f"\n{YELLOW}No complete ORF (ATG...Stop) found in this frame. Displaying first 20 codons instead:{RESET}")
#             print(f"{'Index':<6} | {'Codon':<6} | {'Amino Acid':<18}")
#             print("-" * 38)
#             limit = min(20, len(codons))
#             for i in range(limit):
#                 colored_aa = get_colored_amino_acid(amino_acids[i])
#                 print(f"{i+1:<6} | {codons[i]:<6} | {colored_aa}")
                
#         print(f"\n{BOLD}Color Legend:{RESET} {GREEN}Hydrophobic{RESET} | {BLUE}Polar{RESET} | {CYAN}Basic{RESET} | {YELLOW}Acidic{RESET} | {RED}Stop{RESET}")

"""
Project Name: Codon Table Generator & NCBI / RNA Integration
Author: Mahalakshmi
Description: Validates and translates DNA or RNA sequences using the standard genetic code table.
"""

import urllib.request
import urllib.error

# ANSI Color Codes for Terminal Styling
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"   # Hydrophobic / Non-polar
BLUE = "\033[94m"    # Polar
YELLOW = "\033[93m"  # Special / Start / Stop
RED = "\033[91m"     # Stop Codons / Acidic
CYAN = "\033[96m"    # Basic

# 1. Standard Genetic Code Dictionary (Standard 'T'-based table)
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

# Helper function to assign colors to amino acids
def get_colored_amino_acid(aa):
    if aa == 'Stop':
        return f"{RED}{BOLD}Stop{RESET}"
    elif aa in ['I', 'L', 'V', 'F', 'M', 'W', 'A', 'P']:
        return f"{GREEN}{aa}{RESET}"  # Hydrophobic (Green)
    elif aa in ['S', 'T', 'Y', 'N', 'Q', 'C']:
        return f"{BLUE}{aa}{RESET}"   # Polar (Blue)
    elif aa in ['K', 'R', 'H']:
        return f"{CYAN}{aa}{RESET}"   # Basic (Cyan)
    elif aa in ['D', 'E']:
        return f"{YELLOW}{aa}{RESET}" # Acidic (Yellow)
    else:
        return aa

# 2. Fetch Sequence from NCBI Database
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

# 3. Accept and Validate DNA or RNA Input
def get_valid_sequence():
    choice = input("Select input type:\n (1) Enter DNA manually (A, T, G, C)\n (2) Enter RNA manually (A, U, G, C)\n (3) Fetch from NCBI Database\nEnter 1, 2, or 3: ").strip()
    
    if choice == '3':
        acc_id = input("Enter NCBI Accession ID (e.g., NC_001422 or NC_000007.14): ").strip()
        raw_seq = fetch_ncbi_sequence(acc_id)
        if not raw_seq:
            print("Falling back to manual entry.")
            return get_valid_sequence()
        clean_seq = "".join([n for n in raw_seq if n in ['A', 'T', 'G', 'C']])
        return clean_seq, "DNA"
        
    elif choice == '2':
        while True:
            rna = input("Enter an RNA sequence (e.g., AUGGCUUUUUAA): ").upper()
            if all(n in ['A', 'U', 'G', 'C'] for n in rna):
                return rna, "RNA"
            else:
                print("Invalid RNA sequence! Please use only A, U, G, and C.")
    else:
        while True:
            dna = input("Enter a DNA sequence (e.g., ATGGCTTTTTAA): ").upper()
            if all(n in ['A', 'T', 'G', 'C'] for n in dna):
                return dna, "DNA"
            else:
                print("Invalid DNA sequence! Please use only A, T, G, and C.")

# 4. Translate Sequence (Handles RNA by mapping U to T for standard table lookup)
def translate_sequence(seq, seq_type):
    codons = []
    amino_acids = []
    
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        codons.append(codon)
        
        # If input is RNA, replace 'U' with 'T' to look up in the standard table
        lookup_codon = codon.replace('U', 'T')
        amino_acid = codon_table.get(lookup_codon, 'Unknown')
        amino_acids.append(amino_acid)
            
    return codons, amino_acids

# 5. Extract Open Reading Frames (ORFs: Start to Stop)
def find_orfs(codons, amino_acids, seq_type):
    start_marker = 'AUG' if seq_type == 'RNA' else 'ATG'
    orfs = []
    current_orf_codons = []
    current_orf_aas = []
    in_orf = False
    
    for codon, aa in zip(codons, amino_acids):
        # Match start codon depending on sequence type
        if codon == start_marker and not in_orf:
            in_orf = True
            current_orf_codons = [codon]
            current_orf_aas = [aa]
        elif in_orf:
            current_orf_codons.append(codon)
            current_orf_aas.append(aa)
            if aa == 'Stop':
                orfs.append((current_orf_codons, current_orf_aas))
                in_orf = False
                current_orf_codons = []
                current_orf_aas = []
    return orfs

# 6. Run and Display Results
if __name__ == "__main__":
    print(f"{BOLD}=== Codon Table Generator (DNA & RNA Support) ==={RESET}")
    seq, seq_type = get_valid_sequence()
    
    if seq:
        codons, amino_acids = translate_sequence(seq, seq_type)
        orfs = find_orfs(codons, amino_acids, seq_type)
        
        print(f"\n{BOLD}--- Sequence Summary ({seq_type}) ---{RESET}")
        print(f"Total Nucleotides : {len(seq)}")
        print(f"Total Codons      : {len(codons)}")
        print(f"Complete ORFs Found: {len(orfs)}")
        
        start_display = 'AUG' if seq_type == 'RNA' else 'ATG'
        
        if orfs:
            print(f"\n{BOLD}--- Displaying First Complete Open Reading Frame ({start_display}...Stop) ---{RESET}")
            first_orf_codons, first_orf_aas = orfs[0]
            print(f"ORF Length: {len(first_orf_codons)} codons ({len(first_orf_codons)*3} base pairs)\n")
            
            print(f"{'Index':<6} | {'Codon':<6} | {'Amino Acid':<18}")
            print("-" * 38)
            
            for i in range(len(first_orf_codons)):
                colored_aa = get_colored_amino_acid(first_orf_aas[i])
                print(f"{i+1:<6} | {first_orf_codons[i]:<6} | {colored_aa}")
        else:
            print(f"\n{YELLOW}No complete ORF ({start_display}...Stop) found. Displaying first 20 codons instead:{RESET}")
            print(f"{'Index':<6} | {'Codon':<6} | {'Amino Acid':<18}")
            print("-" * 38)
            limit = min(20, len(codons))
            for i in range(limit):
                colored_aa = get_colored_amino_acid(amino_acids[i])
                print(f"{i+1:<6} | {codons[i]:<6} | {colored_aa}")
                
        print(f"\n{BOLD}Color Legend:{RESET} {GREEN}Hydrophobic{RESET} | {BLUE}Polar{RESET} | {CYAN}Basic{RESET} | {YELLOW}Acidic{RESET} | {RED}Stop{RESET}")