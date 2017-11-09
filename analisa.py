from correla_fase import correla,escreve_array
import numpy as np

#
# pattern seleciona quais arquivos pretende acessar.
#
pattern = 'Patient_2/*_ictal_*_?.mat' #10 ictais classificados do paciente 2

corr_ic, tau_ic = correla(pattern) 

pattern = 'Patient_2/*_interictal_*_?.mat' #10 os interictais classificados

corr_in, tau_in = correla(pattern)
#Nesse exemplo não foram analisados os clipes de teste

#As próximas linhas calculam média e desvio padrão dos arrays. A opção axis=0 determina que os cálculos sejam feitos elemento a elemento ao longo da dimensão que determina os arquivos. Não testei se esses cálculos funcionam com listas ou só com arrays.
corr_ic_mean = np.mean(corr_ic, axis=0) 
corr_ic_std = np.std(corr_ic, axis=0) 
escreve_array(np.stack((corr_ic_mean,corr_ic_std)), 'corr_ic.dat')
# escreve_array escreve um array com três dimensões de maneira legível
# np.stack transforma 2 arrays em 1 para escrever em um só arquivo
tau_ic_mean = np.mean(tau_ic, axis=0) 
tau_ic_std = np.std(tau_ic, axis=0) 
escreve_array(np.stack((tau_ic_mean,tau_ic_std)), 'tau_ic.dat')

corr_in_mean = np.mean(corr_in, axis=0) 
corr_in_std = np.std(corr_in, axis=0) 
escreve_array(np.stack((corr_in_mean,corr_in_std)), 'corr_in.dat')

tau_in_mean = np.mean(tau_in, axis=0) 
tau_in_std = np.std(tau_in, axis=0) 
escreve_array(np.stack((tau_in_mean,tau_in_std)), 'tau_in.dat')
