from mrjob.job import MRJob
import re

class InvertedIndex(MRJob):
    
    def mapper(self, _, line):
        # Parsear la linea del archivo TSV
        fields = line.strip().split('\t')
        
        # Obtener el nombre del autor (primaryName) y la ID (knownForTitles)
        name = fields[1]
        titleid = fields[5]
        
        # Emitir el nombre del autor con la ID asociada
        yield name, titleid
    
    def reducer(self, name, titleid):
        # Eliminar duplicados en las IDs de los autores
        unique_titleid = list(set(titleid))
        
        # Emitir el nombre del autor y su lista de IDs
        yield name, unique_titleid

if __name__ == '__main__':
    InvertedIndex.run()
