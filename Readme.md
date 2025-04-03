# 🧠 CÓDIGOS DE BASE DE CONOCIMIENTO Y MECANISMOS DE CONTROL EN IA

<div align="center">
  <img src="https://img.shields.io/badge/Prolog-Bases%20de%20Conocimiento-blue?style=for-the-badge&logo=prolog" alt="Prolog Base de Conocimiento">
  <img src="https://img.shields.io/badge/Python-Algoritmo%20A*-yellow?style=for-the-badge&logo=python" alt="Python Algoritmo A*">
</div>

## 📝 Descripción
Este repositorio contiene implementaciones prácticas de dos componentes fundamentales en sistemas de Inteligencia Artificial:

| Componente | Descripción | Lenguaje |
|------------|-------------|----------|
| 📚 Base de conocimiento | Sistema experto médico simple | Prolog |
| 🔍 Algoritmo A* | Búsqueda con mecanismos de control | Python |

Los códigos sirven como ejemplos educativos para entender cómo funcionan estos sistemas en la práctica.

## 📦 Contenido

### `base_conocimiento.pl` 🏥
Sistema experto médico simple implementado en Prolog que demuestra:
- 📊 **Representación de hechos** - Síntomas de pacientes
- 📏 **Reglas de inferencia** - Diagnóstico lógico
- ⛓️ **Encadenamiento lógico** - Tratamientos basados en diagnósticos
- 🔎 **Consultas** - Interrogación a la base de conocimiento

```prolog
% Ejemplo de consulta
?- enfermedad(juan, X).
X = gripe.
```

### `mecanismos_control.py` 🧩
Implementación del algoritmo A* en Python con diversos mecanismos de control que ilustra:

<div align="center">
  <table>
    <tr>
      <td align="center">🛑</td>
      <td><b>Control de exploración</b></td>
      <td>Límites de búsqueda</td>
    </tr>
    <tr>
      <td align="center">🔄</td>
      <td><b>Prevención de ciclos</b></td>
      <td>Mediante conjunto de nodos visitados</td>
    </tr>
    <tr>
      <td align="center">📏</td>
      <td><b>Control de profundidad</b></td>
      <td>Limitación de longitud de caminos</td>
    </tr>
    <tr>
      <td align="center">📊</td>
      <td><b>Monitoreo de rendimiento</b></td>
      <td>Conteo de nodos explorados</td>
    </tr>
  </table>
</div>

```python
# Ejemplo de resultado
Camino encontrado: A -> B -> C -> D -> E -> F
```

## ⚙️ Requisitos

### Para base_conocimiento.pl:
- 💻 [SWI-Prolog](https://www.swi-prolog.org/download/stable)
- 🌐 Alternativamente, puede utilizarse un intérprete en línea como [SWISH](https://swish.swi-prolog.org/)

### Para mecanismos_control.py:
- 🐍 Python 3.6 o superior
- 📦 No requiere bibliotecas adicionales (solo utiliza módulos estándar)

## 🚀 Uso

### Base de conocimiento (Prolog)

```bash
# Ejecutar con SWI-Prolog
swipl -s base_conocimiento.pl
```

<details>
  <summary><b>📋 Consultas de ejemplo</b> (clic para expandir)</summary>
  
  ```prolog
  % Consultar una enfermedad
  ?- enfermedad(juan, X).
  
  % Consultar un tratamiento
  ?- tratamiento(juan, X).
  
  % Verificar múltiples enfermedades
  ?- enfermedad(pedro, X).
  ```
</details>

### Algoritmo con mecanismos de control (Python)

```bash
# Ejecutar el algoritmo
python mecanismos_control.py
```

El script ejecuta automáticamente un ejemplo de búsqueda de ruta en un grafo predefinido.

## 🔧 Modificaciones posibles

### Para base_conocimiento.pl:
- ➕ Añadir nuevos síntomas y pacientes
- 📝 Crear reglas adicionales para otras enfermedades
- 💊 Implementar tratamientos más específicos

### Para mecanismos_control.py:
- 🔄 Modificar el grafo para probar diferentes topologías
- ⚙️ Ajustar los parámetros de control (límites, profundidad)
- 📈 Cambiar la heurística para observar efectos en el rendimiento

## 📝 Notas adicionales
Estos códigos fueron desarrollados como material educativo para una presentación sobre IA. Aunque son funcionales, están optimizados para claridad pedagógica más que para rendimiento en entornos de producción.

<div align="center">
  <img src="https://img.shields.io/badge/Propósito-Educativo-green?style=for-the-badge" alt="Propósito Educativo">
</div>

## 📄 Licencia
MIT