# Sistema de Gestión de Envíos

## 📋 Descripción

Este es un sistema de gestión de envíos desarrollado en Python que permite administrar clientes, registrar envíos, realizar seguimiento de paquetes y generar reportes. El sistema está diseñado para una empresa de mensajería o transportadora que necesita gestionar sus operaciones de manera eficiente.

## 🚀 Funcionalidades Principales

### 1. **Gestión de Clientes**
- Registro de nuevos clientes con validación de datos
- Almacenamiento de información personal (nombre, apellidos, identificación, dirección, teléfonos)
- Validación de números de celular (debe comenzar con 3 y tener 10 dígitos)
- Actualización de datos de clientes existentes

### 2. **Registro de Envíos**
- Creación de nuevos envíos con datos del destinatario
- Generación automática de números de guía únicos
- Asignación de estado inicial "Recibido"
- Validación de remitente (debe estar registrado en el sistema)
- Captura automática de fecha y hora del envío

### 3. **Seguimiento de Envíos**
- Consulta de estado de paquetes por número de guía
- Visualización de información detallada del envío
- Interfaz intuitiva para búsqueda de envíos

### 4. **Actualización de Estados**
- Gestión de estados de envío:
  - Recibido
  - En tránsito
  - En ciudad de destino
  - En bodega de la transportadora
  - En reparto
  - Entregado
- Actualización manual de estados por número de guía

### 5. **Generación de Reportes**
- Informes básicos de envíos
- Estadísticas de entregas
- Porcentajes de envíos entregados

## 📁 Estructura del Proyecto

```
Proyecto Python/
├── main.py              # Archivo principal con menú de navegación
├── clients.py           # Gestión de clientes (registro y actualización)
├── envios.py            # Registro de envíos y generación de guías
├── f_seguimiento.py     # Seguimiento de envíos por número de guía
├── state.py             # Actualización de estados de envíos
├── actualize.py         # Actualización de datos de clientes
├── reports.py           # Generación de reportes e informes
├── clients.json         # Base de datos de clientes
├── shipments.json       # Base de datos de envíos
└── README.md           # Documentación del proyecto
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**: Lenguaje principal del proyecto
- **JSON**: Almacenamiento de datos en archivos
- **datetime**: Manejo de fechas y horas
- **random**: Generación de números de guía aleatorios

## 📦 Instalación y Uso

### Requisitos Previos
- Python 3.x instalado en el sistema
- No se requieren dependencias adicionales (solo librerías estándar de Python)

### Ejecución del Programa

1. **Navegar al directorio del proyecto:**
   ```bash
   cd "Proyecto Python"
   ```

2. **Ejecutar el programa principal:**
   ```bash
   python main.py
   ```

3. **Usar el menú principal:**
   - Seleccionar la opción deseada ingresando el número correspondiente
   - Seguir las instrucciones en pantalla para cada operación

## 🎯 Menú Principal

El sistema presenta un menú principal con las siguientes opciones:

1. **Registrar cliente** - Crear nuevo cliente en el sistema
2. **Menú de empleado** - Registrar nuevos envíos
3. **Seguimiento de envío** - Consultar estado de paquetes
4. **Actualizar estado del envío** - Cambiar estado de envíos
5. **Actualizar datos del cliente** - Modificar información de clientes
6. **Generar informe** - Crear reportes de envíos
7. **Salir** - Terminar el programa

## 📊 Estructura de Datos

### Cliente (clients.json)
```json
{
  "Nombre": "string",
  "Apellidos": "string", 
  "Identificacion": "string",
  "Tipo": "CC|TI|CE",
  "Direccion": "string",
  "Fijo": "number",
  "Celular": "string",
  "Barrio": "string"
}
```

### Envío (shipments.json)
```json
{
  "Fecha": "YYYY-MM-DD",
  "Hora": "HH:MM:SS",
  "Destinatario": {
    "Nombre": "string",
    "Direccion": "string", 
    "Telefono": "string",
    "Ciudad": "string",
    "Barrio": "string"
  },
  "Identificacion": "string",
  "Guia": "string",
  "Estado": "string"
}
```

## 🔧 Características Técnicas

### Validaciones Implementadas
- **Números de celular**: Deben comenzar con 3 y tener exactamente 10 dígitos
- **Tipos de identificación**: Solo CC, TI o CE permitidos
- **Remitentes**: Deben estar registrados en el sistema para crear envíos
- **Números de guía**: Generación automática de 6 dígitos únicos

### Manejo de Errores
- Validación de tipos de datos en entradas
- Manejo de archivos JSON corruptos o inexistentes
- Mensajes de error informativos para el usuario
- Búsqueda de clientes y envíos con validación

## 📈 Funcionalidades Futuras

- [ ] Interfaz gráfica (GUI)
- [ ] Base de datos SQL en lugar de archivos JSON
- [ ] Sistema de usuarios y autenticación
- [ ] Reportes más detallados y exportables
- [ ] Integración con APIs de transportadoras
- [ ] Notificaciones automáticas por email/SMS
- [ ] Dashboard web para administración

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

**Desarrollado con ❤️ en Python** 