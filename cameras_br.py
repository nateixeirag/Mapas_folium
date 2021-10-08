import pandas as pd #importa o panda e o folium
import folium

brasil = folium.Map( #funcao para criar um mapa
    location=[-16.1237611, -59.9219642],    # Coordenadas retiradas do Google Maps
    zoom_start=6
)


# In[13]:


cameras_br_localizacao = pd.read_csv('pontos_passagem.csv',sep=";");

def columns_renamer(dataframe):  # funcao para renomear as colunas
    ##### ALTERAR NOME DAS COLUNAS #####
    cols = dataframe.columns
    coluna_zero = cols[0];
    print(coluna_zero)
    print((type(coluna_zero)))
    #coluna_zero.replace(' ',"_")
    dataframe.rename(coluna_zero, 'Pontos_Arquivo', inplace=True)

    return dataframe

#cameras_br_localizacao = columns_renamer(cameras_br_localizacao);

#cameras_br_localizacao = cameras_br.loc[:, ['Lat_1','Lon_1']]

print(cameras_br_localizacao)

#for _, camera in cameras_br_localizacao.iterrows():
#   folium.Marker(
#       location=[camera['Lat_1'], camera['Lon_1']],
#  ).add_to(brasil)

url_lat= {
    float('-25.546944'): 'pin-yellow.png',
    float('-25.084119'): 'pin-yellow.png',
    float('-25.427135'): 'pin-yellow.png',
    float('-23.16759'): 'pin-yellow.png',
    float('-25.465857'): 'pin-red.png',
    float('-23.789359'): 'pin-red.png',
    float('-23.820685'): 'pin-yellow.png',
}

for _, camera in cameras_br_localizacao.iterrows():
    if camera['Lat_1'] in url_lat.keys():
        folium.Marker(
            location=[camera['Lat_1'], camera['Lon_1']],
            #icon= folium.Icon(color=url_lat[camera['Lat_1']], size=15),
            icon = folium.features.CustomIcon(url_lat[camera['Lat_1']],icon_size=(30,30)),
            popup = folium.Popup(camera['Ponto Arquivo'])
        ).add_to(brasil)
    else:
        folium.Marker(
            location=[camera['Lat_1'], camera['Lon_1']],
            popup=folium.Popup(camera['Ponto Arquivo']),
            icon = folium.features.CustomIcon('pin-blue.png',icon_size=(27,27)),
    ).add_to(brasil)

brasil
brasil.save('cameras_br.html')
