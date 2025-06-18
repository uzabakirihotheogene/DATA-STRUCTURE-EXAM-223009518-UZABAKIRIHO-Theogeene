#include <iostream>

// ===== Edge and Vertex =====
struct Edge {
    int to;
    float weight;
};

struct Vertex {
    int id;
    Edge* edges;
    int edgeCount;

    Vertex() : id(-1), edges(nullptr), edgeCount(0) {}
};

// ===== Abstract Graph Base Class =====
class Graph {
public:
    virtual void addVertex(int id) = 0;
    virtual void removeVertex(int id) = 0;
    virtual void addEdge(int from, int to, float weight) = 0;
    virtual void printGraph() const = 0;
    virtual ~Graph() {}
};

// ===== Directed Graph =====
class DirectedGraph : public Graph {
protected:
    Vertex* vertices;
    int vertexCount;

public:
    DirectedGraph() : vertices(nullptr), vertexCount(0) {}

    void addVertex(int id) override {
        Vertex* newVertices = new Vertex[vertexCount + 1];
        for (int i = 0; i < vertexCount; ++i)
            newVertices[i] = vertices[i];

        newVertices[vertexCount].id = id;
        newVertices[vertexCount].edges = nullptr;
        newVertices[vertexCount].edgeCount = 0;

        delete[] vertices;
        vertices = newVertices;
        vertexCount++;
    }

    void removeVertex(int id) override {
        int index = -1;
        for (int i = 0; i < vertexCount; ++i) {
            if (vertices[i].id == id) {
                index = i;
                break;
            }
        }
        if (index == -1) return;

        delete[] vertices[index].edges;

        Vertex* newVertices = new Vertex[vertexCount - 1];
        for (int i = 0, j = 0; i < vertexCount; ++i) {
            if (i != index) {
                newVertices[j++] = vertices[i];
            }
        }

        delete[] vertices;
        vertices = newVertices;
        vertexCount--;
    }

    void addEdge(int from, int to, float weight) override {
        for (int i = 0; i < vertexCount; ++i) {
            if (vertices[i].id == from) {
                Vertex& v = vertices[i];
                Edge* newEdges = new Edge[v.edgeCount + 1];

                for (int j = 0; j < v.edgeCount; ++j)
                    *(newEdges + j) = *(v.edges + j); // Pointer arithmetic

                *(newEdges + v.edgeCount) = { to, weight };

                delete[] v.edges;
                v.edges = newEdges;
                v.edgeCount++;
                return;
            }
        }
    }

    void printGraph() const override {
        for (int i = 0; i < vertexCount; ++i) {
            const Vertex& v = vertices[i];
            std::cout << "Vertex " << v.id << " -> ";
            for (int j = 0; j < v.edgeCount; ++j) {
                const Edge& e = *(v.edges + j); // pointer arithmetic
                std::cout << "(" << e.to << ", w=" << e.weight << ") ";
            }
            std::cout << "\n";
        }
    }

    virtual ~DirectedGraph() {
        for (int i = 0; i < vertexCount; ++i)
            delete[] vertices[i].edges;
        delete[] vertices;
    }
};

// ===== CyclicGraph - prevents duplicate edges (simple check) =====
class CyclicGraph : public DirectedGraph {
public:
    void addEdge(int from, int to, float weight) override {
        for (int i = 0; i < vertexCount; ++i) {
            if (vertices[i].id == from) {
                Vertex& v = vertices[i];
                for (int j = 0; j < v.edgeCount; ++j) {
                    if ((v.edges + j)->to == to) {
                        std::cout << "Edge already exists, preventing cycle.\n";
                        return;
                    }
                }
                break;
            }
        }
        DirectedGraph::addEdge(from, to, weight);
    }
};

int main() {
    // ===== Graph Pointer Array =====
    Graph** graphs = new Graph*[2];

    graphs[0] = new DirectedGraph();
    graphs[1] = new CyclicGraph();

    // ===== Using Directed Graph =====
    graphs[0]->addVertex(1);
    graphs[0]->addVertex(2);
    graphs[0]->addEdge(1, 2, 5.0f);
    graphs[0]->addEdge(2, 1, 3.0f);
    std::cout << "Directed Graph:\n";
    graphs[0]->printGraph();

    // ===== Using Cyclic Graph =====
    graphs[1]->addVertex(10);
    graphs[1]->addVertex(20);
    graphs[1]->addEdge(10, 20, 2.0f);
    graphs[1]->addEdge(10, 20, 4.0f); // should be rejected
    std::cout << "\nCyclic Graph:\n";
    graphs[1]->printGraph();

    // ===== Cleanup =====
    for (int i = 0; i < 2; ++i)
        delete graphs[i];
    delete[] graphs;

    return 0;
}
