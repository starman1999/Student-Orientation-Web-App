# import psycopg2
#
# conn = psycopg2.connect(
#      database="orient",
#      user="root",
#      password="toor",
#      host="localhost",
#      port='5432'
# )
# cur = conn.cursor()
# cur.execute("SELECT etudiants.id, etudiants.name, etudiants.matricule FROM etudiants")
# cur.execute("JOIN Moyenne on (etudiants.id= Moyenne.etudiant_id")
# cur.execute("JOIN modules on (module.id= Moyenne.module_id")
#
# conn.commit()
#
#
