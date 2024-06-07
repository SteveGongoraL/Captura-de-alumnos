# Registro de Estudiantes - Aplicación PyQt5
![main](https://github.com/SteveGongoraL/Captura-de-alumnos/assets/55302658/2d506601-159e-4fc8-8667-a0b2790ff808)

Esta es una aplicación de escritorio creada con PyQt5 para registrar información de estudiantes. La aplicación permite capturar, visualizar y eliminar registros de estudiantes, y exportar la información capturada a un archivo CSV.

## Contenido
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)

## Características
- **Registro de estudiantes:** Captura de datos personales y académicos de los estudiantes.
- **Visualización de datos:** Muestra los registros en una tabla dentro de la aplicación.
- **Eliminación de registros:** Permite eliminar o modificar registros específicos.
- **Exportación a CSV:** Exporta la información capturada a un archivo CSV.

## Requisitos
- Python 3.x
- PyQt5
- pandas

## Instalación

- **Instalar dependencias:**

   ```bash
   pip install PyQt5 pandas
    ```

## Uso

### Ventana Principal

- **Captura de Datos:**
  Introducir los datos en los campos correspondientes (Nombre, Apellido Paterno, Apellido Materno, Matrícula, Edad, Domicilio, Municipio, Estado, Porcentaje de Beca, Materias Favoritas).

- **Guardar Registro:**
  Presionar el botón "Grabar" para almacenar los datos ingresados.

- **Exportar a CSV:**
  Presionar el botón "Escribir" para exportar la información capturada a un archivo CSV llamado Registro_alumnos.csv.

- **Limpiar Campos:**
  Presionar el botón "Limpiar" para vaciar todos los campos de entrada.

### Ventana de Visualización

- **Visualización de Registros:**
  La ventana muestra una tabla con los registros de estudiantes capturados.

- **Eliminar Fila:**
  Seleccionar una fila y presionar el botón "Eliminar fila" para eliminarla.

- **Limpiar Tabla:**
  Presionar el botón "Borrar Todo" para limpiar toda la tabla.

- **Regresar a la Ventana Principal:**
  Presionar el botón "Regresar" para volver a la ventana principal.
