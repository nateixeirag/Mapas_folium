#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd #importa o panda e o folium
import folium

brasil = folium.Map( #funcao para criar um mapa
    location=[-16.1237611, -59.9219642],    # Coordenadas retiradas do Google Maps
    zoom_start=4
)


# In[13]:


empresas = pd.read_csv('empresas')

empresa1 = empresas.loc[0]
folium.Marker(
    location=[empresa1['latitude'], empresa1['longitude']],
).add_to(brasil)


# In[14]:


empresa2 = empresas.iloc[1]
folium.Marker(
    location=[empresa2['latitude'], empresa2['longitude']],
).add_to(brasil)


# In[42]:


empresas_pr = empresas.loc[empresas.state =='PR']
empresas_pr = empresas_pr.loc[0:500,:]

#empresas_pr = empresas_p1
#empresas_pr = empresas_pr_1[empresas_pr_1['state'] == 'PR']


# In[43]:


parana = folium.Map(
    location=[ -25.3935,-51.4562],
    zoom_start=7
)

#parana


# In[41]:


for _, empresa in empresas_pr.iterrows():
    folium.Marker(
        location=[empresa['latitude'], empresa['longitude']],
    ).add_to(parana)

parana


# In[60]:


colors = {
 'CURITIBA': 'pink',
 'FOZ DO IGUACU': 'red',
 'LONDRINA': 'purple',
 'GUARAPUAVA': 'orange',
 'PONTA GROSSA': 'black',
}

for _, empresa in empresas_pr.iterrows():
    if empresa['city'] in colors.keys():
        folium.Marker(
            location=[empresa['latitude'], empresa['longitude']],
            icon=folium.Icon(color=colors[empresa['city']])
        )
    else:
        folium.Marker(
        location=[empresa['latitude'], empresa['longitude']],
        icon=folium.Icon(color='green')
    ).add_to(parana)


# In[72]:


cont = 0
for _, empresa in empresas_pr.iterrows():
    cont = cont + 1
    if empresa['city'] in colors.keys():
        test = folium.Html("<a href='https://www.ibge.gov.br/'> VISUALIZAR </a>", script=True)
        folium.Marker(
        location=[empresa['latitude'], empresa['longitude']],
        popup= folium.Popup(test),
        icon=folium.Icon(color=colors[empresa['city']])
    ).add_to(parana)
parana
parana.save('pr_some_colored.html')


# In[ ]:




