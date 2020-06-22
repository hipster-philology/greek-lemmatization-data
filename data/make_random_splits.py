
import os
import shutil
import itertools
import random
import glob

if __name__ == '__main__':

    random.seed(2000)
    test_per_split = 3
    dev_per_split = 2

    target = './splits'
    os.makedirs(target)
    os.makedirs(os.path.join(target, 'dev'))
    os.makedirs(os.path.join(target, 'test'))
    os.makedirs(os.path.join(target, 'train'))

    files = glob.glob('output/*tsv')
    for _, group in itertools.groupby(
            sorted(files), key=lambda f: os.path.basename(f).split('-')[0]):
        group = list(group)
        for _ in range(dev_per_split):
            f = random.choice(group)
            group.remove(f)
            shutil.copy(f, os.path.join(target, 'dev', os.path.basename(f)))
        for _ in range(test_per_split):
            f = random.choice(group)
            group.remove(f)
            shutil.copy(f, os.path.join(target, 'test', os.path.basename(f)))
        for f in group:
            shutil.copy(f, os.path.join(target, 'train', os.path.basename(f)))
