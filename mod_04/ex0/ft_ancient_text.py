#!usr/bin/env python3

def data_recovery_system(filename: str) -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {filename}")

    try:
        f = open(filename)
        print("Connection established...\n")
        data = f.read()
        print("RECOVERED DATA:")
        print(data)
        f.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR:Storage vault not found")


if __name__ == "__main__":
    data_recovery_system("ancient_fragment.txt")
