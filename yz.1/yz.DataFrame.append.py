import pandas as pd

veriseti1 = pd.DataFrame(columns = ['A','B'])

veriseti1.loc[0] = {'A':'a1', 'B':'b1'}
veriseti1.loc[1] = {'A':'a2', 'B':'b2'}

veriseti2 = pd.DataFrame(columns = ['B','C'])
veriseti2.loc[0] = {'B':'b2', 'C':'c1'}

print(veriseti1,'\n')
print(veriseti2,'\n')

veriseti = veriseti1.append(veriseti2, ignore_index = True)
print(veriseti,'\n')

veriseti.fillna('abc', inplace = True)
print(veriseti)
