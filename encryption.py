def encrypt(text, shift):
    """Encrypt text using Caesar cipher"""
    result = ""
    
    for char in text:
        if char.isalpha():
            # Get the ASCII value
            ascii_offset = 65 if char.isupper() else 97
            # Shift the character and wrap around using modulo
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += encrypted_char
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result

def decrypt(text, shift):
    """Decrypt text using Caesar cipher"""
    # Decryption is just encryption with negative shift
    return encrypt(text, -shift)

# Main program
if __name__ == "__main__":
    print("=== Caesar Cipher Encryption ===\n")
    
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (1-25): "))
    
    if choice == 'E':
        encrypted = encrypt(message, shift)
        print(f"\nEncrypted message: {encrypted}")
    elif choice == 'D':
        decrypted = decrypt(message, shift)
        print(f"\nDecrypted message: {decrypted}")
    else:
        print("Invalid choice!")
        
    # Example usage
    print("\n--- Example ---")
    original = "Hello World!"
    shift_value = 3
    enc = encrypt(original, shift_value)
    dec = decrypt(enc, shift_value)
    print(f"Original: {original}")
    print(f"Encrypted (shift {shift_value}): {enc}")
    print(f"Decrypted: {dec}")

import heapq
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v, weight):
        """Add an edge to the graph"""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # For undirected graph
    
    def dijkstra(self, start, end):
        """Find the shortest path from start to end using Dijkstra's algorithm"""
        pq = [(0, start, [start])]  # (distance, current_node, path)
        visited = set()
        distances = {start: 0}
        
        while pq:
            curr_dist, curr_node, path = heapq.heappop(pq)
            
            if curr_node in visited:
                continue
            visited.add(curr_node)
            if curr_node == end:
                return curr_dist, path
            for neighbor, weight in self.graph.get(curr_node, []):
                if neighbor not in visited:
                    new_dist = curr_dist + weight
                    if neighbor not in distances or new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor, path + [neighbor]))
        return float('inf'), []
    def print_graph(self):
        """Print the graph structure"""
        print("\nGraph Structure:")
        for node in sorted(self.graph.keys()):
            print(f"{node}: {self.graph[node]}")
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'D', 7)
    g.add_edge('B', 'C', 3)
    g.add_edge('C', 'D', 1)
    g.add_edge('C', 'E', 2)
    g.add_edge('D', 'E', 6)
    g.print_graph()
    # Find shortest path from A to E
    distance, path = g.dijkstra('A', 'E')
    print(f"\nShortest path from A to E: Distance = {distance}, Path =
    {path}")
    g.add_edge('D', 'E', 2)
    g.print_graph()
    g.add_edge('E', 'F', 3)
    g.print_graph()
        """Display the graph structure"""
        print("\nGraph Structure:")
        for node in sorted(self.graph.keys()):
            print(f"{node}: {self.graph[node]}")f"{node}: {self.graph[node]}")
            