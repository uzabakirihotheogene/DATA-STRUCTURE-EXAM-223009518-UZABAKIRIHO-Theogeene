Graph Implementation in C++

==============================
Project: Graph Structure with Directed and Cyclic Graphs
Language: C++
Author: UZABAKIRIHO Theogene
==============================

Description:
------------
This project demonstrates the implementation of a simple graph data structure in C++, supporting both directed and cyclic graph types. It includes features to add vertices, add edges, prevent duplicate edges (to avoid cycles), and print the structure of the graph.

Structure:
----------
1. Edge struct:
   - Represents a connection from one vertex to another with a weight.

2. Vertex struct:
   - Contains an identifier (ID), a dynamic list of edges, and edge count.

3. Graph (Abstract Class):
   - Defines the interface for any graph:
     - addVertex()
     - removeVertex()
     - addEdge()
     - printGraph()

4. DirectedGraph:
   - Implements a directed graph.
   - Stores vertices and their outgoing edges.
   - Supports dynamic memory management.

5. CyclicGraph:
   - Inherits from DirectedGraph.
   - Prevents the addition of duplicate edges to the same destination (a simple way to avoid cycles).

Main Function:
--------------
- Creates an array of Graph pointers.
- Adds vertices and edges to both a DirectedGraph and a CyclicGraph.
- Demonstrates edge rejection in CyclicGraph.
- Prints graph structure.
- Cleans up all dynamically allocated memory.

Compilation:
------------
Use a C++ compiler to compile the code. For example:
g++ -o graph graph.cpp

Usage:
------
Run the program after compiling. It will:
- Print the structure of a DirectedGraph.
- Print the structure of a CyclicGraph.
- Show how duplicate edges are prevented in CyclicGraph.

Notes:
------
- Memory management is handled manually using `new` and `delete`.
- Use modern C++ containers (like `std::vector`) for improved safety and scalability.
