def recover_ancient_text(filename: str) -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {filename}")

    try:
        vault = open(filename, 'r')
        print("Connection established...\n")
        print("RECOVERED DATA:")
        content = vault.read()
        print(content)
        vault.close()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    recover_ancient_text("ancient_fragment.txt")
