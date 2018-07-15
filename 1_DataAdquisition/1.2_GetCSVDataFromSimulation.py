import json
import pandas as pd
from pprint import pprint
from os import listdir
from os.path import isfile, join, basename
import glob
from decimal import *

#def diferenciaPresion(A, B, Q): 
#    return  ( Decimal(A*Q) + Decimal(B*Q*Q))

def diferenciaPresion(data): 
    li = data['Pressures'][0]['Pressure Inlet'][0]
    return  li[-1]

def ls(expr = '*.*'):
    return glob(expr)

def getTipo(nombreArchivo):
      return nombreArchivo.split('_')[1].strip()

def getDLBeta(argument):
    switcher = {
        1:(0.04,0.9,0.2),
        2:(0.04,1.10,0.2),
        3:(0.04,1.30,0.2),

        4:(0.04,0.9,0.6),
        5:(0.04,1.10,0.6),
        6:(0.04,1.30,0.6),

        7:(0.04,0.9,1),
        8:(0.04,1.10,1),
        9:(0.04,1.30,1),

        10:(0.055,0.9,0.2),
        11:(0.055,1.10,0.2),
        12:(0.055,1.30,0.2),

        13:(0.055,0.9,0.6),
        14:(0.055,1.10,0.6),
        15:(0.055,1.30,0.6),

        16:(0.055,0.9,1),
        17:(0.055,1.10,1),
        18:(0.055,1.30,1),

        19:(0.08,0.9,0.2),
        20:(0.08,1.10,0.2),
        21:(0.08,1.30,0.2),

        22:(0.08,0.9,0.6),
        23:(0.08,1.10,0.6),
        24:(0.08,1.30,0.6),

        25:(0.08,0.9,1),
        26:(0.08,1.10,1),
        27:(0.08,1.30,1)
    }
    #return "Caso " + str(argument)
    return switcher.get(argument, "Tipo Invalido")

def getAngulo(nombreArchivo):
    if len(nombreArchivo.split('_')) == 2:
        return 0
    else:
        if len(nombreArchivo.split('_')) == 3:
            return int(nombreArchivo.split('_')[2].strip())
        else:
            # Si contiene _I entonces es que es un angulo negativo
            return -int(nombreArchivo.split('_')[2].strip())

   
############################################        
# MAIN
############################################        

rows_list = []
df = pd.DataFrame(rows_list, columns=['Caso X', 'D','L','Beta','Velocidad','Angulo','A','B','Q', 'Reynolds','TotalAreaInlet', 'P'])

carpetaTrabajo = ""
for itemCarpeta in  [carpetaTrabajo +"2A1DD7CB-EAA3-4D50-944D-C6F77031592C\\",carpetaTrabajo +"0320BF40-5294-46A7-9CF8-A9DE41A66D3C\\",carpetaTrabajo +"389FE1BC-1058-4FF0-B428-42F92B19222A\\", carpetaTrabajo +"A8266BA2-5937-45D5-90BD-79875E9E7255\\",carpetaTrabajo +"D4147996-D704-4328-8891-3BE1E29E76BE\\", carpetaTrabajo + "EE7F8FBF-3683-4435-9C3A-E4A5A3BD0BFD\\"]:

    # Obtenemos el nombre de todos los archivos JSON de la carpeta de trabajo
    #ficheros_directorio_1 = ls(itemCarpeta + "*.json")
    ficheros_directorio_1 = glob.glob(itemCarpeta + "*.json")

    for f in ficheros_directorio_1:
            with open(f) as data_file: 
         
                print(f)

                # Leemos el archivo JSON
                data = json.load(data_file)

                # A partir de la ruta completa obtemos el nombre del archivo sin extension
                rutaSplit = f.split("\\")
                nombreArchivoSinExtension = rutaSplit[len(rutaSplit)-1].split(".")[0]
        
                # Obtenemos el tipo de caso segun el nombre del archivo sin extension 
                tipo = getTipo(nombreArchivoSinExtension)
      
                # Conseguimos D,L,BETA, segun el caso tipificado, leido anteriormente
                dlbeta = getDLBeta(int(tipo))
     
                # Obtenemos angulo de incidencia con la aorta del nombre del archivo sin extension
                angulo = getAngulo(nombreArchivoSinExtension)

                # Conseguimos A,B del JSON
                A = data['Hemodynamic Parameters_1001_AB'][0]['A']
                B = data['Hemodynamic Parameters_1001_AB'][0]['B']
                       
                Q = data['Outlet 1001'][0]['Flow_outlet(peak)']
          
                Reynolds = data['Inlet'][0]['Reynolds(peak)']
                TotalAreaInlet =  data['Inlet'][0]['Total_area_inlet']

                # Conseguimos Velocidad = Flow_inlet(mean) / Total_area_inlet 
                Velocidad = abs(data['Inlet'][0]['Flow_inlet(mean)'] / data['Inlet'][0]['Total_area_inlet'])
                        
                tupla = [{'Caso X': 'Caso ' + str(tipo), 'D': dlbeta[0], 'L': dlbeta[1], 'Beta': dlbeta[2], 'Velocidad': Velocidad, 'Angulo': angulo, 'A': A, 'B': B, 'Q': Q , 'Reynolds': Reynolds, 'TotalAreaInlet': TotalAreaInlet, 'P': diferenciaPresion(data)}]
                df = df.append(tupla, ignore_index=True)

df.to_csv('salida.csv')

print ('Finished')

############################################        
