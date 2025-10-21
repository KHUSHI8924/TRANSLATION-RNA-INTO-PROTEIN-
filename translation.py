dict = {'UUU':'F', 'CUU':'L',    'AUU' :'I'  ,    'GUU' :'V',
'UUC' :'F'  ,   'CUC': 'L' ,    'AUC' :'I',     'GUC': 'V',
'UUA' :'L'   ,  'CUA': 'L',     'AUA' :'I'  ,    'GUA':'V',
'UUG' :'L'  , 'CUG':'L',      'AUG' :'M'   ,   'GUG' :'V',
'UCU' :'S'    ,'CCU':'P'     , 'ACU' :'T'    ,  'GCU' :'A',
'UCC' :'S',     'CCC' :'P'    ,  'ACC' :'T'     , 'GCC' :'A',
'UCA' :'S',    'CCA' :'P'   ,   'ACA' :'T',      'GCA' :'A',
'UCG' :'S' ,   'CCG' :'P'  ,    'ACG' :'T' ,     'GCG' :'A',
'UAU' :'Y'   ,  'CAU' :'H' ,     'AAU' :'N'  ,    'GAU' :'D',
'UAC' :'Y'     , 'CAC' :'H',      'AAC' :'N'   ,   'GAC' :'D',
'UAA' :'Stop',  'CAA' :'Q'      ,'AAA' :'K'    ,  'GAA':'E',
'UAG' :'Stop',  'CAG' :'Q'     , 'AAG' :'K'     , 'GAG' :'E',
'UGU' :'C',    'CGU' :'R'    ,  'AGU' :'S'      ,'GGU':'G',
'UGC' :'C',   'CGC' :'R'   ,   'AGC' :'S',      'GGC' :'G',
'UGA' :'Stop' ,  'CGA' :'R'  ,    'AGA' :'R' ,     'GGA' :'G',
'UGG' :'W'    ,  'CGG' :'R' ,     'AGG': 'R'  ,    'GGG':'G'}


def translate_rna(rna_sequence):
    amino_acid = []
    codons=[]
    for i in range(0, len(rna_sequence)-1, 3):
        codon = rna_sequence[i] + rna_sequence[i+1] + rna_sequence[i+2]
        aminoacid = dict[codon]
        if aminoacid == 'Stop':
            pass
        else:
            amino_acid += aminoacid 
            codons.append(codon)
    return amino_acid, codons 

rna_sequence = input("ENTER THE RNA SEQUENCE TO MAKE PROTEIN:").upper()
amino_acid,codon = translate_rna(rna_sequence)
print("amino acid:", amino_acid)
print("codon:", codon)


