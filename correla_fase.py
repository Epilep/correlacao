import glob
import scipy.io
import numpy as np
from scipy.signal import hilbert

def correla(pattern):
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
                tau_clip[i][j] = t/freq - 1
                corr_clip[i][j] = c[t]
        corr.append(corr_clip)
        tau.append(tau_clip)

    corr = np.array(corr)    
    tau = np.array(tau)    

    return corr, tau
