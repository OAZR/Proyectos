#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Primero importamos las bibliotecas que vamos a utilizar 
import pandas as pd
import numpy as np


# In[2]:


#Aquí leemos el archivo CSV y lo guardamos en la variable "dato"
dato=pd.read_csv("synergy_logistics_database.csv")


# In[3]:


dato.head() #vemos su estructura básica


# In[4]:


# Opción 1) Rutas de importación y exportación. Synergy logistics está considerando la posibilidad de enfocar sus
# esfuerzos en las 10 rutas más demandadas. Acorde a los flujos de importación y exportación, ¿cuáles son esas
# 10 rutas? ¿le conviene implementar esa estrategia? ¿porqué?


# In[5]:


#creamos la columna "ruta" que concatena "direction", "origin", "destination" y "transport mode"
dato["ruta"]=dato["direction"]+" "+dato["origin"]+" "+dato["destination"]+" "+dato["transport_mode"]
dato.head()


# In[6]:


#agrupamos y tenemos cada una de las rutas acompañada del número de veces que fue transitada, así obtenemos la demanda de cada ruta
uno=dato.groupby("ruta").count()[["register_id"]].sort_values("register_id",ascending=0).head(10)
uno.rename(columns={"register_id": "Número de veces utilizada"}).plot.bar(title="Las 10 rutas más usadas") #sólo mostramos las 10 rutas más transitadas


# In[229]:


#para ver si es correcta la opción de elegir las rutas más demandadas veamos unos puntos importantes
dato.groupby("ruta").count()[["register_id"]].sort_values("register_id",ascending=0).describe()
#aquí vemos que el 75% de los datos está debajo de 110, que son las veces que se usó esa ruta


# In[230]:


#Aquí vemos que las 10 rutas que elegimos arriba son aproximadamente el 4% más alto, nos da un primer indicador de que no es 
#conveniente usar esta estrategia pues dejaríamos muchos viajes fuera
np.percentile(dato.groupby("ruta").count()[["register_id"]].sort_values("register_id",ascending=0),95.79) 


# In[18]:


#con la columna "agregado", vemos que las 10 rutas que elegimos arriba acumulan aproximadamente el 17.5% del total de 
#viajes realizados o demandados
uno1=dato.groupby("ruta").agg(["sum","count"])[["total_value"]].sort_values(("total_value","count"),ascending=0)
uno1["Porc. agregado veces util."]=uno1[("total_value","count")].cumsum()/sum(uno1[("total_value","count")])
#q=dato[dato['direction']=='Imports'].groupby("origin").agg(["sum","count"])[["total_value"]].sort_values(("total_value","sum"),ascending=0)
#uno1["agregado"]=uno1["register_id"].cumsum()/sum(uno1["register_id"])
#uno1.rename(columns={"register_id" : "Veces utilizada"}, inplace=1)
uno1.rename(columns={"sum":"valor de imp/exp","count":"veces utilizada","total_value":"resultados"}).head(15)


# In[22]:


promedio1=sum(uno1[("total_value", "sum")][:10])/sum(uno1[("total_value", "count")][:10])
print("En promedio, por cada vez que se utiliza una de las 10 rutas el valor de las importaciones/exportaciones es: ",
      promedio1)


# In[24]:


#después de ver esto notamos que no es conveniente quedarnos unicamente con 10 rutas pues apenas engloban al 17.5% del total de 
#viajes 


# In[25]:


# ¿Cuáles son los 3 medios de transporte más importantes para Synergy logistics considerando el valor de las
# importaciones y exportaciones? ¿Cuál es medio de transporte que podrían reducir?


# In[26]:


#si en vez de considerar la demanda de rutas nos enfocamos en el medio de transporte, primero veamos cuáles son los 
#medios de transporte y su respectivo valor total de importaciones/exportaciones
w=dato.groupby("transport_mode").sum()[["total_value"]].sort_values("total_value",ascending=0)
w["agregado"]=w["total_value"].cumsum()/sum(w["total_value"])
w.rename(columns={"total_value" : "valor total"}, inplace=1)
w


# In[27]:


wq=dato.groupby("transport_mode").agg(["sum","count"])[["total_value"]].sort_values(("total_value", "sum"),ascending=0)
wq["valor promedio por servicio"]=wq[("total_value", "sum")]/wq[("total_value", "count")]
wq["Porc. agregado valor imp/exp"]=wq[("total_value","sum")].cumsum()/sum(wq[("total_value","sum")])
wq["Porc. agregado apariciones"]=wq[("total_value","count")].cumsum()/sum(wq[("total_value","count")])
wq


# In[ ]:





# In[31]:


promedio2=sum(wq[("total_value", "sum")][:3])/sum(wq[("total_value", "count")][:3])
print("En promedio, cada vez que se utiliza una de las rutas de las 3 categorías (sea, rail, air) el valor de las importaciones/exportaciones es: ",
      promedio2)


# In[32]:


print(sum(wq[("total_value", "sum")][:3]),sum(wq[("total_value", "count")[:3]]))


# In[33]:


#Veamos por año cuales son los medios de transporte que generan más valor de importaciones/exportaciones
mas1=dato.groupby(["year","transport_mode"]).sum()[["total_value"]]
g = mas1['total_value'].groupby('year', group_keys=False)
mejor=pd.DataFrame(g.nlargest(4))
mejor


# In[34]:


#si sólo consideramos importaciones:
mas1=dato[dato['direction']=='Imports'].groupby(["transport_mode"]).sum()[["total_value"]].sort_values("total_value",ascending=0)
mas1
#g = mas1['total_value'].groupby('year', group_keys=False)
#mejor=pd.DataFrame(g.nlargest(4))
#mejor


# In[35]:


#si sólo consideramos exportaciones
mas1=dato[dato['direction']=='Exports'].groupby(["transport_mode"]).sum()[["total_value"]].sort_values("total_value",ascending=0)
mas1
#g = mas1['total_value'].groupby('year', group_keys=False)
#mejor=pd.DataFrame(g.nlargest(4))
#mejor


# In[36]:


#con esto vemos que el transporte "sea" es el que más genera valor sin importar el año o actividad. Para el resto de medios de 
#transporte vemos que "air" y "road" son los que menos valor generan sin embargo es "road" el que genera el la menor cantidad
#de ambos y se podría eliminar para enfocarse en el resto.


# In[37]:


#Opción 3) Valor total de importaciones y exportaciones. Si Synergy Logistics quisiera enfocarse en los países que le
#generan el 80% del valor de las exportaciones e importaciones ¿en qué grupo de países debería enfocar sus esfuerzos?


# In[38]:


#nos interesa el origen tanto de importaciones como exportaciones, agrupemos por país y veamos cuáles son los 
#países que acumulan el 80% del valor de importaciones/exportaciones.
q=dato[dato['direction']=='Imports'].groupby("origin").agg(["sum","count"])[["total_value"]].sort_values(("total_value","sum"),ascending=0)
q["Porc. agregado valor imp/exp"]=q[("total_value","sum")].cumsum()/sum(q[("total_value","sum")])
q["Porc. agregado apariciones"]=q[("total_value","count")].cumsum()/sum(q[("total_value","count")])
q["valor promedio por servicio"]=q[("total_value", "sum")]/q[("total_value", "count")]
q


# In[39]:


print("si elegimos la segunda opción nos quedamos con ",sum(wq[("total_value", "sum")][:3])/sum(q[("total_value", "sum")][:7]),"veces más valor de imp/exp que en la tercera y con ",sum(wq[("total_value", "count")][:3])/sum(q[("total_value", "count")][:7]),"más servicios")
#si elegimos la segunda opción nos quedamos con 4.3 veces más valor de imp/exp que en la tercera y con 6.31 más servicios


# In[43]:


promedio3=sum(q[("total_value", "sum")][:7])/sum(q[("total_value", "count")][:7])
print("sin embargo, tener más flujo de servicios o demanda no siempre es mejor y como vemos el valor de importaciones/exportaciones promedio es mayor con la tercer propuesta (",promedio3/promedio2,"veces más) por lo que la tercer propuesta es más recomendable")


# In[73]:


promedio3/promedio1


# In[71]:


plt.figure(figsize=(7.5,6))
plt.bar(["propuesta 1","propuesta 2","propuesta 3"],[round(promedio1,2), round(promedio2,2),
                                                     round(promedio3,2)],color=["blue","green","red"])
plt.title("valor promedio de importaciones/exportaciones por propuesta")
plt.ylabel("decenas de millón")


# In[ ]:




