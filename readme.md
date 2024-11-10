# Proyecto de E-commerce con Django

Este es un proyecto de e-commerce básico desarrollado con Django que permite gestionar productos, categorías, clientes y órdenes. El proyecto también incluye comandos personalizados de Django para facilitar la administración de inventario, la generación de reportes y la limpieza de datos.

## Características

Modelos de e-commerce: Productos, Categorías, Clientes, Órdenes, y Logs de Inventario.
Comandos personalizados de Django:
Reporte de ventas: Generación y exportación de reportes de ventas.
Limpieza de órdenes: Eliminación de órdenes canceladas o inactivas.
Importación de productos: Carga de productos desde archivos CSV.
Importación de inventario: Carga de inventario inicial y actualización de stock.

## Instalación

### Prerrequisitos

Python 3.8+
Django 4.x
Base de datos PostgreSQL, MySQL o SQLite para desarrollo.

### Configuración del Entorno

Clona el repositorio:

```bash
git clone <URL-del-repositorio>
cd <nombre-del-proyecto>
```

Crea y activa un entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate # En Windows: venv\Scripts\activate
```

Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

Configura la base de datos en el archivo settings.py y realiza las migraciones:

```bash
python manage.py migrate
```

Crea un superusuario para acceder al panel de administración:

```bash
python manage.py createsuperuser
```

Ejecuta el servidor de desarrollo:

```bash
python manage.py runserver
```

## Uso de Comandos Personalizados

1. Reporte de Ventas
   Genera un reporte de ventas de los últimos días y permite exportarlo a un archivo CSV.

```bash
python manage.py sales_report --days 30 --export
```

- --days: Número de días hacia atrás para el reporte (por defecto, 30).
- --export: Exporta el reporte a un archivo CSV.

2. Limpieza de Órdenes
   Elimina órdenes antiguas con un estado específico.

```bash
python manage.py cleanup_orders --days 90 --status CANCELLED
```

- --days: Número de días hacia atrás para considerar órdenes antiguas (por defecto, 90).
- --status: Estado de las órdenes a eliminar, como CANCELLED.

3. Limpieza de Productos Inactivos
   Elimina productos sin stock que no se han actualizado en un tiempo determinado.

```bash
python manage.py cleanup_products --inactive-days 180
```

- --inactive-days: Número de días de inactividad para considerar productos sin stock (por defecto, 180).

4. Importación de Productos desde CSV
   Importa productos desde un archivo CSV, con opción de actualización.

```bash
python manage.py import_products productos.csv --update
```

- file_path: Ruta al archivo CSV.
- --update: Opción para actualizar productos existentes.

5. Importación de Inventario Inicial
   Importa y actualiza el inventario inicial desde un archivo CSV.

```bash
python manage.py import_inventory inventario.csv
```

- file_path: Ruta al archivo CSV con los datos de inventario.

## Estructura de Archivos CSV

`productos.csv`
Archivo de ejemplo para importar productos.

| name      | description              | price | stock | category    |
| --------- | ------------------------ | ----- | ----- | ----------- |
| Producto1 | Descripción del producto | 10.99 | 100   | Electrónica |

`inventario.csv`
Archivo de ejemplo para importar inventario inicial.

| product_name | initial_stock |
| ------------ | ------------- |
| Producto1    | 50            |

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para mejorar el proyecto.

## Licencia

Este proyecto está bajo la licencia MIT.
