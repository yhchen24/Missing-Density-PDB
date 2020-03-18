import os
import random
import pandas as pd
from Bio.PDB.PDBParser import PDBParser
from glob import glob

import protein_properties


def samples_statistics(directory):
    """
    This function would calculate how many files have missing residues,
    and helps you get new data frame with 50% files have missing
    residues and 50% files have no missing residues.
    :param directory: directory of pdb files, /local-folder/
    :return: print total number of files, number of files w/ w/o missing
    residues, percentage of how many files have missing residues,
    return dataset with 50% files w/ w/o missing residues
    """
    # set parser in BioPython
    parser = PDBParser(PERMISSIVE=True)
    # create pdb_files as all .pdb file in the folder
    pdb_files = glob(directory + '*.pdb')

    # create null lists
    res_missing = []
    res_nomissing = []
    reslist = []

    for filename in pdb_files:
        # grab filename contained extension from path
        base = os.path.basename(filename)
        # split filename and Extension, take the former
        structure_id = os.path.splitext(base)[0]
        # get structure
        data = parser.get_structure(structure_id, filename)

        # Get informaation from header that if files have missing residues
        # Append to different list
        keywords = data.header["has_missing_residues"]
        reslist.append(keywords)
        if keywords is True:
            res_missing.append(structure_id)
        elif keywords is False:
            res_nomissing.append(structure_id)

    print('Total number of samples:', len(reslist))
    print('Samples have missing residues:', len(res_missing))
    print('Samples without missing residues::', len(res_nomissing))
    print('There are {:.2%} samples have missing residue'.format(
        len(res_missing) / (len(res_nomissing) + len(res_missing))))

    sample_missing = random.sample(res_missing, len(res_nomissing))
    sample_nomissing = res_nomissing
    Samples_pdb = sample_missing + sample_nomissing
    print('New dataset has {} files'.format(len(Samples_pdb)))
    new_samples = pd.DataFrame(Samples_pdb, columns=['Protein'])

    return new_samples


def extraction_residues_headers(directory, protein_list):
    """
    :param directory: directory of pdb files, /local-folder/
    :param protein_list: list of names of proteins
    :return: residues and some properties/environment setting of proteins
    """

    parser = PDBParser(PERMISSIVE=True)

    pdb_files = []
    for i in range(len(protein_list)):
        pdb_files.append(directory + protein_list[i] + '.pdb')
    # Get residues, headers(missing/nomissing, )
    res_data = pd.DataFrame()
    headers = pd.DataFrame()
    name_list = []
    head_list = []
    structure_method_list = []
    resolution_list = []
    has_missing_residues_list = []
    compound_list = []

    for filename in pdb_files:
        # grab filename contained extension from path
        base = os.path.basename(filename)
        # split filename and Extension, take the former
        structure_id = os.path.splitext(base)[0]
        # get structure
        data = parser.get_structure(structure_id, filename)

        # get residues
        # create null list of residues
        res_list = []
        for model in data:
            for chain in model:
                # Iterate over all residues in the structure
                for residue in chain.get_residues():
                    # check hetero-flag, omit cases of a glucose molecule
                    # and cases of a water molecule
                    if residue.id[0] == ' ':
                        res_list.append(residue.get_resname())
        # Transform to dataframe and combine by column
        df_res = pd.DataFrame(data=res_list, columns=[structure_id])
        res_data = pd.concat([res_data, df_res], axis=1)

        # get headers
        name_list.append(data.header["name"])
        head_list.append(data.header["head"])
        structure_method_list.append(data.header["structure_method"])
        resolution_list.append(data.header["resolution"])
        has_missing_residues_list.append(data.header["has_missing_residues"])
        compound_list.append(data.header["compound"])

    # combine headers to one dataframe
    data_protein = pd.DataFrame(data=protein_list, columns=["protein"])
    data_name = pd.DataFrame(data=name_list, columns=["name"])
    data_head = pd.DataFrame(data=head_list, columns=["head"])
    data_structure_method = pd.DataFrame(data=structure_method_list,
                                         columns=["structure_method"])
    data_resolution = pd.DataFrame(data=resolution_list,
                                   columns=["resolution"])
    data_has_missing_residues = pd.DataFrame(data=has_missing_residues_list,
                                             columns=["has_missing_residues"])

    headers = pd.concat([data_protein, data_name, data_head,
                         data_structure_method, data_resolution,
                         data_has_missing_residues], axis=1)

    return [res_data, headers]


def extracted_features(directory, protein_list):
    '''
    This function returns a dataframe consisting of extracted features for use
    in the random forest and neural network models.

    Parameters
    ----------
    directory: directory of pdb files, /local-folder/

    protein_list: list of names of proteins, 'str'
    '''
    # extract residues and headers
    [res_data, headers] = extraction_residues_headers(directory, protein_list)

    # collect amino acid properties
    properties = protein_properties.residue_groups(res_data)

    # merge the two dataframes
    merge = pd.concat([headers, properties], axis=1)

    # drop a redundant column between the two dataframes
    extracted_features = merge.drop(['Protein'], axis=1)

    # return features of interest as dataframe
    return extracted_features
