from correla_fase import correla

#
# pattern seleciona quais arquivos pretende acessar. Alguns exemplos abaixo:
#

pattern = 'Patient_1/*_ictal_*1.mat'

corr, tau = correla(pattern)
