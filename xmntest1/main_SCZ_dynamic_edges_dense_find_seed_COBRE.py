""" Example for MOGONET classification
"""
from train_test_SCZ_dynamic_edges_dense_find_seed_COBRE import *
#run the code
# from train_test_SCZ_dynamic_edges_dense_two_modalities_k_fold import *
import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"
if __name__ == "__main__":
    #三个
    data_folder = './xmn2/model/SCZ/'
    view_list = [1,2]
    num_epoch_pretrain = 100
    num_epoch = 300
    lr_e_pretrain = 1e-3
    lr_e = 5e-4
    lr_c = 1e-3
    if data_folder == './xmn2/model/SCZ/':
        num_class = 2
    data_subfolder='COBRE'
    print(data_subfolder)
    N_SEED_all = [227]
    atlas = "aal_116"
    data_num = "145"
    model_folder = "models_true_VCDN"
    fMRI_type = 3
    # for fMRI_type in range(4):
    if fMRI_type==3:
        type_folder = "alff_gmv"
    elif fMRI_type==1:
        type_folder = "vmhc_gmv"
    elif fMRI_type==2:
        type_folder = "reho_gmv"
    elif fMRI_type==4:
        type_folder = "falff_gmv"
    # # while fMRI_type<5:
    #     # if fMRI_type in (1,2):
    print(fMRI_type)
    fold=5
    N_SEED = 1
    adj_num=10
    adj_parameter = [adj_num, adj_num, adj_num]
    type_folder = type_folder + "_adj_parameter_" + str(adj_parameter[0])
    print(atlas, data_subfolder, fMRI_type, type_folder)
    dim_he_list = [48, 48, 24]
    fold_repeat_all=0
    if N_SEED == 1:
        train_test(data_folder, view_list, num_class,
                   lr_e_pretrain, lr_e, lr_c,
                   num_epoch_pretrain, num_epoch,fold,
                   fMRI_type,fold_repeat_all,data_subfolder,
                   N_SEED_all,adj_parameter,dim_he_list,data_num,atlas,model_folder,type_folder,
                   test_fMRI="./xmn2/model/SCZ/COBRE/fMRI.csv",
                   test_sMRI="./xmn2/model/SCZ/COBRE/sMRI.csv",
                   test_DTI=None)
    fold_repeat_all = fold_repeat_all + 1