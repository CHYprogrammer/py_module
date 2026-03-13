#!usr/bin/env python3

def data_recovery_system(filename: str) -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {filename}")

    try:
        vault = open(filename)
        print("Connection established...\n")
        data = vault.read()
        print("RECOVERED DATA:")
        print(data)
        vault.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR:Storage vault not found")
    except PermissionError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    data_recovery_system("ancient_fragment.txt")
