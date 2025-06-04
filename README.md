# Proyecto Final - Métodos Numéricos

Este proyecto implementa una aplicación en Python 3 para resolver problemas de métodos numéricos paso a paso, incluyendo explicaciones matemáticas generadas mediante la API de DeepSeek. Se puede ejecutar en consola con una interfaz amigable, y utiliza SQLite para guardar historial.

## Estructura del Proyecto

metodos_numericos/

├── main.py

├── .env

├── requirements.txt

├── core/

│ ├── gauss.py

│ ├── lu.py

│ ├── jacobi.py

│ ├── interpolation.py

│ ├── differentiation.py

│ ├── integration.py

│ └── ode.py

├── utils/

│ ├── io_handler.py

│ ├── exporter.py

│ └── explainer.py

├── interface/

│ └── cli.py

├── database/

│ ├── db.py

│ └── esquema.sql

├── docs/

│ └── resultados.pdf

└── README.md
---

## Requisitos

- Python 3.10 o superior
- Tener instalado pip
- Acceso a internet para usar la API de DeepSeek

## Instalación

1. Clona o descarga el repositorio:
```bash
   git clone https://github.com/josuerom/metodos_numericos.git
   cd metodos_numericos
```

2. Instale las dependencias
```bash
    pip install -r requirements.txt
```

3. (Opcional) Inicializa la base de datos SQLite:
```bash
    sqlite3 database/metodos.db < database/esquema.sql
```

## Ejecución
```bash
    python main.py
```
## Antes de ejecutar

Ejecute los siguientes comandos para que el proyecto no presente ningun error en la powershell
```powershell
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
    .\env\Scripts\activate
    pip install -r requirements.txt
    python main.py
```

## Vista por entrada y salida estándar
Aparecerá el menú principal con las siguientes opciones:

```bash
    ==== MATRIX CALC METODOS NUMÉRICOS ====
    1. Gauss
    2. LU
    3. Jacobi
    4. Interpolación
    5. Derivación
    6. Integración
    7. EDO
    7. Exportar resultados
    0. Salir
```

## Tipo de entrada por caso de prueba
El programa a medida que solicita los datos de entrada este te da un ejemplo sencillo del tipo de entrada que acepta por consola con su simbologia.

## Funcionalidades
Cálculo paso a paso con explicación matemática generada.

- Interfaz de consola simple e intuitiva.
- Historial de cálculos guardado en SQLite.
- Exportación a PDF o TXT (pendiente en utils/exporter.py).

## Exportación (Próximamente)
Los resultados y pasos se podrán exportar como:

- PDF usando fpdf
- TXT simple

## Documentación
Incluye plantilla de informe final en /docs/informe_tecnico.pdf con:

- Descripción de métodos
- Capturas del sistema
- Fundamento teórico y código comentado

## Licencia
Protegido con MIT License.
