import streamlit as st
import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
import re
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from wordcloud import WordCloud
import os
import time
import numpy as np

# Configuration de la page
st.set_page_config(
    page_title="Transport Idéal ENSEA",
    page_icon="🚌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Définition des styles CSS personnalisés
st.markdown("""
<style>
    .main-title {
        text-align: center; 
        color: #1E88E5;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    
    .sub-title {
        text-align: center;
        color: #004D40;
        font-size: 24px;
        font-weight: bold;
    }
    
    .section-title {
        text-align: center;
        color: #333;
        font-size: 20px;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    
    .info-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f2f6;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    
    .metric-box {
        background-color: #0066cc;
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .offer-box {
        background-color: #f8f9fa;
        padding: 30px;
        border-radius: 15px;
        border: 2px solid #0066cc;
        text-align: center;
        margin: 20px 0;
    }
    
    .footer {
        text-align: center;
        margin-top: 40px;
        padding: 20px;
        background-color: #f8f9fa;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Fonction pour créer la page de garde (Partie 1)
def page_garde():
        
    # Création de trois colonnes pour les logos
    col1, col2, col3 = st.columns([1, 2, 1])

    import base64
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
             data = f.read()
        return base64.b64encode(data).decode()

# Convertir l'image en base64
    #img_base64 = get_base64_of_bin_file("NEW_LOGO_ENSEA_sans_fond.PNG")
    with col2:
        st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{img_base64}" width="200">
            <p style="font-weight: bold; margin-top: 0.5rem;">École Nationale Supérieure de Statistique et d'Économie Appliquée</p>
        </div>
        """,
        unsafe_allow_html=True
    )
  

    
    # Titre de l'étude
    st.markdown("<div class='main-title'>OFFRE  DE TRANSPORT IDÉALE POUR LES ÉTUDIANTS DE L'ENSEA</div>", unsafe_allow_html=True)
    
    # Encadré pour le nom du professeur
    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>SOUS LA SUPERVISION DE:</h3>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Mr COULIBALY M. Raymond</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Photos et noms de l'équipe
    st.markdown("<h3 style='text-align: center;'>ÉQUIPE</h3>", unsafe_allow_html=True)
    
    # Création de 4 colonnes pour les membres de l'équipe
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.image("HVAJM.jpeg", width=150, caption="HOUENOU VANGAH ")
    
    with col2:
        st.image("yoric.jpeg", width=135, caption="NGOUDJO KELL",)
    
    with col3:
        st.image("SAWADOGO.jpeg", width=150, caption="SAWADOGO ALBERT")
    
    with col4:
        st.image("AMAVI.jpeg", width=150, caption="TOMALOU AMAVI")
    
    
# Fonction pour créer la partie 2 (Contexte et justification)
def partie_2():
    st.title("CONTEXTE DE L'ÉTUDE")
    
    # Cadre 1: Contexte et justification de l'étude
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    #st.markdown("<h3>Contexte </h3>", unsafe_allow_html=True)
    st.write("""
    L'ENSEA (École Nationale Supérieure de Statistique et d'Économie Appliquée) accueille chaque année des centaines d'étudiants 
    venant de différentes régions de la Côte d'Ivoire et de l'étranger. Le transport quotidien entre le lieu de résidence et 
    l'établissement représente un défi majeur pour ces étudiants, impactant leur ponctualité, leur assiduité et leur bien-être.
    
    Cette étude vise à identifier les besoins spécifiques des étudiants en matière de transport et à proposer une offre de 
    service adaptée qui répond à leurs attentes tout en tenant compte des contraintes économiques, temporelles et géographiques.
    
    La pertinence de cette étude repose sur la nécessité d'améliorer les conditions d'études des étudiants de l'ENSEA en 
    facilitant leur mobilité quotidienne, facteur essentiel de leur réussite académique.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    st.title("OBJECTIFS DE L'ÉTUDE")
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)

    st.subheader("Objectif principal")

    st.write("""
    Identifier les caractéristiques d’une offre de transport optimale répondant aux besoins, préférences et contraintes des étudiants de l’ENSEA afin d’améliorer leur mobilité quotidienne et leur qualité de vie.
    """)

    st.subheader("Objectifs spécifiques")

    st.write("""
    1. Analyser les modes de transport actuellement utilisés par les étudiants et évaluer leur niveau de satisfaction.  
    2. Identifier les principaux critères de choix d’un mode de transport (coût, sécurité, accessibilité, ponctualité, confort, etc.).  
    3. Mesurer les difficultés rencontrées par les étudiants dans leurs déplacements quotidiens (retards, embouteillages, coût élevé, etc.).  
    4. Explorer les attentes des étudiants vis-à-vis d’une offre de transport idéale, notamment en termes de services complémentaires.  
    
    """)

    st.title("METHODOLOGIE DE L'ÉTUDE")
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    st.write("""
    1. Préparation d'un questionnaire de 21 questions sur Kobotoolbox.  
    2. Sensibilisaion de la population cible via des passages dans les classes.  
    3. Collecte des données par CAWI entre le 21/03 et le 02/04/2025.  
    4. Analyse des données à l'aide de Python et de bibliothèques telles que Pandas, Matplotlib et Plotly.  
    """)

    st.title("DONNEES")
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    
    # Cadre 2: Métriques de l'enquête
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='metric-box'<p style='font-size: 24px';>Individus captés / touchés </p> ", unsafe_allow_html=True)
        st.markdown("<h1 style='font-size: 48px;text-align:center'>118 / 147 étudiants</h1>", unsafe_allow_html=True)
        #st.markdown("<p>Individus enquêtés</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='metric-box'<p style='font-size: 24px';>Durée de la collecte </p> ", unsafe_allow_html=True)
        st.markdown("<h1 style='font-size: 48px;text-align:center'>02 Semaines</h1>", unsafe_allow_html=True)
        #st.markdown("<p>Individus enquêtés</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Graphiques relatifs à l'enquête
    st.markdown("<div class='section-title'><b>CARACTERISTIQUES SOCIO-DEMOGRAPHIQUES</b></div>", unsafe_allow_html=True)
    
    # Création de données fictives pour les graphiques
    col1, col2 = st.columns(2)
    data = pd.read_csv("cleaned_dataset.csv")

    # 🔎 Filtrage interactif
    

    # 🎨 Mise en page avec colonnes pour une meilleure présentation
    col1, col2 = st.columns(2)

    # Répartition par sexe
    with col1:
        
        sexe_counts = data["sex"].value_counts().reset_index()
        sexe_counts.columns = ['Sexe', 'Effectif']
        couleurs = {'masculin': '#4682B4', 'feminin': 'lightpink'}
        fig_sexe = px.pie(sexe_counts, names='Sexe', values='Effectif', color='Sexe',
                          color_discrete_map=couleurs, title="Répartition par Sexe")
        fig_sexe.update_layout(title_x=0.5, title_font=dict(size=20))
        st.plotly_chart(fig_sexe, use_container_width=True)

    # Répartition par âge
    with col2:
        
        age_counts = data['age'].value_counts().reset_index()
        age_counts.columns = ['Tranche d\'âge', 'Effectif']
        fig_age = px.bar(age_counts, x='Effectif', y='Tranche d\'âge', orientation='h',
                         text='Effectif', title="Répartition par Tranche d'âge",
                         color='Tranche d\'âge', color_discrete_sequence=px.colors.sequential.Blues_r)
        fig_age.update_layout(title_x=0.5, title_font_size=20)
        st.plotly_chart(fig_age, use_container_width=True)

    # Nouvelle ligne de colonnes
    col3, col4 = st.columns(2)

    # Répartition par nationalité
    with col3:
        
        nat_counts = data['nationality'].value_counts().reset_index()
        nat_counts.columns = ['Nationalité', 'Effectif']
        fig_nat = px.bar(nat_counts, y='Nationalité', x='Effectif', orientation='h',
                         text='Effectif', title="Répartition par Nationalité",
                         color_discrete_sequence=['#4682B4'])
        fig_nat.update_layout(title_x=0.5, title_font_size=20)
        st.plotly_chart(fig_nat, use_container_width=True)

    # Répartition par Filière et Classe
    with col4:
        
        liste = ["ISE" if val == "ise" else "AS" if val == "as" else None for val in data["course"].values]
        data["course"] = liste
        data_counts = data.groupby(['course', 'class']).size().reset_index(name='Effectif')
        colors = {
            'as1': '#1f77b4', 'as2': '#6baed6', 'as3': '#c6dbef',
            'ise1': '#ff7f0e', 'ise2': '#ffa07a', 'ise3': '#ffcc99'
        }
        fig_class = px.bar(data_counts, x='course', y='Effectif', color='class',
                           title="Répartition par Filière et Classe",
                           text='Effectif', barmode='stack', color_discrete_map=colors)
        fig_class.update_layout(title_x=0.5, title_font_size=20)
        st.plotly_chart(fig_class, use_container_width=True)



    # 📊 Ajout du tableau CSV ici
    st.markdown("<h3>Données détaillées de l'enquête</h3>", unsafe_allow_html=True)

    try:
        df = pd.read_csv("cleaned_dataset.csv")
        df = df.drop(columns=['Unnamed: 0'])
        st.dataframe(df, use_container_width=True)
    except FileNotFoundError:
        st.warning("Le fichier 'cleaned_dataset.csv' est introuvable. Veuillez vérifier le chemin du fichier.")


# Fonction pour créer la partie 3 (Analyses effectuées)

    
def partie_3():
    st.title("ANALYSES DES DONNEES")
    st.markdown("<div class='section-title'><b>Analyses approfondies pour déterminer l'offre idéale</b></div>", unsafe_allow_html=True)
    data = pd.read_csv("cleaned_dataset.csv")
    # 1. Services de transport utilisés
    col1, col2 = st.columns([2, 1])
    with col1:
        counts = data['main_service'].value_counts().reset_index()
        counts.columns = ['Service', 'Effectif']
        fig = px.bar(counts, x='Service', y='Effectif', text='Effectif',
                     color='Service', color_discrete_sequence=px.colors.qualitative.Pastel,
                     title="Services de transport utilisés")
        fig.update_layout(title_x=0.5, title_font=dict(size=22))
        fig.update_traces(textposition='auto')
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.markdown("""
        **Interprétation :**
        La majorité des étudiants utilisent les services de type yango, suivi des taxi rouges. Cela reflète les préférences actuelles basées sur la disponibilité et le coût.
        """)

    # 2. Durée moyenne actuelle du trajet
    col1, col2 = st.columns([2, 1])
    with col1:
        counts = data['mean_time'].value_counts().reset_index()
        counts.columns = ['Durée', 'Effectif']
        fig = px.bar(counts, x='Durée', y='Effectif', text='Effectif',
                     color='Durée', color_discrete_sequence=px.colors.qualitative.Vivid,
                     title="Durée moyenne actuelle du trajet")
        fig.update_layout(title_x=0.5, title_font=dict(size=22))
        fig.update_traces(textposition='auto')
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.markdown("""
        **Interprétation :**
        La majorité des trajets se situent entre 10 et 15 minutes, ce qui indique une localisation plutôt favorable des étudiants.
        """)

    # 3. Durée de trajet souhaitée
    col1, col2 = st.columns([2, 1])
    with col1:
        counts = data['mean_time_wanted'].value_counts().reset_index()
        counts.columns = ['Durée souhaitée', 'Effectif']
        fig = px.bar(counts, x='Durée souhaitée', y='Effectif', text='Effectif',
                     color='Durée souhaitée', color_discrete_sequence=px.colors.qualitative.Vivid,
                     title="Durée de trajet souhaitée")
        fig.update_layout(title_x=0.5, title_font=dict(size=22))
        fig.update_traces(textposition='auto')
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.markdown("""
        **Interprétation :**
        Les étudiants aimeraient idéalement des trajets de moins de 15 minutes, montrant une exigence forte sur la rapidité.
        """)

    # 4. Critère principal de choix du service
    col1, col2 = st.columns([2, 1])
    with col1:
        counts = data['criteria'].value_counts().reset_index()
        counts.columns = ['Critère', 'Effectif']
        fig = px.bar(counts, x='Critère', y='Effectif', text='Effectif',
                     color='Critère', color_discrete_sequence=px.colors.qualitative.Safe,
                     title="Critère principal de choix du service")
        fig.update_layout(title_x=0.5, title_font=dict(size=22))
        fig.update_traces(textposition='auto')
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.markdown("""
        **Interprétation :**
        Le prix ,la sécurité et la rapidité ressortent clairement comme les critères déterminants dans le choix du transport.
        """)
    
    def normaliser_terme(terme):
        equivalences = {
            'wi-fi': 'wifi', 'wi fi': 'wifi', 'wifi': 'wifi', 'Wifi': 'wifi', 'Wi-Fi': 'wifi', 'Wi-fi': 'wifi',
            'usb': 'usb', 'prise': 'usb', 'prise usb': 'usb', 'chargeur': 'usb',
            'eau': 'eau', "l'eau": 'eau',
            'clim': 'climatisation', 'climatisation': 'climatisation', 'climatisatio': 'climatisation', 'la clim': 'climatisation',
            'musique': 'musique'
        }
        return equivalences.get(terme.strip().lower(), terme.strip().lower())

    # === Liste des termes à exclure (stop words) ===
    STOP_WORDS = {"de", "des", "le", "la", "les", "et", "l'", "un", "une", "d'", "à", "au", "aux", "du"}

    # === Analyse des services avec exclusion des mots indésirables ===
    def analyser_services_simplifie(data, colonne):
        compteur = Counter()
        for val in data[colonne].dropna().astype(str):
            elements = re.split(r'[;,/\\|\n\s]+', val)  # Meilleure gestion des séparateurs
            services_uniques = set()
            for el in elements:
                el_clean = normaliser_terme(el)
                if el_clean and el_clean not in STOP_WORDS:  # Exclusion des mots indésirables
                    services_uniques.add(el_clean)
            for item in services_uniques:
                compteur[item] += 1
        return pd.DataFrame(compteur.items(), columns=["Service", "Occurrences"]).sort_values(by="Occurrences", ascending=False)

    # === Suppression des modalités composées si leurs éléments existent déjà ===
    def nettoyer_modalites_composes(data_services):
        services_exacts = set(data_services["Service"].values)
        lignes_a_supprimer = []
        for idx, service in data_services["Service"].items():
            composants = re.split(r'[\\s\\-_]+', service)
            composants = [c for c in composants if c in services_exacts and c != service]
            if len(composants) >= 2:
                lignes_a_supprimer.append(idx)
        return data_services.drop(lignes_a_supprimer).reset_index(drop=True)



        # === Application des traitements ===
    services_data = analyser_services_simplifie(data, 'other_services')
    services_data_final = nettoyer_modalites_composes(services_data)

    services = services_data_final["Service"].tolist()
    occurrences = services_data_final["Occurrences"].tolist()
    sizes = [10 + (o * 3) for o in occurrences]
    # 5. Souhait de services supplémentaires (Wordcloud)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Services additionnels souhaités")
        freq = dict(zip(services_data_final['Service'], services_data_final['Occurrences']))
        wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate_from_frequencies(freq)
        fig, ax = plt.subplots(figsize=(14, 7))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig, use_container_width=True)
    with col2:
        st.markdown("""
        **Interprétation :**
        Les étudiants souhaitent principalement des services offrant du wifi et de la climatisation à bord.
        """)

    # 6. Répartition des prix : Actuel vs Souhaité
    col1, col2 = st.columns([2, 1])

     #Nettoyage - garder seulement les modalités valides
    modalites_valides = ['moins_1000', 'frs_1000_1500', 'frs_1500_2000', 'plus_2000']

    data_clean = data[
        data['price_vehicle'].isin(modalites_valides) &
        data['price_wanted'].isin(modalites_valides)
    ].copy()

    # Ordonner les catégories
    ordre_categories = ['moins_1000', 'frs_1000_1500', 'frs_1500_2000', 'plus_2000']
    data_clean['price_vehicle'] = pd.Categorical(data_clean['price_vehicle'], categories=ordre_categories, ordered=True)
    data_clean['price_wanted'] = pd.Categorical(data_clean['price_wanted'], categories=ordre_categories, ordered=True)

    df_compare = pd.DataFrame({
    'Tranche de prix': ordre_categories * 2,
    'Proportion': [
        (data_clean['price_vehicle'] == cat).mean() for cat in ordre_categories
    ] + [
        (data_clean['price_wanted'] == cat).mean() for cat in ordre_categories
    ],
    'Type': ['Actuel']*4 + ['Souhaité']*4
        })
    with col1:
        fig = px.bar(df_compare,
                    x='Tranche de prix',
                    y='Proportion',
                    color='Type',
                    barmode='group',
                    title='Prix actuel vs souhaité',
                    labels={'Proportion': 'Proportion des répondants'},
                    color_discrete_map={'Actuel': '#e74c3c', 'Souhaité': '#2ecc71'})
        fig.update_layout(title_x=0.5, xaxis_title='Tranche de prix', yaxis_tickformat='.0%', plot_bgcolor='white', title_font_size=22)
        fig.update_traces(texttemplate='%{y:.0%}', textposition='outside')
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.markdown("""
        **Interprétation :**
        On note une forte aspiration pour des tarifs inférieur à 1000 FCFA, alors que les prix actuels dépassent souvent ce seuil.
        """)

    # Sexe × service utilisé
    col1, col2 = st.columns([2, 1])
    data = pd.read_csv("cleaned_dataset.csv")
    with col1:
        data_sexe_service = data[['sex', 'main_service']].dropna()
        data_sexe_service['sex'] = data_sexe_service['sex'].str.lower().str.strip()
        grouped = data_sexe_service.groupby(['sex', 'main_service']).size().reset_index(name='Effectif')
        color_map = {'masculin': '#4682B4', 'feminin': 'lightpink'}
        fig_sexe_service = px.bar(grouped, x='main_service', y='Effectif', color='sex', barmode='group',
                                text='Effectif',
                                title="Services de transport par sexe",
                                labels={'sex': 'Sexe', 'main_service': 'Service utilisé'},
                                color_discrete_map=color_map)
        fig_sexe_service.update_layout(title_x=0.5, title_font_size=22,
                                    xaxis_title="Service utilisé", yaxis_title="Nombre d'étudiants",
                                    legend_title="Sexe", height=500)
        fig_sexe_service.update_traces(textposition='outside')
        st.plotly_chart(fig_sexe_service, use_container_width=True)
    with col2:
        st.markdown("#### Interprétation")
        st.write("""
        Ceci présente une répartition de l'utilisation des services de transports actuels par sexe.On remarque que aucune fille de notre échantillon n'a l'habitude de marcher.
        """)

    # Classe d'âge × service
    col1, col2 = st.columns([2, 1])
    with col1:
        df = data.dropna(subset=['age', 'main_service'])
        grouped = df.groupby(['age', 'main_service'], observed=True).size().reset_index(name='Effectif')
        grouped.rename(columns={'age': 'Tranche d’âge'}, inplace=True)
        total_par_age = grouped.groupby('Tranche d’âge')['Effectif'].sum().reset_index(name='Total_Effectif')
        grouped = grouped.merge(total_par_age, on='Tranche d’âge')
        grouped['Proportion_ponderee'] = (grouped['Effectif'] / grouped['Total_Effectif']) * grouped['Total_Effectif']
        fig_age_service = px.bar(grouped,
                                x='Tranche d’âge',
                                y='Proportion_ponderee',
                                color='main_service',
                                title="Services de transport par âge",
                                labels={'main_service': 'Service de transport', 'Proportion_ponderee': 'Effectif pondéré'},
                                text=grouped['Effectif'].astype(str) + ' (' + (grouped['Effectif']/grouped['Total_Effectif']*100).round(1).astype(str) + '%)',
                                barmode='stack',
                                height=500,
                                color_discrete_sequence=px.colors.qualitative.Vivid)
        fig_age_service.update_layout(title_x=0.5,
                                    title_font_size=22,
                                    xaxis_title="Tranche d’âge",
                                    yaxis_title="Effectif pondéré")
        fig_age_service.update_traces(textposition='inside')
        st.plotly_chart(fig_age_service, use_container_width=True)
    with col2:
        st.markdown("#### Interprétation")
        st.write("""
        Ce graphique illustre les services de transport privilégiés selon les tranches d’âge avec le service Yango étant majoritaire dans tous les cas.
        """)

    # Critère de choix selon sexe
    col1, col2 = st.columns([2, 1])
    with col1:
        data['sex'] = data['sex'].str.lower().str.strip()
        df = data.dropna(subset=['sex', 'criteria'])
        grouped = df.groupby(['sex', 'criteria'], observed=True).size().reset_index(name='Effectif')
        total_par_sexe = grouped.groupby('sex')['Effectif'].transform('sum')
        grouped['Proportion'] = grouped['Effectif'] / total_par_sexe * 100
        fig_critere_sexe = px.bar(grouped, y='sex', x='Proportion', color='criteria',
                                title="Critères de choix du transport selon le sexe",
                                labels={'sex': 'Sexe', 'criteria': 'Critère de choix'},
                                text=grouped['Proportion'].round(1).astype(str) + '%',
                                orientation='h', barmode='stack',
                                color_discrete_sequence=px.colors.qualitative.Prism)
        fig_critere_sexe.update_layout(title_x=0.5, title_font_size=22,
                                    xaxis_title="Part (%) des critères", yaxis_title="Sexe",
                                    height=500)
        fig_critere_sexe.update_traces(textposition='inside')
        st.plotly_chart(fig_critere_sexe, use_container_width=True)
    with col2:
        st.markdown("#### Interprétation")
        st.write("""
        Les priorités de sélection d'un transport varient selon le sexe.
        Cela permet de cibler les arguments commerciaux selon le public, le prix étant toujours prédominant dans chaque sexe mais la sécurité ressortant plus chez les femmes.
        """)

    # Type de véhicule selon critère principal
    col1, col2 = st.columns([2, 1])
    with col1:
        data['criteria'] = data['criteria'].str.lower().str.strip()
        data['vehicle_type'] = data['vehicle_type'].str.lower().str.strip()
        df1 = data.dropna(subset=['criteria', 'vehicle_type'])
        grouped1 = df1.groupby(['criteria', 'vehicle_type'], observed=True).size().reset_index(name='Effectif')
        total_criteria = grouped1.groupby('criteria')['Effectif'].transform('sum')
        grouped1['Proportion'] = grouped1['Effectif'] / total_criteria * 100
        fig_vehicule_critere = px.bar(grouped1, y='criteria', x='Proportion', color='vehicle_type',
                                    title="Type de véhicule selon le critère",
                                    text=grouped1['Proportion'].round(1).astype(str) + '%',
                                    orientation='h', barmode='stack',
                                    color_discrete_sequence=px.colors.qualitative.Set2)
        fig_vehicule_critere.update_layout(title_x=0.5, title_font_size=22,
                                        xaxis_title="Part (%)", yaxis_title="Critère de choix")
        fig_vehicule_critere.update_traces(textposition='inside')
        st.plotly_chart(fig_vehicule_critere, use_container_width=True)
    with col2:
        st.markdown("#### Interprétation")
        st.write("""
        Les préférences en matière de véhicule sont étroitement liées aux critères de choix prioritaires.
        Ce graphique aide à aligner l’offre sur les attentes des étudiants.
        """)

    # Transport en soirée par classe
    col1, col2 = st.columns([2, 1])
    with col1:
        data['even_transport'] = data['even_transport'].str.lower().str.strip()
        data['class'] = data['class'].astype(str).str.strip()
        df_even = data.dropna(subset=['even_transport', 'class'])
        grouped_even = df_even.groupby(['class', 'even_transport'], observed=True).size().reset_index(name='Effectif')
        total_par_classe = grouped_even.groupby('class')['Effectif'].transform('sum')
        grouped_even['Proportion'] = grouped_even['Effectif'] / total_par_classe * 100
        fig_soiree_classe = px.bar(grouped_even, x='class', y='Proportion', color='even_transport',
                                title="Transport en soirée selon la classe",
                                text=grouped_even['Proportion'].round(1).astype(str) + '%',
                                barmode='group',
                                labels={'class': 'Classe', 'even_transport': 'Souhaite un transport en soirée'},
                                color_discrete_sequence=px.colors.qualitative.Bold)
        fig_soiree_classe.update_layout(title_x=0.5, title_font_size=22,
                                        yaxis_title="Part (%)", xaxis_title="Classe",
                                        height=500)
        fig_soiree_classe.update_traces(textposition='outside')
        st.plotly_chart(fig_soiree_classe, use_container_width=True)
    with col2:
        st.markdown("#### Interprétation")
        st.write("""
        Certaines classes expriment une demande plus forte pour des services de transport en soirée.
        Cela reflète leurs contraintes horaires spécifiques.
        """)

    # Score NPS global
    col1, col2 = st.columns([2, 1])
    with col1:
        data_clean = data[['main_service', 'nps']].dropna()
        data_clean['nps'] = pd.to_numeric(data_clean['nps'], errors='coerce')
        data_clean = data_clean.dropna()
        def classify_nps(score):
            if score >= 9:
                return 'Promoteur'
            elif score >= 7:
                return 'Passif'
            else:
                return 'Détracteur'
        data_clean['NPS_category'] = data_clean['nps'].apply(classify_nps)
        def compute_nps(group):
            total = len(group)
            promoters = len(group[group == 'Promoteur'])
            detractors = len(group[group == 'Détracteur'])
            return round(((promoters - detractors) / total) * 100, 1)
        nps_by_service = data_clean.groupby('main_service')['NPS_category'].apply(compute_nps).reset_index()
        nps_by_service.columns = ['Service', 'NPS']
        fig_nps_global = px.bar(nps_by_service, x='Service', y='NPS', text='NPS',
                                title='Score NPS global par service',
                                color='NPS', color_continuous_scale='Tealgrn')
        fig_nps_global.update_traces(textposition='outside')
        fig_nps_global.update_layout(title_x=0.5, title_font_size=22,
                                    yaxis_title='Score NPS', xaxis_title='Service',
                                    height=500)
        st.plotly_chart(fig_nps_global, use_container_width=True)
    with col2:
        st.markdown("#### Interprétation")
        st.write("""
        Le score NPS est un excellent indicateur de la satisfaction globale des services.
        Les services avec un score négatif méritent une attention particulière pour améliorer l’expérience client.
        """)

    # Répartition des catégories NPS par service
    col1, col2 = st.columns([2, 1])
    with col1:
        nps_grouped = data_clean.groupby(['main_service', 'NPS_category']).size().reset_index(name='count')
        fig_nps_detail = px.bar(nps_grouped, x='main_service', y='count', color='NPS_category', text='count',
                                title="Répartition des catégories par service",
                                color_discrete_map={'Détracteur': 'red', 'Passif': 'orange', 'Promoteur': 'green'})
        fig_nps_detail.update_layout(barmode='stack', title_x=0.5, title_font_size=20,
                                    xaxis_title="Service", yaxis_title="Nombre d'étudiants",
                                    height=500)
        st.plotly_chart(fig_nps_detail, use_container_width=True)
    with col2:
        st.markdown("#### Interprétation")
        st.write("""
        Ce graphique détaillé complète l’analyse du NPS.
        Il permet de visualiser la proportion de promoteurs, passifs et détracteurs par service.
        """)


        # 👉🏼 Si tu veux, je peux te préparer toute la suite complète dans ce format homogène, tu auras un rendu ultra propre, comme une vraie application pro de dataviz 🎨🚀


    # Veux-tu que je te finalise absolument tout jusqu’au dernier graphique dans ce style ? ✅

    # Fonction pour créer la partie 4 (Présentation de l'offre)
def partie_4():
    st.title("PRÉSENTATION DE L'OFFRE")
    
    # Logo de l'entreprise
    col1, col2, col3 = st.columns([1, 2, 1])
    
    # Cadre esthétique pour l'offre
    st.markdown("<div class='offer-box'>", unsafe_allow_html=True)
    st.markdown("<h2>L'entreprise <span style='color: #0066cc;'>TRANSEA</span> vous présente son offre de transport</h2>", unsafe_allow_html=True)
    
    # Bouton pour afficher l'offre
    if st.button("Afficher l'offre", key="afficher_offre"):
        # Animation de chargement
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        st.success("Offre chargée avec succès!")
        
        st.title("🚍 Navettes ENSEA Premium")
        st.markdown("<h3 style='text-align: center; color: #1E90FF;'>Rapide, sécurisé, connecté – Votre mobilité étudiante réinventée</h3>", unsafe_allow_html=True)

        # Concept-Produit
        st.subheader("✨ Pourquoi Navettes ENSEA Premium ?")
        st.markdown("""
        *Concept :* Un transport étudiant rapide, sécurisé et connecté, conçu pour l’ENSEA.  
        *Objectif :* Simplifier vos trajets quotidiens avec une solution abordable et moderne.
        """)
        st.markdown("---")

        # Formule Flexible
        st.subheader("💵 Une formule adaptée à vos besoins")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("#### Tarif : 1200 FCFA")
            st.write("*Avantage :* Flexibilité pour vos trajets occasionnels.")
            st.write("*Argument :* Prix dans la fourchette 1000-1500 FCFA, plébiscitée par les étudiants pour rester accessible.")
        with col2:
            st.markdown("#### Abonnement : 20 000 FCFA / 20 trajets")
            st.write("*Avantage :* Économies pour les utilisateurs réguliers.")
            st.write("*Argument :* Tarif réduit à ~1000 FCFA/trajet, répondant à l’aspiration budgétaire des étudiants.")
        with col3:
            st.markdown("#### Formule Soirée : 1500 FCFA")
            st.write("*Avantage :* Sécurité pour vos retours tardifs.")
            st.write("*Argument :* Répond au besoin de trajets sécurisés en soirée, apprécié par tous.")
        st.write("Paiement simplifié via mobile money ou notre appli.")
        st.markdown("---")

        # Package Premium
        st.subheader("📦 Ce que vous offre notre package")
        col4, col5, col6 = st.columns(3)
        with col4:
            st.markdown("#### Rapidité")
            st.write("Départs toutes les 15-30 min.")
            st.write("*Avantage :* Ponctualité garantie pour vos cours.")
            st.write("*Argument :* Identifié comme critère clé par les étudiants pour arriver à l’heure.")
        with col5:
            st.markdown("#### Connectivité")
            st.write("Wi-Fi gratuit + ports USB.")
            st.write("*Avantage :* Restez productif ou détendu.")
            st.write("*Argument :* Répond à la forte demande de Wi-Fi à bord pour travailler ou se connecter.")
        with col6:
            st.markdown("#### Confort & Assistance")
            st.write("Climatisation + suivi en temps réel + support réactif.")
            st.write("*Avantage :* Voyagez sereinement.")
            st.write("*Argument :* Service client réactif et suivi plébiscités pour une expérience fluide.")
        st.markdown("---")

        # Services Associés
        st.subheader("📱 Des services qui font la différence")
        col7, col8, col9 = st.columns(3)
        with col7:
            st.markdown("#### Application Mobile")
            st.write("Réservation, suivi, support.")
            st.write("*Avantage :* Tout à portée de main.")
            st.write("*Argument :* Application de suivi demandée pour planifier vos trajets facilement.")
        with col8:
            st.markdown("#### Sécurité Renforcée")
            st.write("*Avantage :* Rentrez sans souci.")
            st.write("*Argument :* Répond aux besoins de sécurité, notamment en soirée.")
        with col9:
            st.markdown("#### Adapté à Tous")
            st.write("Personnalisation genrée.")
            st.write("*Avantage :* Une offre qui vous ressemble.")
            st.write("*Argument :* Les différences de préférences entre garçons et filles sont prises en compte.")
        st.markdown("---")

        # Tableau récapitulatif
        st.subheader("Tout en un coup d’œil")
        data = {
            "Élément": ["Tarif", "Abonnement", "Soirée", "Rapidité", "Connectivité", "Confort", "Appli", "Sécurité"],
            "Détail": ["1200 FCFA", "20 000 FCFA/20 trajets", "1500 FCFA", "Départs fréquents", "Wi-Fi + USB", "Climatisation", "Suivi + réservation", "Nuit sécurisée"],
            "Bénéfice": ["Flexibilité", "Économies", "Sérénité", "Ponctualité", "Productivité", "Bien-être", "Commodité", "Confiance"],
            "Argument": ["Prix accessible", "Budget étudiant", "Retours tardifs", "Critère clé", "Demande forte", "Service réactif", "Planification", "Besoin sécurité"]
        }
        st.table(data)

        # Synthèse
        st.subheader("En résumé")
        st.markdown("""
        *Navettes ENSEA Premium* :  
        - *Prix* : 1200 FCFA/trajet ou 20 000 FCFA/20 trajets.  
        - *Service* : Navettes fréquentes, connectées, confortables, avec suivi et sécurité.  
        - *Promesse* : Une mobilité simple, abordable et adaptée à vos besoins, validée par vos attentes.
        """, unsafe_allow_html=True)

# Fonction principale pour gérer la navigation entre les pages
def main():
    # Initialisation des query params pour la navigation
    params = st.query_params

    # Sidebar avec logo personnalisé
    with st.sidebar:
        #st.image("transea.jpeg", width=200)  # Ton logo

        #st.markdown("<h2 style='margin-top: 20px;'>Navigation</h2>", unsafe_allow_html=True)

        # Menu de navigation avec mise à jour des paramètres d'URL
        if st.button("ACCUEIL"):
            st.query_params.page = "garde"
        if st.button("CONTEXTE & MEHODOLOGIE"):
            st.query_params.page = "contexte"
        if st.button("ANALYSES"):
            st.query_params.page = "analyses"
        if st.button("PRESENTATION DE L'OFFRE"):
            st.query_params.page = "offre"

    # Lecture du paramètre actuel
    page = params.get("page", "garde")

    # Affichage de la page sélectionnée
    if page == "garde":
        page_garde()
    elif page == "contexte":
        partie_2()
    elif page == "analyses":
        partie_3()
    elif page == "offre":
        partie_4()

    # Pied de page
    st.markdown("---")
    st.markdown("<div class='footer'>© 2025 - Projet réalisé dans le cadre de l'application du cours de Marketing à l'ENSEA</div>", unsafe_allow_html=True)

    # Exécution de l'application
if __name__ == "__main__":
    main()
