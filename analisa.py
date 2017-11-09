from correla_fase import correla

#
# pattern seleciona quais arquivos pretende acessar. Alguns exemplos abaixo:
#


pattern = 'Patient_1/*_ictal_*1.mat'

corr_1_ic, tau_1_ic = correla(pattern)



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

