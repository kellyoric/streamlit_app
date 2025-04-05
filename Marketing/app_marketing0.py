import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
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
    st.title("PAGE DE GARDE")
    
    # Création de trois colonnes pour les logos
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col1:
        # Logo de la Côte d'Ivoire à gauche
        st.image("Logo_CI.jpg", width=150, caption="Armoiries de la Côte d'Ivoire")
    
    with col3:
        # Logo de l'ENSEA à droite
        st.image("DAS.JPEG", width=150, caption="DIVISION DES ANALYSE STATISTICIEN")
    
    # Titre de l'étude
    st.markdown("<div class='main-title'>OFFRE TRANSPORT IDÉAL DE TRANSPORT POUR LES ÉTUDIANTS DE L'ENSEA</div>", unsafe_allow_html=True)
    
    # Encadré pour le nom du professeur
    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>SOUS LA DIRECTION DE:</h3>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Mr MOUSSA K. COULIBALY</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Photos et noms de l'équipe
    st.markdown("<h3 style='text-align: center;'>L'ÉQUIPE:</h3>", unsafe_allow_html=True)
    
    # Création de 4 colonnes pour les membres de l'équipe
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.image("HVAJM.jpeg", width=150, caption="NOM Prénom 1")
    
    with col2:
        st.image("KELL.jpeg", width=150, caption="NOM Prénom 2")
    
    with col3:
        st.image("SAWADOGO.jpeg", width=150, caption="NOM Prénom 3")
    
    with col4:
        st.image("AMAVI.jpeg", width=150, caption="NOM Prénom 4")
    
    # Logo et nom de l'entreprise en bas
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("transport.webp", width=120)
        st.markdown("<div style='text-align: center; font-weight: bold;'>NOM DE L'ENTREPRISE</div>", unsafe_allow_html=True)

# Fonction pour créer la partie 2 (Contexte et justification)
def partie_2():
    st.title("CONTEXTE ET JUSTIFICATION DE L'ÉTUDE")
    
    # Cadre 1: Contexte et justification de l'étude
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    st.markdown("<h3>Contexte et justification</h3>", unsafe_allow_html=True)
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
    
    # Cadre 2: Métriques de l'enquête
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
        st.markdown("<h1 style='font-size: 48px;'>250</h1>", unsafe_allow_html=True)
        st.markdown("<p>Individus enquêtés</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
        st.markdown("<h1 style='font-size: 48px;'>2 semaines</h1>", unsafe_allow_html=True)
        st.markdown("<p>Durée de la collecte</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Graphiques relatifs à l'enquête
    st.markdown("<div class='section-title'>Résultats de l'enquête</div>", unsafe_allow_html=True)
    
    # Création de données fictives pour les graphiques
    col1, col2 = st.columns(2)
    
    with col1:
        # Graphique 1: Répartition des modes de transport actuels
        fig1, ax1 = plt.subplots(figsize=(8, 6))
        transport_modes = ['Bus public', 'Taxi collectif', 'Voiture personnelle', 'Moto', 'À pied']
        transport_values = [45, 25, 10, 15, 5]
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
        ax1.pie(transport_values, labels=transport_modes, autopct='%1.1f%%', startangle=90, colors=colors)
        ax1.axis('equal')
        plt.title('Répartition des modes de transport actuels')
        st.pyplot(fig1)
    
    with col2:
        # Graphique 2: Satisfaction avec le transport actuel
        fig2, ax2 = plt.subplots(figsize=(8, 6))
        satisfaction = ['Très satisfait', 'Satisfait', 'Neutre', 'Insatisfait', 'Très insatisfait']
        satisfaction_values = [5, 15, 20, 40, 20]
        ax2.bar(satisfaction, satisfaction_values, color='#1f77b4')
        plt.title('Niveau de satisfaction avec le transport actuel')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(fig2)
    
    # Graphique 3: Durée moyenne du trajet
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    travel_time = ['< 15 min', '15-30 min', '30-45 min', '45-60 min', '> 60 min']
    travel_time_values = [10, 25, 30, 25, 10]
    ax3.bar(travel_time, travel_time_values, color='#2ca02c')
    plt.title('Durée moyenne du trajet domicile-école')
    plt.ylabel('Pourcentage d\'étudiants')
    plt.tight_layout()
    st.pyplot(fig3)

# Fonction pour créer la partie 3 (Analyses effectuées)
def partie_3():
    st.title("ANALYSES EFFECTUÉES")
    
    st.markdown("<div class='section-title'>Analyses approfondies pour déterminer l'offre idéale</div>", unsafe_allow_html=True)
    
    # Graphiques supplémentaires pour les analyses
    col1, col2 = st.columns(2)
    
    with col1:
        # Graphique 1: Budget mensuel pour le transport
        fig1, ax1 = plt.subplots(figsize=(8, 6))
        budget_ranges = ['< 5000 FCFA', '5000-10000 FCFA', '10000-15000 FCFA', '15000-20000 FCFA', '> 20000 FCFA']
        budget_values = [15, 35, 30, 15, 5]
        ax1.bar(budget_ranges, budget_values, color='#1f77b4')
        plt.title('Budget mensuel alloué au transport')
        plt.ylabel('Pourcentage d\'étudiants')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(fig1)
    
    with col2:
        # Graphique 2: Préférences horaires
        fig2, ax2 = plt.subplots(figsize=(8, 6))
        x = np.array(['6h-7h', '7h-8h', '8h-9h', '16h-17h', '17h-18h', '18h-19h', '19h-20h'])
        y = np.array([20, 40, 15, 10, 25, 35, 15])
        ax2.plot(x, y, marker='o', linewidth=2, markersize=10, color='#ff7f0e')
        plt.title('Préférences horaires pour les déplacements')
        plt.ylabel('Nombre d\'étudiants')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(fig2)
    
    # Graphique 3: Zones de résidence
    st.markdown("<h3>Répartition géographique des étudiants</h3>", unsafe_allow_html=True)
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    quartiers = ['Cocody', 'Abobo', 'Yopougon', 'Adjamé', 'Plateau', 'Treichville', 'Marcory', 'Koumassi', 'Port-Bouët']
    etudiants = [30, 15, 20, 10, 5, 5, 8, 4, 3]
    ax3.barh(quartiers, etudiants, color='#2ca02c')
    plt.title('Répartition des étudiants par quartier de résidence')
    plt.xlabel('Pourcentage d\'étudiants')
    plt.tight_layout()
    st.pyplot(fig3)
    
    # Graphique 4: Facteurs importants pour le choix du transport
    st.markdown("<h3>Facteurs déterminants dans le choix du transport</h3>", unsafe_allow_html=True)
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    factors = ['Prix', 'Ponctualité', 'Confort', 'Sécurité', 'Rapidité', 'Flexibilité horaire']
    importance = [4.8, 4.5, 3.9, 4.7, 4.2, 3.8]
    ax4.bar(factors, importance, color='#d62728')
    plt.title('Importance des facteurs (sur une échelle de 1 à 5)')
    plt.ylim(0, 5)
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(fig4)

# Fonction pour créer la partie 4 (Présentation de l'offre)
def partie_4():
    st.title("PRÉSENTATION DE L'OFFRE")
    
    # Logo de l'entreprise
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("transport.webp", width=150)
    
    # Cadre esthétique pour l'offre
    st.markdown("<div class='offer-box'>", unsafe_allow_html=True)
    st.markdown("<h2>L'entreprise <span style='color: #0066cc;'>TransportENSEA</span> vous présente son offre de transport</h2>", unsafe_allow_html=True)
    
    # Bouton pour afficher l'offre
    if st.button("Afficher l'offre", key="afficher_offre"):
        # Animation de chargement
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        st.success("Offre chargée avec succès!")
        
        # Tableau de l'offre
        offre_data = {
            "Caractéristiques": ["Concept-Produit", "Formule", "Package", "Service associé", "Marque"],
            "Description": [
                "Service de navette dédiée aux étudiants de l'ENSEA avec des horaires fixes adaptés aux emplois du temps académiques",
                "Abonnement mensuel à 12000 FCFA ou abonnement trimestriel à 32000 FCFA avec passages à 7h, 12h30, 14h et 18h",
                "Accès à l'application mobile de suivi en temps réel + WiFi gratuit à bord + espace de rangement pour les effets personnels",
                "Assistance téléphonique 24/7 + service de réclamation en ligne + programme de fidélité",
                "TransportENSEA"
            ]
        }
        
        df = pd.DataFrame(offre_data)
        
        # Style pour le tableau
        st.markdown("""
        <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th {
            background-color: #0066cc;
            color: white;
            text-align: left;
            padding: 12px;
        }
        td {
            text-align: left;
            padding: 12px;
            border-bottom: 1px solid #ddd;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        tr:hover {
            background-color: #ddd;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Affichage du tableau
        st.table(df)
        
        # Image pour la marque (remplacer par l'image réelle de la marque)
        st.image("transport.webp", width=200, caption="Logo de la marque TransportENSEA")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Fonction principale pour gérer la navigation entre les pages
def main():
    # Création d'une barre latérale pour la navigation
    st.sidebar.title("Navigation")
    pages = ["Page de Garde", "Contexte et Justification", "Analyses Effectuées", "Présentation de l'Offre"]
    choice = st.sidebar.radio("Aller à:", pages)
    
    # Affichage de la page sélectionnée
    if choice == "Page de Garde":
        page_garde()
    elif choice == "Contexte et Justification":
        partie_2()
    elif choice == "Analyses Effectuées":
        partie_3()
    elif choice == "Présentation de l'Offre":
        partie_4()
    
    # Pied de page
    st.markdown("---")
    st.markdown("<div class='footer'>© 2025 - Projet réalisé dans le cadre des études à l'ENSEA</div>", unsafe_allow_html=True)

# Exécution de l'application
if __name__ == "__main__":
    main()