import pandas as pd
import folium


# Nosso primeiro mapa

# In[2]:


brasil = folium.Map(
    location=[-16.1237611, -59.9219642],
    zoom_start=4
)

# brasil.save('mapas_htmls/brasil_clean.html')
brasil


# ## Marcando pontos no mapa

# Lendo os dados

# In[3]:


empresas = pd.read_csv('empresas')
print(empresas.shape)
empresas.head(3)


# Colocando algumas empresas no mapa

# In[4]:


brasil_com_pontos = brasil

empresa1 = empresas.iloc[0]
folium.Marker(
    location=[empresa1['latitude'], empresa1['longitude']],
).add_to(brasil_com_pontos)

empresa2 = empresas.iloc[1]
folium.Marker(
    location=[empresa2['latitude'], empresa2['longitude']],
).add_to(brasil_com_pontos)

# brasil_com_pontos.save('mapas_htmls/brasil_some_companies.html')
brasil_com_pontos


# Colocar todas as empresas do nosso dataset no mapa pode não ser uma boa ideia.

# In[5]:


# # Descomentar e rodar esse código pode travar seu computador.
# # Faça por sua conta e risco ;P
# brasil_com_todas_empresas = brasil

# for _, empresa in empresas.iterrows():
#     folium.Marker(
#         location=[empresa['latitude'], empresa['longitude']],
#     ).add_to(brasil_com_todas_empresas)

# brasil_com_todas_empresas


#  Então vamos escolher apenas um estado:

# In[6]:


pernambuco = folium.Map(
    location=[-8.3833569, -38.5757127],
    zoom_start=7
)

# pernambuco.save('mapas_htmls/pernambuco_clean.html')
pernambuco


# In[7]:


empresas_pe = empresas[empresas['state'] == 'PE']
empresas.shape, empresas_pe.shape


# In[9]:


pernambuco = folium.Map(
    location=[-8.3833569, -38.5757127],
    zoom_start=7
)

for _, empresa in empresas_pe.iterrows():
    folium.Marker(
        location=[empresa['latitude'], empresa['longitude']],
    ).add_to(pernambuco)

# pernambuco.save('mapas_htmls/pernambuco_all_companies.html')
pernambuco


# Alguma cidade no litoral pernambucano

# In[10]:


empresas_olinda_pe = empresas[empresas['city'] == 'OLINDA']
empresas_olinda_pe.shape


# In[ ]:


olinda = folium.Map(
    location=[-7.9981267, -34.9082027],
    zoom_start=13
)
#
for _, empresa in empresas_olinda_pe.iterrows():
    folium.Marker(
        location=[empresa['latitude'], empresa['longitude']],
    ).add_to(olinda)

# olinda.save('mapas_htmls/olinda_all_companies.html')
olinda


# Colorindo de acordo com o bairro:

# In[11]:


empresas_olinda_pe.neighborhood.value_counts()


# In[12]:


colors = {
 'AMPARO': 'pink',
 'GUADALUPE': 'blue',
 'CASA CAIADA': 'green',
 'PEIXINHOS': 'orange',
 'RIO DOCE': 'red',
 'BAIRRO NOVO': 'purple',
}

olinda = folium.Map(
    location=[-7.9981267, -34.9082027],
    zoom_start=13
)

for _, empresa in empresas_olinda_pe.iterrows():
    if empresa['neighborhood'] in colors.keys():
        folium.Marker(
            location=[empresa['latitude'], empresa['longitude']],
            icon=folium.Icon(color=colors[empresa['neighborhood']])
        ).add_to(olinda)

# olinda.save('mapas_htmls/olinda_some_colored.html')
olinda


# In[13]:


folium.Marker(
    location=[empresa['latitude'], empresa['longitude']],
    popup='sou uma empresa de Olinda',
    icon=folium.Icon(color=colors[empresa['neighborhood']])
).add_to(olinda)


# In[ ]:




