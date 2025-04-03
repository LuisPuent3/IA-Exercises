#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implementación del algoritmo A* con varios mecanismos de control.
Este código ilustra:
- Control de exploración (límites de búsqueda)
- Prevención de ciclos (mediante conjunto de nodos visitados)
- Control de profundidad (limitación de longitud de caminos)
- Monitoreo de rendimiento (conteo de nodos explorados)
"""

import heapq
import time
from collections import defaultdict

class Node:
    """Representa un nodo en el grafo con su información de estado y camino."""
    
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1
    
    def __lt__(self, other):
        return self.path_cost < other.path_cost
    
    def __eq__(self, other):
        return self.state == other.state
    
    def __hash__(self):
        return hash(self.state)

class AStar:
    """Implementación del algoritmo A* con mecanismos de control."""
    
    def __init__(self, graph, heuristic, max_nodes=1000, max_depth=100):
        """
        Inicializa el algoritmo A* con el grafo y la heurística.
        
        Args:
            graph: Diccionario donde las claves son nodos y los valores son
                  diccionarios con los nodos vecinos y los costos.
            heuristic: Función que estima el costo desde un nodo al objetivo.
            max_nodes: Límite máximo de nodos a explorar (control de exploración).
            max_depth: Profundidad máxima permitida (control de profundidad).
        """
        self.graph = graph
        self.heuristic = heuristic
        self.max_nodes = max_nodes
        self.max_depth = max_depth
        self.nodes_explored = 0
    
    def get_neighbors(self, node):
        """Obtiene los vecinos de un nodo."""
        neighbors = []
        for neighbor, cost in self.graph[node.state].items():
            new_node = Node(
                state=neighbor,
                parent=node,
                action=f"Move to {neighbor}",
                path_cost=node.path_cost + cost
            )
            neighbors.append(new_node)
        return neighbors
    
    def search(self, start, goal):
        """
        Ejecuta el algoritmo A* desde start hasta goal.
        
        Args:
            start: Nodo inicial.
            goal: Nodo objetivo.
        
        Returns:
            La solución como una lista de estados o None si no hay solución.
        """
        start_time = time.time()
        
        # Nodo inicial
        start_node = Node(state=start, path_cost=0)
        
        # Cola de prioridad para la frontera
        frontier = []
        heapq.heappush(frontier, (0, start_node))
        
        # Diccionario para acceder rápidamente a los nodos en la frontera
        frontier_hash = {start: 0}
        
        # Conjunto de estados visitados (prevención de ciclos)
        explored = set()
        
        while frontier:
            # MECANISMO DE CONTROL: Límite de nodos explorados
            if self.nodes_explored >= self.max_nodes:
                print(f"Búsqueda cancelada: se alcanzó el límite de {self.max_nodes} nodos")
                return None
            
            # Extraer el nodo con menor f(n) = g(n) + h(n)
            _, current_node = heapq.heappop(frontier)
            
            # Eliminar del diccionario de la frontera
            if current_node.state in frontier_hash:
                del frontier_hash[current_node.state]
            
            # Incrementar contador de nodos explorados (monitoreo de rendimiento)
            self.nodes_explored += 1
            
            # Mostrar progreso cada cierto número de nodos
            if self.nodes_explored % 100 == 0:
                print(f"Nodos explorados: {self.nodes_explored}")
            
            # Verificar si hemos llegado al objetivo
            if current_node.state == goal:
                end_time = time.time()
                # Reconstruir la solución
                path = []
                while current_node:
                    path.append(current_node.state)
                    current_node = current_node.parent
                path.reverse()
                
                print(f"Solución encontrada en {end_time - start_time:.2f} segundos")
                print(f"Nodos explorados: {self.nodes_explored}")
                print(f"Longitud del camino: {len(path)}")
                return path
            
            # Añadir el nodo actual al conjunto de explorados
            explored.add(current_node.state)
            
            # MECANISMO DE CONTROL: Límite de profundidad
            if current_node.depth >= self.max_depth:
                continue
            
            # Expandir nodos vecinos
            for neighbor in self.get_neighbors(current_node):
                # MECANISMO DE CONTROL: Prevención de ciclos
                if neighbor.state in explored:
                    continue
                
                # Calcular f(n) = g(n) + h(n)
                f_score = neighbor.path_cost + self.heuristic(neighbor.state, goal)
                
                # Si el vecino ya está en la frontera con mayor costo, actualizarlo
                if neighbor.state in frontier_hash and f_score >= frontier_hash[neighbor.state]:
                    continue
                
                # Añadir a la frontera
                heapq.heappush(frontier, (f_score, neighbor))
                frontier_hash[neighbor.state] = f_score
        
        # No se encontró solución
        print("No se encontró solución")
        return None

def ejemplo_grafo():
    """Crea un grafo de ejemplo."""
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1, 'E': 3},
        'E': {'D': 3, 'F': 2},
        'F': {'E': 2}
    }
    return graph

def heuristica_ejemplo(nodo, objetivo):
    """
    Heurística simple basada en un diccionario predefinido.
    En un caso real, podría ser distancia euclidiana, Manhattan, etc.
    """
    heuristics = {
        'A': {'F': 5},
        'B': {'F': 4},
        'C': {'F': 3},
        'D': {'F': 2},
        'E': {'F': 1},
        'F': {'F': 0}
    }
    return heuristics[nodo][objetivo]

def main():
    """Función principal que ejecuta el ejemplo."""
    # Crear el grafo de ejemplo
    graph = ejemplo_grafo()
    
    # Definir inicio y objetivo
    start = 'A'
    goal = 'F'
    
    # Crear instancia de A*
    astar = AStar(
        graph=graph,
        heuristic=heuristica_ejemplo,
        max_nodes=1000,
        max_depth=10
    )
    
    # Ejecutar el algoritmo
    print(f"Buscando camino de {start} a {goal}...")
    path = astar.search(start, goal)
    
    # Mostrar el resultado
    if path:
        print(f"Camino encontrado: {' -> '.join(path)}")
    else:
        print("No se pudo encontrar un camino.")

if __name__ == "__main__":
    main() 