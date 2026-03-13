#!/usr/bin/env python3

def preservation_system(filename: str) -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    print(f"Initializing new storage unit: {filename}")

    try:
        exist = open(filename, 'r')
        exist.close()
        raise FileExistsError("Error: Storage vault already exists.\n"
                              "       Overwriting archives is forbidden.")
    except FileExistsError as e:
        print(f"{e}")
        return None
    except FileNotFoundError:
        pass

    vault = open(filename, 'w')
    print("Storage unit created successfully...\n")
    entries = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist heychong",
    ]
    for entry in entries:
        vault.write(entry + "\n")
        print(entry)
    vault.close()
    print("\nData inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for "
          "long-term preservation.")


if __name__ == "__main__":
    preservation_system("new_discovery.txt")
