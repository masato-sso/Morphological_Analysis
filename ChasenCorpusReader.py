import os
from ChasenCorpus import ChasenCorpus

class ChasenCorpusReader(object):
    def __init__(self,file_path):
        self.words=None
        self._read(os.path.expanduser(file_path))
    
    def _read(self,file_path):
        with open(file_path, 'r') as f:
            self.words=[ChasenCorpus(line[:-1]) for line in f.readlines()]
