# CÓDIGOS DE BASE DE CONOCIMIENTO Y MECANISMOS DE CONTROL EN IA

## Descripción
Este repositorio contiene implementaciones prácticas de dos componentes fundamentales en sistemas de Inteligencia Artificial:
1. Base de conocimiento en Prolog
2. Algoritmo A* con mecanismos de control en Python

Los códigos sirven como ejemplos educativos para entender cómo funcionan estos sistemas en la práctica.

## Contenido

### `base_conocimiento.pl`
Sistema experto médico simple implementado en Prolog que demuestra:
- Representación de hechos (síntomas de pacientes)
- Definición de reglas de inferencia (diagnóstico)
- Encadenamiento lógico (tratamientos basados en diagnósticos)
- Consultas a la base de conocimiento

### `mecanismos_control.py`
Implementación del algoritmo A* en Python con diversos mecanismos de control que ilustra:
- Control de exploración (límites de búsqueda)
- Prevención de ciclos (mediante conjunto de nodos visitados)
- Control de profundidad (limitación de longitud de caminos)
- Monitoreo de rendimiento (conteo de nodos explorados)

## Requisitos

### Para base_conocimiento.pl:
- SWI-Prolog (https://www.swi-prolog.org/download/stable)
- Alternativamente, puede utilizarse un intérprete en línea como SWISH (https://swish.swi-prolog.org/)

### Para mecanismos_control.py:
- Python 3.6 o superior
- No requiere bibliotecas adicionales (solo utiliza módulos estándar)

## Uso

### Base de conocimiento (Prolog)

```bash
# Ejecutar con SWI-Prolog
swipl -s base_conocimiento.pl
```

Consultas de ejemplo:
```prolog
?- enfermedad(juan, X).
?- tratamiento(juan, X).
?- enfermedad(pedro, X).
```

### Algoritmo con mecanismos de control (Python)

```bash
# Ejecutar el algoritmo
python mecanismos_control.py
```

El script ejecuta automáticamente un ejemplo de búsqueda de ruta en un grafo predefinido.

## Modificaciones posibles

### Para base_conocimiento.pl:
- Añadir nuevos síntomas y pacientes
- Crear reglas adicionales para otras enfermedades
- Implementar tratamientos más específicos

### Para mecanismos_control.py:
- Modificar el grafo para probar diferentes topologías
- Ajustar los parámetros de control (límites, profundidad)
- Cambiar la heurística para observar efectos en el rendimiento

## Notas adicionales
Estos códigos fueron desarrollados como material educativo para una presentación sobre IA. Aunque son funcionales, están optimizados para claridad pedagógica más que para rendimiento en entornos de producción.

## Licencia
MIT