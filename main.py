from merkle import MerkleTree

def main():
    print("Welcome to the Merkle Tree Implementation!")
    data = input("Enter a list of items (comma-separated): ").split(",")

    merkle_tree = MerkleTree(data)
    print(f"\nMerkle Root: {merkle_tree.get_root()}")

if __name__ == "__main__":
    main()