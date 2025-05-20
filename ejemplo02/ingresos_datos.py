from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# 1. Insertar los clubes desde el txt que el profe nos dio
with open("data/datos_clubs.txt", encoding="utf-8") as archivo_clubs:
    for linea in archivo_clubs:
        datos = linea.strip().split(";")
        nombre = datos[0]
        deporte = datos[1]
        fundacion = int(datos[2])
#Creo el objeto de club
        club = Club(nombre=nombre, deporte=deporte, fundacion=fundacion)
        session.add(club)

# Confirmar para que los clubes estén disponibles para consulta
session.commit()

# Inserto los jugadores desde el archivo txt que nos dio el profe
with open("data/datos_jugadores.txt", encoding="utf-8") as archivo_jugadores:
    for linea in archivo_jugadores:
        datos = linea.strip().split(";")
        nombre_club = datos[0]
        posicion = datos[1]
        dorsal = int(datos[2])
        nombre_jugador = datos[3]

        # Busca el club al que pertenece el jugador
        club = session.query(Club).filter_by(nombre=nombre_club).one()

        jugador = Jugador(
            nombre=nombre_jugador,
            dorsal=dorsal,
            posicion=posicion,
            club=club
        )
        session.add(jugador)

# Confirmar la inserción de los jugadores de fut
session.commit()
