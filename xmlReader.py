'''
Created on 14/8/2015

@author: ucsp
'''

import elementtree.ElementTree as ET
from elementtree.ElementTree import ElementTree

xml = "stompol-tweets-train-tagged.xml"

class Reader(object):
    
    def __init__(self, xml_file, xml_type):
        self.__file = xml_file
        self.__type = xml_type
        #self.__data = self.read()
    
    def read(self):
        if self.__type == 1:
            return self.__readType1()
        elif self.__type == 2:
            return self.__readType2()
        elif self.__type == 3:
            return self.__readType3()
        elif self.__type == 4:
            return self.__readType4()
        elif self.__type == 5:
            return self.__readType5()
    
    def __readType1(self):
        arch = open(self.__file, 'r')
        comentarios = []
        for lines in arch:
            comentario = []
            lines = lines.rstrip()
            aux = lines.find(">")+1
            lines = lines[aux:]
            aux = lines.find("</tweet>")
            lines = lines[:aux]
            aux = lines.find("<sentiment")
            while aux != -1:
                texto = lines[:aux]
                lines = lines[aux:]
                aux = lines.find("entity=")+8
                entity = lines[aux:]        
                texto2 = entity
                aux = entity.find("polarity")-2
                entity = entity[:aux]
                aux = texto.find("<")
                texto = texto[:aux]
                aux = texto2.find("=")+2
                polarity = texto2[aux:]
                texto2 = polarity        
                aux = polarity.find(">")-1
                polarity = polarity[:aux]
                aux = texto2.find(">")+1
                texto2 = texto2[aux:]            
                aux = texto2.find("</sentiment>")
                texto3 = texto2
                texto2 = texto2[:aux]
                texto = texto + " " +texto2
                aux = texto3.find(">")+1
                texto3 = texto3[aux:]             
                aux = texto3.find("<sentiment")
                if aux == -1:
                    texto = texto + texto3
                lines = texto3
                contenido = [texto, entity, polarity]
                comentario.append(contenido)
            comentarios.append(comentario)
        return comentarios
    
    def __readType2(self):
        arch = open(self.__file, 'r')
        comentarios = []
        for lines in arch:
            comentario = []
            lines = lines.rstrip()
            aux = lines.find(">")+1
            lines = lines[aux:]
            aux = lines.find("</tweet>")
            lines = lines[:aux]
            aux = lines.find("<sentiment")
            while aux != -1:
                texto = lines[:aux]
                lines = lines[aux:]
                aux = lines.find("entity=")+8
                entity = lines[aux:]
                texto2 = entity
                aux = entity.find(">")-1
                entity = entity[:aux]
                aux = texto2.find(">")+1
                texto2 = texto2[aux:]
                aux = texto2.find("</sentiment")
                texto3 = texto2
                texto2 = texto2[:aux]
                texto = texto + texto2
                aux = texto3.find(">")+1
                texto3 = texto3[aux:]
                aux = texto3.find("<sentiment")
                if aux == -1:
                    texto = texto + texto3
                lines = texto3
                contenido = [texto , entity]
                comentario.append(contenido)
            comentarios.append(comentario)
        return comentarios
    
    def __readType3(self):
        arch = open(self.__file, 'r')
        labels = []
        for lines in arch:
            lines = lines.rstrip()
            aux = lines.find("-")
            if aux == -1:
                labels.append(lines) 
            else:
                while aux != -1:
                    texto = lines[:aux]
                    labels.append(texto)   
                    lines = lines[aux+1:]
                    aux = lines.find("-")
                    if aux == -1:
                        texto = lines
                        labels.append(texto)
        return labels
    
    def __readType4(self):
        tree = ET.parse(self.__file)
        root = tree.getroot()
        comments = []
        for child in root:
            texto = child[1].text
            polaridad = child[2].text
            value = (texto, polaridad)
            comments.append(value)
        return comments 
    
    def __readType5(self):
        tree = ET.parse(self.__file)
        root = tree.getroot()
        comentarios = []
        for child in root:
            contenido = child[1].text 
            polaridad = child[2].text
            value = (contenido, polaridad)
            comentarios.append(value)
        return comentarios
            

                                    
    
    def getData(self):
        return self.__data

if __name__ == '__main__':
    
    arc = "Corpus/edu.xml"
    obj = Reader(arc, 5)
    
    
    
    data = obj.read()
    for i in data:
        print i
    
     
        
    