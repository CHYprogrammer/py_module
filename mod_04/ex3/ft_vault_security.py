#!/usr/bin/env python3

def vault_security_system(read_vault: str, write_vault: str) -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    print("\nSECURE EXTRACTION:")
    try:
        # with open(read_vault, 'w') as vault:
        #    vault.write("[CLASSIFIED] Quantum encryption keys recovered\n")
        #    vault.write("[CLASSIFIED] Archive integrity: 100%\n")

        with open(read_vault, 'r') as vault:
            data = vault.read()
            print(data)
    except (FileNotFoundError, PermissionError,
            IsADirectoryError, OSError) as e:
        print(f"ERROR: {e}")
    except TypeError:
        print("ERROR: filename is not string.")

    print("\nSECURE PRESERVATION:")
    entry = "[CLASSIFIED] New security protocols archived"
    try:
        with open(write_vault, 'w') as vault:
            vault.write(entry)
        print(entry)
        print("Vault automatically sealed upon completion\n")
    except (FileNotFoundError, PermissionError,
            IsADirectoryError, OSError) as e:
        print(f"ERROR: {e}")
    except TypeError:
        print("ERROR: expected str, bytes or os.PathLike object")

    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    vault_security_system("classified_data.txt", "security_log.txt")
