
import random  
import time   

# --- FUNCIÓN AUXILIAR ---

def pausa():
    """Hace una pequeña pausa para dar dramatismo."""
    time.sleep(1)

def separador():
    """Imprime una línea decorativa."""
    print("\n" + "=" * 45 + "\n")

def mostrar_estado(jugador):
    """Muestra la vida y el inventario del jugador."""
    print(f"❤️  Vida: {jugador['vida']}   💰 Oro: {jugador['oro']}")
    if jugador['inventario']:
        print(f"🎒 Inventario: {', '.join(jugador['inventario'])}")
    else:
        print("🎒 Inventario: (vacío)")

# --- ESCENAS DEL JUEGO ---

def inicio(jugador):
    """La pantalla de bienvenida."""
    separador()
    print("🏰  BIENVENIDO A LA MAZMORRA MISTERIOSA  🏰")
    separador()
    print("Eres un valiente aventurero que ha entrado")
    print("a una mazmorra en busca de gloria y tesoros.")
    print()
    nombre = input("¿Cómo te llamas, aventurero? > ")
    if nombre.strip() == "":
        nombre = "Aventurero"
    jugador['nombre'] = nombre
    pausa()
    print(f"\n¡Bienvenido, {jugador['nombre']}! Tu aventura comienza...")
    pausa()
    sala_entrada(jugador)

def sala_entrada(jugador):
    """Primera sala: la entrada."""
    separador()
    mostrar_estado(jugador)
    print("🚪 SALA DE ENTRADA")
    print()
    print("Estás en la entrada de la mazmorra.")
    print("Hay tres caminos frente a ti:")
    print()
    print("  1. ⬅️  Ir al pasillo OSCURO (a la izquierda)")
    print("  2. ⬆️  Avanzar al SALÓN PRINCIPAL (al frente)")
    print("  3. ➡️  Explorar la SALA DEL TESORO (a la derecha)")
    print()

    opcion = input("¿Qué camino eliges? (1, 2 o 3) > ")

    if opcion == "1":
        pasillo_oscuro(jugador)
    elif opcion == "2":
        salon_principal(jugador)
    elif opcion == "3":
        sala_tesoro(jugador)
    else:
        print("❌ Opción no válida. Intenta de nuevo.")
        pausa()
        sala_entrada(jugador)

def pasillo_oscuro(jugador):
    """El pasillo oscuro: encuentro con un monstruo."""
    separador()
    mostrar_estado(jugador)
    print("🌑 PASILLO OSCURO")
    print()
    print("Caminas por un oscuro pasillo.")
    print("De repente... ¡aparece un GOBLIN! 👺")
    print()
    print("  1. ⚔️  Atacar al goblin")
    print("  2. 🏃 Huir de regreso a la entrada")
    print()

    opcion = input("¿Qué haces? (1 o 2) > ")

    if opcion == "1":
        pausa()
        # El ataque tiene algo de azar
        dado = random.randint(1, 6)  # Número aleatorio entre 1 y 6
        print()
        if dado >= 3:
            print("💥 ¡Atacas con valentía y derrotas al goblin!")
            oro_ganado = random.randint(5, 15)
            jugador['oro'] += oro_ganado
            print(f"💰 ¡Encontraste {oro_ganado} monedas de oro!")
            pausa()
            sala_entrada(jugador)
        else:
            daño = random.randint(10, 25)
            jugador['vida'] -= daño
            print(f"💔 El goblin te ataca. ¡Pierdes {daño} puntos de vida!")
            pausa()
            if jugador['vida'] <= 0:
                fin_juego(jugador, victoria=False)
            else:
                print("Logras escapar malherido...")
                pausa()
                sala_entrada(jugador)

    elif opcion == "2":
        print("🏃 ¡Corres de regreso a la entrada!")
        pausa()
        sala_entrada(jugador)
    else:
        print("❌ Opción no válida.")
        pausa()
        pasillo_oscuro(jugador)

def salon_principal(jugador):
    """El salón principal: un comerciante."""
    separador()
    mostrar_estado(jugador)
    print("🕯️  SALÓN PRINCIPAL")
    print()
    print("Encuentras un COMERCIANTE sentado junto a una hoguera. 🔥")
    print(f"'¡Hola, {jugador['nombre']}! Tengo artículos para ti.'")
    print()
    print("  1. 🍖 Comprar ración de comida (+30 vida) — cuesta 10 oro")
    print("  2. ⚔️  Comprar espada mágica — cuesta 20 oro")
    print("  3. 🚶 Continuar sin comprar nada")
    print()

    opcion = input("¿Qué haces? (1, 2 o 3) > ")

    if opcion == "1":
        if jugador['oro'] >= 10:
            jugador['oro'] -= 10
            jugador['vida'] = min(100, jugador['vida'] + 30)  # No superar 100
            print("🍖 ¡Comes la ración y recuperas fuerzas!")
            print(f"❤️  Vida actual: {jugador['vida']}")
        else:
            print("💸 No tienes suficiente oro.")
        pausa()
        salon_principal(jugador)

    elif opcion == "2":
        if jugador['oro'] >= 20:
            if "espada mágica" not in jugador['inventario']:
                jugador['oro'] -= 20
                jugador['inventario'].append("espada mágica")
                print("⚔️  ¡Obtuviste la espada mágica! Serás más poderoso en combate.")
            else:
                print("Ya tienes una espada mágica.")
        else:
            print("💸 No tienes suficiente oro.")
        pausa()
        salon_principal(jugador)

    elif opcion == "3":
        print("🚶 Continúas tu aventura...")
        pausa()
        sala_entrada(jugador)
    else:
        print("❌ Opción no válida.")
        pausa()
        salon_principal(jugador)

def sala_tesoro(jugador):
    """La sala del tesoro: desafío final."""
    separador()
    mostrar_estado(jugador)
    print("💎 SALA DEL TESORO")
    print()
    print("¡Ante ti hay un cofre enorme lleno de oro! 🏆")
    print("Pero está custodiado por un DRAGÓN dormido. 🐉")
    print()
    print("  1. 🤫 Intentar robar el tesoro en silencio")
    print("  2. ⚔️  Despertar y enfrentarte al dragón")
    print("  3. 🚪 Retirarte a la sala de entrada")
    print()

    opcion = input("¿Qué haces? (1, 2 o 3) > ")

    if opcion == "1":
        pausa()
        
        tiene_espada = "espada mágica" in jugador['inventario']
        suerte = random.randint(1, 10)
        umbral = 4 if tiene_espada else 6  # Es más fácil con espada

        print()
        if suerte > umbral:
            print("🤫 Te mueves con sigilo... ¡Lo lograste!")
            print("💰 ¡Tomas el tesoro sin despertar al dragón!")
            jugador['oro'] += 100
            pausa()
            fin_juego(jugador, victoria=True)
        else:
            print("😱 ¡Pisas una piedra suelta y el dragón se despierta!")
            pausa()
            combate_dragon(jugador)

    elif opcion == "2":
        print("⚔️  Gritas un grito de guerra y el dragón despierta furioso...")
        pausa()
        combate_dragon(jugador)

    elif opcion == "3":
        print("🚪 Decides que la discreción es la mejor valentía.")
        pausa()
        sala_entrada(jugador)
    else:
        print("❌ Opción no válida.")
        pausa()
        sala_tesoro(jugador)

def combate_dragon(jugador):
    """Combate contra el dragón."""
    print()
    print("🐉 ¡El dragón ataca con fuego!")
    tiene_espada = "espada mágica" in jugador['inventario']

    if tiene_espada:
        print("⚔️  ¡Usas la espada mágica para defenderte!")
        daño = random.randint(10, 30)
    else:
        print("😬 Sin arma mágica, el ataque te golpea de lleno.")
        daño = random.randint(30, 60)

    jugador['vida'] -= daño
    print(f"💔 Pierdes {daño} puntos de vida.")
    pausa()

    if jugador['vida'] <= 0:
        fin_juego(jugador, victoria=False)
    else:
        # ¿Lograste vencer al dragón?
        if tiene_espada and random.random() > 0.4:
            print()
            print("✨ ¡La espada mágica brilla y derrotas al dragón!")
            jugador['oro'] += 100
            pausa()
            fin_juego(jugador, victoria=True)
        else:
            print("💨 Logras escapar de la sala con vida, pero sin el tesoro.")
            pausa()
            sala_entrada(jugador)

def fin_juego(jugador, victoria):
    """Pantalla de fin de juego."""
    separador()
    if victoria:
        print("🏆  ¡FELICITACIONES!  🏆")
        print()
        print(f"¡{jugador['nombre']} ha completado la mazmorra!")
    else:
        print("💀  FIN DEL JUEGO  💀")
        print()
        print(f"¡{jugador['nombre']} ha caído en la mazmorra!")

    print()
    print(f"  ❤️  Vida final:   {jugador['vida']}")
    print(f"  💰 Oro total:    {jugador['oro']}")
    if jugador['inventario']:
        print(f"  🎒 Inventario:   {', '.join(jugador['inventario'])}")
    separador()

    respuesta = input("¿Quieres jugar de nuevo? (s/n) > ")
    if respuesta.lower() == "s":
        main()  # Reinicia el juego
    else:
        print()
        print("¡Gracias por jugar! ¡Hasta la próxima aventura! 👋")
        print()

# --- FUNCIÓN PRINCIPAL ---
def main():
    # Creamos al jugador con sus estadísticas iniciales
    # Un "diccionario" guarda información con nombre:valor
    jugador = {
        'nombre':     '',
        'vida':       100,
        'oro':        0,
        'inventario': []   # Lista vacía al inicio
    }
    inicio(jugador)

if __name__ == "__main__":
    main()
