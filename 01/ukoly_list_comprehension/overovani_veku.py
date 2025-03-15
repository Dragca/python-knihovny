#https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/cykly-2/list-comprehension/overovani-veku

veky = [35, 12, 44, 11, 18, 21, 28, 18]

#1
print([18-(int(vek))for vek in veky])
#2
print([int(vek) >= 18 for vek in veky])
#3
print([int(vek) == 18 for vek in veky])