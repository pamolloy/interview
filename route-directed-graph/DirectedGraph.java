class Node {
    public String value;
    public Node [] nodes;
}

class DirectedGraph {
    public Node root;

    public static void main(String[] args) {
        // Create an example graph
        // Run graph.routeBetweenNodes(first, second)
    }

    public boolean routeBetweenNodes(Node first, Node second) {
        // Check if the two nodes are the same
        // Traverse the graph
        // Find one of the nodes
        // Follow the children until the second node is found
        // Check for cyclical branches
    }

    /*
     * A solution provided by Cracking the Coding Interview
     * It never checks whether the state is Visited or Visiting
     * Why would you add null to the queue?
     * It needs to traverse once just to set the state
     * This assumes that the first argument comes before the second, which isn't implied by the problem
     */
    public boolean search(Graph graph, Node start, Node end) {
        if (start == end) return true;
        start.state = State.Visting;

        // Assuming the Node class has a state attribute this should set it to unvisited
        for (Node node : graph.getNodes()) {
            node.state = State.Unvisited;
        }

        LinkedList<Node> queue = new LinkedList<Node>();
        queue.add(start);   // Add the start Node to the queue
        Node node;          // Create a Node
        // Iterate until the queue is empty
        while (!queue.isEmpty()) {
            node = queue.removeFirst(); // Dequeue a Node
            if (node != null) {
                // Iterate through the adjacent nodes
                for (Node next : node.getAdjacent()) {
                    if (next.state == State.Unvisited) {
                        if (next == end) {
                            return true;
                        } else {
                            next.state = State.Visiting;
                            queue.add(next);
                        }
                    }
                }
                node.state = State.Visited;
            }
        }
        return false;
    }
}
