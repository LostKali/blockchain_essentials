import hashlib

def build_merkle_tree(leaves):
    num_leaves = len(leaves)

    # If there is only one leaf, return it as the Merkle root
    if num_leaves == 1:
        return leaves[0]

    # If the number of leaves is odd, duplicate the last leaf
    if num_leaves % 2 == 1:
        leaves.append(leaves[-1])
        num_leaves += 1

    # Compute the hash of each pair of leaves
    pairs = [leaves[i] + leaves[i+1] for i in range(0, num_leaves, 2)]
    hashes = [hashlib.sha256(pair.encode()).hexdigest() for pair in pairs]

    # Recursively build the Merkle tree from the hashes
    return build_merkle_tree(hashes)

# Example usage
leaves = ["apple", "banana", "cherry", "date"]
merkle_root = build_merkle_tree(leaves)
print("Merkle root:", merkle_root)

# Print all nodes
def print_merkle_tree(node, depth=0):
    indent = " " * depth * 4
    print(indent + node)
    if len(node) == 64: # Check if the node is a hash value
        print_merkle_tree(node[:32], depth+1)
        print_merkle_tree(node[32:], depth+1)

print_merkle_tree(merkle_root)

