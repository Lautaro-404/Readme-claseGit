# Clase 11 - Entorno Virtual  y Actualización de pip

## Objetivo

Este trabajo consiste en crear un entorno de desarrollo en Python utilizando entorno virtual (`venv`), verificar la versión instalada, actualizar el gestor de paquetes `pip` y registrar todo en un repositorio Git.

---

## Pasos realizados

### 1. Crear carpeta del proyecto
```bash
mkdir python-final
cd python-final
```

### 2. Inicializar repositorio Git
```bash
git init
```

### 3. Crear archivo de Python
```bash
touch finales.py
```

### 4. Abrir el proyecto en Visual Studio Code
```bash
code .
```

### 5. Verificar versión de Python instalada
```bash
python -V
```

### 6. Crear entorno virtual
```bash
python -m venv venv
```

### 7. Activar entorno virtual
- En Windows (Git Bash o CMD):
```bash
source venv/Scripts/activate
```

- En Linux o Mac:
```bash
source venv/bin/activate
```

### 8. Actualizar pip
```bash
python -m pip install --upgrade pip
```

---# python-final
