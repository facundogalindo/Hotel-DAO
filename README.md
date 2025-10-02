# Sistema de Gestión de Reservas de Hotel

Un hotel necesita un sistema para gestionar las reservas de sus habitaciones. Hay tres tipos de habitaciones: estándar, suite y suite premium.
• Habitación estándar: tiene un costo base por noche.
• Suite: tiene un costo base + un 10% adicional si incluye vista al mar.
• Suite premium: tiene un costo base + un 20% adicional si incluye jacuzzi privado.

## Archivo habitaciones.csv:

    • Tipo de habitación (1 = estándar, 2 = suite, 3 = suite premium)
    • Número de habitación
    • Nombre del huésped
    • Costo base por noche
    • Noches reservadas
    • Columna extra (habitación estándar siempre en False, vista al mar = True/False, jacuzzi = True/False).

## Funcionalidades:

    1. Cargar reservas desde el archivo.
    2. Calcular y mostrar la suma de costo de todas las reservas.
    3. Obtener la reserva más cara.
    4. Calcular el ingreso total del hotel.
    5. Contar cuántas suites tienen vista al mar.
    6. Contar cuántas suites premium tienen jacuzzi.
    7. Calcular en un diccionario la cantidad de reservas de cada tipo de habitación.
