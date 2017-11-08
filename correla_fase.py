import glob
import scipy.io
import numpy as np
from scipy.signal import hilbert
#
# pattern seleciona quais arquivos pretende acessar. Alguns exemplos abaixo:
#

#pattern = 'Patient_1/*_ictal_*mat' #Seleciona todos os ictais do pacientes 1
#pattern = 'Patient_?/*_ictal_*mat' #Seleciona todos os ictais de todos os pacientes
#pattern = 'Patient_?/*_interictal_*mat' #Seleciona todos os interictais de todos os pacientes
#pattern = 'Patient_?/*_testing_*mat' #Seleciona todos os testes de todos os pacientes
#pattern = 'Patient_?/*mat' #Seleciona todos os sinais de todos os pacientes
#pattern = '*/*_ictal_*mat' #Seleciona os ictais de todos os humanos e cachorros
#pattern = 'Dog_?/*_ictal_*mat' #Seleciona todos os ictais de todos os cachorros

pattern = 'Patient_1/*_ictal_*1.mat'

files = glob.glob(pattern) # Cria uma lista com todos os arquivos
corr = []
tau = []
for f in files: # Laço sobre todos os arquivos
    #print(f)
    clip = scipy.io.loadmat(f) # Abre cada arquivo
    freq = int(clip['freq'][0])
    chan = np.vstack(clip['channels'][0][0])
    data = clip['data']
    nchan = len(chan)
    
    corr_clip = [[0 for i in chan] for j in chan]
    tau_clip = [[0 for i in chan] for j in chan]
    H = hilbert(data)
    fase = np.arctan2(np.imag(H),data)
    for i in range(nchan):
        for j in range(nchan):
            c = np.correlate(fase[i],fase[j],mode='full')
            t = np.argmax(abs(c))
            tau_clip[i][j] = t/freq
            corr_clip[i][j] = c[t]
    corr.append(corr_clip)
    tau.append(tau_clip)

corr = np.array(corr)    
with open('correl.dat', 'wb') as f:
    for data_slice in corr:
        np.savetxt(f, data_slice, fmt='%f')
        f.write(b'# New slice\n')

tau = np.array(tau)    
with open('tau.dat', 'wb') as f:
    for data_slice in tau:
        np.savetxt(f, data_slice, fmt='%f')
        f.write(b'# New slice\n')

