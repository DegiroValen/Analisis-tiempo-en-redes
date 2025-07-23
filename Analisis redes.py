import pandas as pd
import matplotlib.pyplot as plt 


df = pd.read_csv("Datasets/dummy_data.csv")
#print(df.head(10))
#print(df.columns)
dfig,dfyt,dffb = df[df.platform == 'Instagram'], df[df.platform == 'Facebook'], df[df.platform == 'YouTube']



#Tiempo
#print(f" Instagram {dfig.time_spent.mean()}")
#print(f" Youtube {dfyt.time_spent.mean()}")
#print(f" Facebook {dffb.time_spent.mean()}")



#EDADES
dfige,dfyte,dffbe = dfig.age,dfyt.age,dffb.age
#Promedio
#print(f" Instagram {dfige.mean()}")
#print(f" Youtube {dfyte.mean()}")
#print(f" Facebook {dffbe.mean()}")

#Desvio estandar
#print(f" Instagram {dfige.std()}")
#print(f" Youtube {dfyte.std()}")
#print(f" Facebook {dffbe.std()}")



#Paises
dfAus,dfEng,dfUsa = df[df.location == "Australia"], df[df.location == "United Kingdom"], df[df.location == "United States"]
#Promedio
#print(f" Australia {dfAus.time_spent.mean()}")
#print(f" England {dfEng.time_spent.mean()}")
#print(f" USA {dfUsa.time_spent.mean()}")

#Desvio estandar
#print(f" Australia {dfAus.time_spent.std()}")
#print(f" England {dfEng.time_spent.std()}")
#print(f" USA {dfUsa.time_spent.std()}")



#Relacion tiempo en redes - edad
#tiempoxedad = []
#for i in range(18,65):
#    dfactual = df[df.age == i]
#    tiempoxedad.append(dfactual.time_spent.mean() )
#print(tiempoxedad)
#plt.bar([i for i in range(18, 65)],tiempoxedad)
#plt.show()



ingresoxtiempo = []
for i in range(1,10):
    dfactual = dfAus[dfAus.time_spent == i]
    ingresoxtiempo.append(dfactual.income.mean() )
print(ingresoxtiempo)
plt.bar([i for i in range(1, 10)],ingresoxtiempo)
plt.show()
