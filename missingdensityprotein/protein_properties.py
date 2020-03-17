'''
This module includes functions for counting number of electrically charged
residues, unpolar residues, hydrophobic residues, and special case residues.
A grouping function is also available in this module to create a pandas
dataframe including the features from the previously listed functions.
'''


import pandas as pd


def electrically_charged_residues(protein_sequence):
    '''
    This function returns the number of electrically charged residues (ARG,
    HIS, LYS, ASP, GLU) in the given protein sequence.

    Parameters
    ----------
    protein_sequence: Pandas dataframe assembled from
                      pdbautofill.extract_sample function in the pdb autofill
                      package. This dataframe includes the amino acid sequences
                      of each protein.
    '''
    # create empty list for electrically charged residue sum
    electrically_charged = []
    width = len(protein_sequence.columns)
    length = len(protein_sequence)

    # count number of ARG, HIS, LYS, ASP, GLU in each protein
    for j in range(width):
        sum_e_charged = 0
        for i in range(length):
            if protein_sequence.iloc[i, j] == 'ARG':
                sum_e_charged += 1
            elif protein_sequence.iloc[i, j] == 'HIS':
                sum_e_charged += 1
            elif protein_sequence.iloc[i, j] == 'LYS':
                sum_e_charged += 1
            elif protein_sequence.iloc[i, j] == 'ASP':
                sum_e_charged += 1
            elif protein_sequence.iloc[i, j] == 'GLU':
                sum_e_charged += 1
        electrically_charged.append(sum_e_charged)

    return electrically_charged


def unpolar_residues(protein_sequence):
    '''
    This function returns the number of unpolar residues (SER, THR, ASN, GLN)
    in the given protein sequence.

    Parameters
    ----------
    protein_sequence: pandas dataframe assembled from
                      pdbautofill.extract_sample function in the pdb autofill
                      package. This dataframe includes the amino acid sequences
                      of each protein.
    '''
    # create empty list for unpolar residue sum
    unpolar = []
    width = len(protein_sequence.columns)
    length = len(protein_sequence)

    # count number of SER, THR, ASN, GLN in each protein
    for j in range(width):
        sum_unpolar = 0
        for i in range(length):
            if protein_sequence.iloc[i, j] == 'SER':
                sum_unpolar += 1
            elif protein_sequence.iloc[i, j] == 'THR':
                sum_unpolar += 1
            elif protein_sequence.iloc[i, j] == 'ASN':
                sum_unpolar += 1
            elif protein_sequence.iloc[i, j] == 'GLN':
                sum_unpolar += 1

        # append to unpolar residue list
        unpolar.append(sum_unpolar)

    return unpolar


def hydrophobic_residues(protein_sequence):
    '''
    This function returns the number of hydrophobic residues (ALA, VAL, ILE,
    LEU, MET, PHE, TYR, TRP) in the given protein sequence.

    Parameters
    ----------
    protein_sequence: pandas dataframe assembled from
                      pdbautofill.extract_sample function in the pdb autofill
                      package. This dataframe includes the amino acid sequences
                      of each protein.
    '''
    # create empty list for hydrophobic residue sum
    hydrophobic = []
    width = len(protein_sequence.columns)
    length = len(protein_sequence)

    # count number of ALA, VAL, ILE, LEU, MET, PHE, TYR, TRP in each protein
    for j in range(width):
        sum_hydrophobic = 0
        for i in range(length):
            if protein_sequence.iloc[i, j] == 'ALA':
                sum_hydrophobic += 1
            elif protein_sequence.iloc[i, j] == 'VAL':
                sum_hydrophobic += 1
            elif protein_sequence.iloc[i, j] == 'ILE':
                sum_hydrophobic += 1
            elif protein_sequence.iloc[i, j] == 'LEU':
                sum_hydrophobic += 1
            elif protein_sequence.iloc[i, j] == 'MET':
                sum_hydrophobic += 1
            elif protein_sequence.iloc[i, j] == 'PHE':
                sum_hydrophobic += 1
            elif protein_sequence.iloc[i, j] == 'TYR':
                sum_hydrophobic += 1
            elif protein_sequence.iloc[i, j] == 'TRP':
                sum_hydrophobic += 1

        # append to hydrophobic residue list
        hydrophobic.append(sum_hydrophobic)

    return hydrophobic


def special_residues(protein_sequence):
    '''
    This function returns the number of special case residues (CIS, GLY, PRO)
    in the given protein sequence.

    Parameters
    ----------
    protein_sequence: pandas dataframe assembled from
                      pdbautofill.extract_sample function in the pdb autofill
                      package. This dataframe includes the amino acid sequences
                      of each protein.
    '''
    # create empty list for special residue sum
    special = []
    width = len(protein_sequence.columns)
    length = len(protein_sequence)

    # count number of CIS, GLY, PRO in each protein
    for j in range(width):
        sum_special = 0
        for i in range(length):
            if protein_sequence.iloc[i, j] == 'CIS':
                sum_special += 1
            elif protein_sequence.iloc[i, j] == 'GLY':
                sum_special += 1
            elif protein_sequence.iloc[i, j] == 'PRO':
                sum_special += 1

        # append to special residue list
        special.append(sum_special)

    return special


def residue_groups(protein_sequence):
    '''
    This function returns a dataframe that includes the amount of resides in a
    group divided by the total residues for each protein in protein_sequence.
    Groups consist of electrically charged, unpolar, hydrophobic, and special
    case. The rows represent proteins in protein_sequence, and the columns
    represent each group.

    Parameters
    ----------
    protein_sequence: pandas dataframe assembled from
                      pdbautofill.extract_sample function in the pdb autofill
                      package. This dataframe includes the amino acid sequences
                      of each protein.
    '''
    # create empty lists for the following
    sequence_length = []
    fraction_electrically_charged = []  # ARG, HIS, LYS, ASP, GLU
    fraction_unpolar = []  # SER, THR, ASN, GLN
    fraction_hydrophobic = []  # ALA, VAL, ILE, LEU, MET, PHE, TYR, TRP
    fraction_special = []  # CIS, GLY, PRO

    index = protein_sequence.columns
    width = len(index)

    # compute the following from functions in pdb_autofill package
    electrically_charged = electrically_charged_residues(protein_sequence)
    unpolar = unpolar_residues(protein_sequence)
    hydrophobic = hydrophobic_residues(protein_sequence)
    special = special_residues(protein_sequence)

    # count sequence length for each protein
    for i in range(width):
        sequence_length.append(protein_sequence.iloc[:, i].count())

    # compute the fraction of categorized residue per total protein length
    for i in range(width):
        fraction_electrically_charged.append(electrically_charged[i] /
                                             sequence_length[i])
        fraction_unpolar.append(unpolar[i]/sequence_length[i])
        fraction_hydrophobic.append(hydrophobic[i]/sequence_length[i])
        fraction_special.append(special[i]/sequence_length[i])

    # form dataframe with fractions of residues
    properties = pd.DataFrame({'Sequence Length': sequence_length,
                               'Electrically Charged':
                               fraction_electrically_charged,
                               'Nonpolar Side Chains': fraction_unpolar,
                               'Hydrophobic': fraction_hydrophobic,
                               'Special': fraction_special},
                              index=index, dtype='int')

    return properties
