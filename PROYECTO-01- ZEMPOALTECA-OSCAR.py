#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Este es el desarrollo del proyecto 1
#Lo primero que haremos es el registro para el usuario 
#Se pedirá el nombre de usuario: Oscar
#Se pedirá la contraseña: proyecto
#Se tienen 3 intentos para ingresar los datos correctamente (usuario y contraseña)


# In[159]:


c=0
print("Bienvenido. Para ingresar coloque su nombre de usuario y contraseña")
usuario=input("Usuario: ")
contraseña=input("Contraseña: ")
while (usuario!="Oscar" or contraseña!="proyecto") and c<2:
    if usuario!="Oscar" and contraseña!="proyecto":
        print("Usuario y contraseña no encontrados, inténtelo nuevamente. \n Intentos restantes: ", 2-c)
        usuario=input("Usuario: ")
        contraseña=input("Contraseña: ")
    elif usuario!="Oscar" and contraseña=="proyecto":
        print("Nombre de usuario no encontrado, ingrese sus datos nuevamente. \n Intentos restantes: ", 2-c)
        usuario=input("Usuario: ")
        contraseña=input("Contraseña: ")
    else:
        print("Contraseña incorrecta, ingrese sus datos nuevamente. \n Intentos restantes: ", 2-c)
        usuario=input("Usuario: ")
        contraseña=input("Contraseña: ")
    c+=1
if c==2:
    if usuario!="Oscar" and contraseña!="proyecto":
        print("Usuario y contraseña no encontrados, acceso denegado.")
    elif usuario!="Oscar" and contraseña=="proyecto":
        print("Usuario no encontrado,acceso denegado")
    elif usuario=="Oscar" and contraseña!="proyecto":
        print("Contraseña incorrecta, acceso denegado")
    else:
        print("Bienvenido, ",usuario)
else:
    print("Bienvenido, ",usuario)


# In[ ]:


#Ahora debemos cargar los datos necesarios para la elaboración del reporte. Estas son las listas que se importan:
#lifestore_searches = [id_search, id product]
#lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
#lifestore_products = [id_product, name, price, category, stock]


# In[5]:


from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches


# In[6]:


# 1) Productos más vendidos y productos rezagados
## 1.1) Generar un listado de los 5 productos con mayores ventas y uno con los 10 productos con mayor búsquedas.


# In[7]:


idprod=[]
for i in lifestore_products:
    idprod.append(i[0]) #ya tenemos una lista con las id de los productos
ventasprod=[]
for i in idprod:
    cont=0
    for k in lifestore_sales:
        if k[-1]==0 and k[1]==i:
            cont+=1
    ventasprod.append((i,cont))
#con ventasprod generamos una lista de tuplas donde (idproducto,#unidades vendidas). Notar que no consideramos devoluciones
ventasprod.sort(key=lambda x:x[1],reverse=1) #Ordenamos los elementos de la lista de tuplas anterior de mayor a menor por el #unidades vendidas
masvendidos=[]
for i in ventasprod[0:5]:
    masvendidos.append(lifestore_products[i[0]-1][1])
[i.split(",")[0] for i in masvendidos]  #Ahora mostramos los 5 productos más vendidos


# In[8]:


#Para los productos más buscados realizamos un procedimiento similar:
buscar=[]
for i in idprod:
    cont=0
    for k in lifestore_searches:
        if k[1]==i:
            cont+=1
    buscar.append((i,cont)) #generamos una lista de tuplas donde (idproducto,#veces buscado)
buscar.sort(key=lambda x:x[1],reverse=1) #Ordenamos los elementos de la lista de tuplas anterior de mayor a menor por el #veces buscado
masbuscados=[]
for i in buscar[0:10]:
    masbuscados.append(lifestore_products[i[0]-1][1])
[i.split(",")[0] for i in masbuscados] #este es el listado de los 10 productos más buscados


# In[9]:


## 1.2) Por categoría, generar un listado con los 5 productos con menores ventas y uno con los 10 productos con menores búsquedas.


# In[161]:


#primero veamos cuales son las categorías
cat=[]
for h in lifestore_products:
    if h[3] not in cat:
        cat.append(h[3])


sa=[]   #Esta es una lista auxiliar para obtener los id product por cada categoría
for q in cat:
    s=[]
    for w in lifestore_products:
        if q in w:
            s.append(w[0])
    sa.append(s)

bus=[] #generamos una lista de tuplas donde (idproducto,#unidades vendidas) para todos los productos
for i in idprod:
    cont=0
    for k in lifestore_sales:
        if k[1]==i and k[-1]!=1:
            cont+=1
    bus.append((i,cont))
    
listadelista=[] #Creamos una lista auxiliar. Es una lista que contiene 8 listas, una para cada categoría y dentro tenemos sus respectivos (idprod,#ventas)
for r in range(0,8):
    cate=[]
    for i in bus:
        if i[0] in sa[r]:
            cate.append(i)
    listadelista.append(cate)

ee=[]
for i in listadelista:
    i.sort(key=lambda x:x[1],reverse=0)
    ee.append(i[0:13]) #estos son los (idproduct,#ventas) menos comprados
fdd=dict(zip(cat,ee))
fdd #diccionario con categorías y sus productos ordenados de menos a más vendidos
#notemos como en algunas categorías hay más de 5 productos que no se vendieron



# In[12]:


tot=[] #lista para llamar los nombres de los productos anteriormente encontrados
for i in ee:
    menos=[]
    for k in i:
        menos.append(lifestore_products[k[0]-1][1])
    tot.append(menos) 


# In[15]:


print("Procesadores menos vendidos: ",[i.split(",")[0] for i in tot[0][0:5]] )


# In[16]:


print("Tarjetas de video menos vendidas: ",[i.split(",")[0] for i in tot[1][0:10]] )  #notar que ponemos 10 pues hay un empate en 0 tarjetas vendidas


# In[17]:


print("Tarjetas madre menos vendidas: ", [i.split(",")[0] for i in tot[2][0:12]])


# In[18]:


print("Discos duros menos vendidos: ",[i.split(",")[0] for i in tot[3][0:5]] )


# In[20]:


print("Memorias USB menos vendidas: ",[i.split(",")[0] for i in tot[4][0:2]] )


# In[21]:


print("Pantallas menos vendidas: ",[i.split(",")[0] for i in tot[5][0:10]] )


# In[22]:


print("Bocinas menos vendidas: ",[i.split(",")[0] for i in tot[6][0:9]])


# In[24]:


print("Audífonos menos vendidos: ",[i.split(",")[0] for i in tot[7][0:9]])


# In[28]:


#Para los productos con menores búsquedas por categoría hacemos un procedimiento similar:
lis=[]
for r in range(0,8):
    cate=[]
    for i in buscar:
        if i[0] in sa[r]:
            cate.append(i)
    lis.append(cate)
# "lis" es una lista que contiene 8 listas, una para cada categoría y dentro tenemos sus respectivos (idprod,#búsquedas)


# In[29]:


ei=[]
for i in lis:
    i.sort(key=lambda x:x[1],reverse=0)
    ei.append(i[0:13]) #estos son los (idproduct,#búsquedas) MENOS BUSCADOS
fdu=dict(zip(cat,ei))
fdu #diccionario con categorías y sus productos ordenados de menos a más buscados
#notemos como en algunas categorías hay más de 5 productos que no se vendieron


# In[30]:


to=[]
for i in ei:
    menos=[]
    for k in i:
        menos.append(lifestore_products[k[0]-1][1])
    to.append(menos)
# aquí tenemos una lista de listas donde vienen los nombres de los productos tal y como están ordenados en el diccionario de arriba


# In[32]:


print("Procesadores menos buscados: ",[i.split(",")[0] for i in to[0][0:10]] )


# In[33]:


print("Tarjetas de video menos buscadas: ",[i.split(",")[0] for i in to[1][0:10]] )


# In[36]:


print("Tarjetas madre menos buscadas: ",[i.split(",")[0] for i in to[2][0:11]] ) #la lista es de 11 elementos porque hay un empate donde el producto se buscó 1 vez


# In[38]:


print("Discos duros menos buscados: ",[i.split(",")[0] for i in to[3][0:10]] )


# In[39]:


print("Memorias USB menos buscadas: ",[i.split(",")[0] for i in to[4][0:10]] )


# In[40]:


print("Pantallas menos buscadas: ",[i.split(",")[0] for i in to[5][0:10]] )


# In[41]:


print("Bocinas menos buscadas: ",[i.split(",")[0] for i in to[6][0:10]] )


# In[43]:


print("Audífonos menos buscados: ",[i.split(",")[0] for i in to[7][0:10]] )


# In[45]:


## 2)Mostrar dos listados de 5 productos cada una, un listado para productos con las mejores reseñas y otro para las peores, considerando los productos con devolución.


# In[47]:


#Para los productos mejor reseñados sólo tomaremos en cuenta a los productos más vendidos así no tomamos en cuenta productos 
#sin reseñas pero sí consideraremos productos devueltos
ventasprod=[]
for i in idprod:
    cont=0
    for k in lifestore_sales:
        if k[1]==i:
            cont+=1
    ventasprod.append((i,cont)) #lista de tuplas donde se consideran productos devueltos (id_prod,#ventas)

final=[]
ventasprod.sort(key=lambda x:x[1],reverse=1)
ventasprod[:9] #nos vamos a quedar con los productos que tengan más de 10 ventas
for i in ventasprod[:9]:
    final.append(i[0])
final   #id_prod de los productos más vendidos, de estos seleccionaremos los 5 mejor reseñados
#usando el criterio del mayor porcentaje de 4 y 5 estrellas


# In[48]:


w=[]
for i in final:
    r=[]
    for k in lifestore_sales:
        if k[1]==i:
            r.append(k[2])
    w.append(r) #ya tenemos una lista de listas donde cada lista es para el idprod más vendido y adentro de estas tenemos sus calif.
por=[]
for i in w:
    n=0
    for k in i:
        if k==4 or k==5:
            n+=1
    por.append(n/len(i))
e=list(zip(final, por)) #tenemos una lista de tuplas donde se muestra (id_prod,porcentaje de calif. 4 o 5 )
e


# In[52]:


ds=[]
e.sort(key=lambda x:x[1],reverse=1)
for i in e[0:5]:
    ds.append(i[0])
#de esta forma ya tenemos los productos con mejores reseñas
#los productos con mejores reseñas son
mejoresreseñados=[]
for i in ds:
    for j in lifestore_products:
        if j[0]==i:
            mejoresreseñados.append(j[1])
print("Los productos mejor reseñados son: ",[i.split(",")[0] for i in mejoresreseñados])


# In[53]:


#del análisis anterior vemos que los 10 productos más vendidos tienen un índice alto de aprobación como se esperaba, ampliemos
#este análisis considerando los 20 más vendidos para así seleccionar los 5 productos peor reseñados


# In[62]:


final2=[]
ventasprod.sort(key=lambda x:x[1],reverse=1)
ventasprod[:20] #nos vamos a quedar con los productos que tengan más de 10 ventas
for i in ventasprod[:20]:
    final2.append(i[0])
#con final2 tenemos el id_prod de los productos más vendidos, de estos seleccionaremos los 5 peor reseñados
#usando el criterio del mayor porcentaje de 1 y 2 y 3 estrellas


# In[63]:


w=[]
for i in final2:
    r=[]
    for k in lifestore_sales:
        if k[1]==i:
            r.append(k[2])
    w.append(r)
#ya tenemos una lista de listas donde cada lista es para el idprod más vendido y adentro de estas tenemos sus calif.


# In[64]:


por=[]
for i in w:
    n=0
    for k in i:
        if k==1 or k==2 or k==3:
            n+=1
    por.append(n/len(i))
e=list(zip(final2, por)) #tenemos una lista de tuplas donde se muestra (id_prod,porcentaje de calif. 1 o 2 o 3 )


# In[69]:


ds=[]
e.sort(key=lambda x:x[1],reverse=1)
for i in e[0:6]:
    ds.append(i[0])  #aquí seleccionamos los peor reseñados y en la parte de abajo mostramos sus nombres

#los productos con peores reseñas son
peoresreseñados=[]
for i in ds:
    for j in lifestore_products:
        if j[0]==i:
            peoresreseñados.append(j[1])
print("Los productos peor reseñados son: ",[i.split(",")[0] for i in peoresreseñados])


# In[70]:


# 3)Total de ingresos y ventas promedio mensuales, total anual y meses con más ventas al año


# In[72]:


ventastot=[]
for i in idprod:
    cont=0
    for k in lifestore_sales:
        if k[-1]==0 and k[1]==i:
            cont+=1
    ventastot.append((i,float(cont*lifestore_products[i-1][2])))
#con ventastot generamos una lista de tuplas donde (idproducto,ingresostotales)
print("El total de ingresos para todos los años fue de: ","${:,.2f}".format(sum(n for _, n in ventastot)))


# In[73]:


#Para los totales anuales primero conozcamos cuántos años diferentes tenemos
years=[]
for i in lifestore_sales:
    years.append(i[3].split("/")[2])
years=list(dict.fromkeys(years))
years #tenemos 2 años, calculemos el total anual de ingresos para cada uno


# In[75]:


ventas19=[]
for i in idprod:
    cont=0
    for k in lifestore_sales:
        if k[-1]==0 and k[1]==i and (k[3].split("/")[2])=="2019":
            cont+=1
    ventas19.append((i,float(cont*lifestore_products[i-1][2])))
#ventas19 #generamos una lista de tuplas donde (idproducto,ingresostotales2020)
print("El total de ingresos para 2019 fue de: ","${:,.2f}".format(sum(n for _, n in ventas19)))


# In[76]:


ventas20=[]
for i in idprod:
    cont=0
    for k in lifestore_sales:
        if k[-1]==0 and k[1]==i and (k[3].split("/")[2])=="2020":
            cont+=1
    ventas20.append((i,float(cont*lifestore_products[i-1][2])))
#ventas20 #generamos una lista de tuplas donde (idproducto,ingresostotales2020)
print("El total de ingresos para 2020 fue de: ","${:,.2f}".format(sum(n for _, n in ventas20)))


# In[77]:


# Ahora calculemos el promedio de ventas mensuales 2020 pues en 2019 no tuvimos ventas
meses=[]
for i in lifestore_sales:
    meses.append(i[3].split("/")[1])
meses=list(dict.fromkeys(meses))
meses  #esos son los meses que tenemos


# In[78]:


km=[]
for i in meses:
    totales=[]
    for k in lifestore_sales:
        if k[-1]==0 and (k[3].split("/")[1])==i:
            totales.append(lifestore_products[k[1]][2])
    km.append((sum(totales),len(totales)))
#km,esta es una lista de tuplas con los (totales mensuales,#ventas mensuales)


# In[92]:


#los promedios mensuales
promedios=[]
for i in km:
    if i[0]!=0:
        promedios.append(i[0]/i[1])
    else:
        promedios.append(0)
#promedios nos sirve para calcular los promedios mensuales
mesventa=dict(zip(meses,promedios)) #diccionario con el número de mes y su respectiva venta promedio


# In[95]:


mesventa["10"]=0
mesventa["12"]=0
#primero insertamos los valores faltantes para que se muestren los 12 meses y así tenemos el diccionario con el número de mes y su respectiva venta promedio


# In[142]:


import pandas as pd
rt=pd.DataFrame(mesventa.values(),mesventa.keys(),columns = ['venta promedio por número de mes'])
rt


# In[144]:


eee=dict(zip(meses,[i[0] for i in km])) #diccionario con el número de mes y su respectivo ingreso total
eee["10"]=0
eee["12"]=0
rk=pd.DataFrame(eee.values(),eee.keys(),columns = ['venta total por número de mes'])
rk


# In[84]:


q=[(k, v) for k, v in eee.items()]
d=[]
q.sort(key=lambda x:x[1],reverse=1)
for i in q[0:5]:
    d.append(i[0])
d #estos son los 5 meses con más ventas ordenados de mayor a menor número de ventas


# In[155]:


import datetime  #llamamos a la biblioteca datetime para cambiar de forma rápida los números de mes por el nombre del mes
MV=[]
for i in d:
    datetime_object = datetime.datetime.strptime(i, "%m")
    month_name = datetime_object.strftime("%B")
    MV.append(month_name)
MV #los mismos meses de antes pero mostrando sus nombres:


# In[ ]:





# In[ ]:




