import os
import pandas as pd
from Bio.PDB.PDBParser import PDBParser
from glob import glob


def data_processing(input_path):
    parser = PDBParser(PERMISSIVE=True)
    pdb_files = glob(input_path + '*.pdb')
    coord_data = pd.DataFrame()
    b_factor_data = pd.DataFrame()
    df_res = pd.DataFrame()
    res_data = pd.DataFrame()
    str_id = []
    miss = []
    for filename in pdb_files:
        base = os.path.basename(filename)
        structure_id = os.path.splitext(base)[0]
        data = parser.get_structure(structure_id, filename)
        str_id.append(structure_id)
        res_list = []
        coord_list = []
        b_factor_list = []
        for model in data:
            for chain in model:
                for residue in chain:
                    for atom in residue:
                        coord_list.append(atom.get_coord())
                        b_factor_list.append(atom.get_bfactor())
                for residue in chain.get_residues():
                    if residue.id[0] == ' ':
                        res_list.append(residue.get_resname())
        df_res = pd.DataFrame(data=res_list, columns=[structure_id])
        res_data = pd.concat([res_data, df_res], axis=1)
        coord_data = pd.DataFrame(data=coord_list, columns=['X', 'Y', 'Z'])
        b_factor_data = pd.DataFrame(data=b_factor_list, columns=['b values'])
        coord_pre_X_data = []
        coord_pre_Y_data = []
        coord_pre_Z_data = []
        coord_post_X_data = []
        coord_post_Y_data = []
        coord_post_Z_data = []
        for i in range(1, len(coord_data)):
            coord_pre_X_data.append(coord_data['X'][i])
            coord_pre_Y_data.append(coord_data['Y'][i])
            coord_pre_Z_data.append(coord_data['Z'][i])
        coord_pre_X_data.append(coord_data['X'][0])
        coord_pre_Y_data.append(coord_data['Y'][0])
        coord_pre_Z_data.append(coord_data['Z'][0])
        coord_post_X_data.append(coord_data['X'][len(coord_data) - 1])
        coord_post_Y_data.append(coord_data['Y'][len(coord_data) - 1])
        coord_post_Z_data.append(coord_data['Z'][len(coord_data) - 1])
        for i in range(len(coord_data) - 1):
            coord_post_X_data.append(coord_data['X'][i])
            coord_post_Y_data.append(coord_data['Y'][i])
            coord_post_Z_data.append(coord_data['Z'][i])
        coord_pre_data = pd.DataFrame({'X pre': coord_pre_X_data,
                                       'Y pre': coord_pre_Y_data,
                                       'Z pre': coord_pre_Z_data})
        coord_post_data = pd.DataFrame({'X post': coord_post_X_data,
                                        'Y post': coord_post_Y_data,
                                        'Z post': coord_post_Z_data})
        coord_total = pd.concat([coord_data,
                                 b_factor_data,
                                 coord_pre_data,
                                 coord_post_data], axis=1)
        miss.append(data.header['missing_residues'])
    miss_seq_tot = []
    miss_chain_tot = []
    miss_res_tot = []
    for i in range(len(miss)):
        miss_seq = []
        miss_chain = []
        miss_res = []
        for j in range(len(miss[i])):
            miss_chain.append(miss[i][j]['chain'])
            miss_res.append(miss[i][j]['res_name'])
            miss_seq.append(miss[i][j]['ssseq'])
        miss_chain_tot.append(miss_chain)
        miss_res_tot.append(miss_res)
        miss_seq_tot.append(miss_seq)
    miss_feat = pd.DataFrame({'res name': miss_res_tot,
                              'chain': miss_chain_tot,
                              'ssseq': miss_seq_tot})
    miss_feat.index = str_id
    return [coord_total, miss_feat]


def save_to_csv(input_path, output_path):
    parser = PDBParser(PERMISSIVE=True)
    pdb_files = glob(input_path + '*.pdb')
    str_id = []
    for filename in pdb_files:
        base = os.path.basename(filename)
        structure_id = os.path.splitext(base)[0]
        parser.get_structure(structure_id, filename)
        str_id.append(structure_id)
    data_total = data_processing(input_path)
    data_total[0].to_csv(output_path + 'coordinate_' + structure_id +
                         '.csv', index=False)
    data_total[1].to_csv(output_path + 'missing_seq_' + structure_id +
                         '.csv', index=False)


def num_atoms_of_seq():
    res_name = ['GLY', 'ALA', 'VAL', 'LEU', 'ILE', 'PHE', 'TRP', 'TYR', 'ASP',
                'HIS', 'ASN', 'GLU', 'LYS', 'GLN', 'MET', 'ARG', 'SER', 'THR',
                'CYS', 'PRO']
    res_seq_num = [4, 5, 7, 8, 8, 11, 14, 12, 8, 10, 8, 9, 9, 9, 8, 11, 6, 7,
                   6, 7]
    res_std_data = pd.DataFrame({'residue name': res_name,
                                 'number of sequence': res_seq_num})
    res_std_data = res_std_data.set_index('residue name')
    return res_std_data


def num_miss_atoms(input_path):
    parser = PDBParser(PERMISSIVE=True)
    pdb_files = glob(input_path + '*.pdb')
    data_total = data_processing(input_path)
    miss_feat = data_total[1]
    str_id = []
    for filename in pdb_files:
        base = os.path.basename(filename)
        structure_id = os.path.splitext(base)[0]
        parser.get_structure(structure_id, filename)
        str_id.append(structure_id)
    num_seq_miss = []
    for i in range(len(str_id)):
        num_seq = []
        for j in range(len(miss_feat['ssseq'][str_id[i]])):
            if miss_feat['res name'][str_id[i]][j] == 'GLY':
                num_seq.append(4)
            elif miss_feat['res name'][str_id[i]][j] == 'ALA':
                num_seq.append(5)
            elif miss_feat['res name'][str_id[i]][j] == 'SER' or\
                    miss_feat['res name'][str_id[i]][j] == 'CYS':
                num_seq.append(6)
            elif miss_feat['res name'][str_id[i]][j] == 'VAL' or\
                    miss_feat['res name'][str_id[i]][j] == 'THR' or\
                    miss_feat['res name'][str_id[i]][j] == 'PRO':
                num_seq.append(7)
            elif miss_feat['res name'][str_id[i]][j] == 'LEU' or\
                    miss_feat['res name'][str_id[i]][j] == 'ILE' or\
                    miss_feat['res name'][str_id[i]][j] == 'ASP' or\
                    miss_feat['res name'][str_id[i]][j] == 'ASN' or\
                    miss_feat['res name'][str_id[i]][j] == 'MET':
                num_seq.append(8)
            elif miss_feat['res name'][str_id[i]][j] == 'GLU' or\
                    miss_feat['res name'][str_id[i]][j] == 'LYS' or\
                    miss_feat['res name'][str_id[i]][j] == 'GLN':
                num_seq.append(9)
            elif miss_feat['res name'][str_id[i]][j] == 'HIS':
                num_seq.append(10)
            elif miss_feat['res name'][str_id[i]][j] == 'PHE' or\
                    miss_feat['res name'][str_id[i]][j] == 'ARG':
                num_seq.append(11)
            elif miss_feat['res name'][str_id[i]][j] == 'TYR':
                num_seq.append(12)
            else:  # == 'TRP'
                num_seq.append(14)
        num_seq_miss.append(num_seq)
    return num_seq_miss
