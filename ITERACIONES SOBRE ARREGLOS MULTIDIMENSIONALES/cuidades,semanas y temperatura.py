print("Semana #12")
print("Iteración de arreglos multidimensionales con bucles anidados")

# Primero debemos crear una matriz 3D
#EN CADA MATRIZ VA UNA CIUDAD Y DENTRO DE ESTA LAS SEMANAS Y LAS TEMPERATURAS.

temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp":65},
            {"day": "Martes", "temp": 45},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 77},
            {"day": "Sábado", "temp": 48},
            {"day": "Domingo", "temp": 92}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 76},
            {"day": "Martes", "temp": 79},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 81},
            {"day": "Viernes", "temp": 90},
            {"day": "Sábado", "temp": 45},
            {"day": "Domingo", "temp": 38}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 77},
            {"day": "Martes", "temp": 68},
            {"day": "Miércoles", "temp": 44},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 66},
            {"day": "Sábado", "temp": 65},
            {"day": "Domingo", "temp": 10}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 45},
            {"day": "Viernes", "temp": 84},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 38}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 62},
            {"day": "Martes", "temp": 64},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 79}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 63},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 61},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 80}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 64},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 80}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 92},
            {"day": "Miércoles", "temp": 94},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 82}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 89},
            {"day": "Martes", "temp": 70},
            {"day": "Miércoles", "temp": 93},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 90},
            {"day": "Sábado", "temp": 74},
            {"day": "Domingo", "temp": 82}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 91},
            {"day": "Martes", "temp": 64},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 78},
            {"day": "Viernes", "temp": 40},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 50},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 79}
        ]
    ]
]

# Nombres de ciudades para facilitar la impresión
nombres_ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]

# Calcular el promedio de temperaturas para cada ciudad y semana
for indice_ciudad, ciudad in enumerate(temperaturas):
    print(f"\nPromedio de temperaturas para {nombres_ciudades[indice_ciudad]}:")

    for indice_semana, semana in enumerate(ciudad):
        suma_temperaturas = 0
        cantidad_dias = len(semana)

        # Sumamos las temperaturas de cada día en la semana
        for dia in semana:
            suma_temperaturas += dia["temp"]

        # Calcular los promedios por cada ciudad
        promedio = suma_temperaturas / cantidad_dias
        print(f"  Semana {indice_semana + 1}: {promedio:.2f}°F")

