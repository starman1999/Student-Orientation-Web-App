import random

etudiants = [
    {
        'name': 'Mounir',
        'matricule': '171736003461',
    },
    {
        'name': 'Assem',
        'matricule': '171835027186',
    },
    {
        'name': 'Djouss',
        'matricule': '1718212121',
    },

]

specialities = [
    {
        'name': 'SII',
    },
    {
        'name': 'RSD',
    },
    {
        'name': 'IL',
    },
    {
        'name':'MIV'
    },
    {
        'name':'SSI'
    },
    {
        'name':'BIGDATAA'
    },
    {
        'name':'BIOINFO'
    },

]

modules = [
    {
        'name': 'Archi 01',
    },
    {
        'name': 'Algo',
    },
    {
        'name': 'SI',
    },
    {
        'name':'Analyse Numérique'
    },
    {
        'name':'Proba Stat'
    },
    {
        'name':'Logique.M'
    },
    {
        'name':'anglais'
    },
    {
        'name':'POO'
    },
    {
        'name':'BDD'
    },
    {
        'name':'Théorie des languages'
    },
    {
        'name':'SE 01'
    },
    {
        'name':'Archi02'
    },
    {
        'name':'SE 02'
    },
    {
        'name':'Réseau'
    },
    {
        'name':'Compilation'
    },
    {
        'name':'GL'
    },
    {
        'name': 'THG'
    },
    {
        'name': 'GL'
    },

]

moyennes = [
    {
        'etudiant_id': random.randint(1, 3),
        'module_id': random.randint(1, 17),
        'moyenne': random.uniform(4, 16),
    },
    {
        'etudiant_id': random.randint(1, 3),
        'module_id': random.randint(1, 17),
        'moyenne': random.uniform(4, 16),
    },
    {
        'etudiant_id': random.randint(1, 3),
        'module_id': random.randint(1, 17),
        'moyenne': random.uniform(4, 16),
    },

]





