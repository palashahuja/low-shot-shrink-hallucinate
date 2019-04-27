import os
import itertools
import glob
import json


model_index = [3]
generator_index = [0]
low_shot_n = [1,2,5,10,20]
experiment_id = [1,2,3,4,5]
index = 0


for prod in itertools.product(model_index, generator_index, low_shot_n, experiment_id):
   f = open('low_shot_scripts/low_shot_' + str(index) + '.sbatch', 'w')
   f.write('#!/bin/sh\n#SBATCH --nodes=1 \n#SBATCH --ntasks-per-node=1 \n#SBATCH --cpus-per-task=2 \n#SBATCH --time=6:00:00 \n#SBATCH --mem=40GB \n#SBATCH --job-name=lowshot \n#SBATCH --mail-type=END \n#SBATCH --mail-user=pa1371@nyu.edu \n#SBATCH --output=slurm_%j.out \n#SBATCH --gres=gpu:1 \ncd ../ \nmodule purge \nmodule load anaconda3/4.3.1 \nsource activate palash-python3.6 \npython ./low_shot.py --lowshotmeta label_idx.json --experimentpath experiment_cfgs/splitfile_{:d}.json   --experimentid ' + str(prod[3]) + ' --lowshotn ' + str(prod[2]) + ' --trainfile features/ResNet10_sgm/train.hdf5    --testfile features/ResNet10_sgm/val.hdf5    --outdir low_shot_our_results   --lr 1 --wd 0.001    --testsetup 1    --max_per_label 5    --generator_name analogies    --generator_file models/generation/ResNet10_sgm/generator.tar --centroid_file centroid_files/ResNet10_sgm/cluster.pkl --model_index ' + str(prod[0]) + ' --generator_type ' + str(prod[1]))
   f.close()
   index += 1 

   


