import os
import shutil
import tarfile
import numpy as np
import nibabel as nib

# download data from: https://drive.google.com/uc?export=download&id=1aWyS_mQ5n7X2bTk9etHrn5di2-EZEzyO

project_dir = "./"
data_folder = os.path.join(project_dir, "dataset")
data_file = os.path.join(data_folder, "L2R_Task3_AbdominalCT.tar") 

temp_folder = os.path.join(data_folder, "Training")
if os.path.exists(temp_folder):
    shutil.rmtree(temp_folder)  

tar_file = tarfile.open(data_file)
tar_file.extractall(data_folder)
tar_file.close

img_folder_name = os.path.join(temp_folder, "img")
label_folder_name = os.path.join(temp_folder, "label")

img_folder_save = os.path.join(data_folder, "images")
label_folder_save = os.path.join(data_folder, "labels")
if os.path.exists(img_folder_save):
    shutil.rmtree(img_folder_save)
if os.path.exists(label_folder_save):
    shutil.rmtree(label_folder_save)
os.makedirs(img_folder_save)
os.makedirs(label_folder_save)

for gz_image_file in os.listdir(img_folder_name):
    img = nib.load(os.path.join(img_folder_name, gz_image_file))
    img = nib.Nifti1Image(np.asarray(img.dataobj,np.int16), img.affine)
    img.to_filename(os.path.join(img_folder_save, gz_image_file[3:]))  # 'img'

for gz_label_file in os.listdir(label_folder_name):    
    lab = nib.load(os.path.join(label_folder_name, gz_label_file))
    lab = nib.Nifti1Image(np.asarray(lab.dataobj,np.int8), lab.affine)
    lab.to_filename(os.path.join(label_folder_save, gz_label_file[5:]))  # 'label'

shutil.rmtree(temp_folder)
