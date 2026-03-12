def create_archive(filename: str) -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print(f"\nInitializing new storage unit: {filename}")

    vault = open(filename, 'w')
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")

    entries = [
        "New quantum algorithm discovered",
        "Efficiency increased by 347%",
        "Archived by Data Archivist trainee",
    ]

    for i, entry in enumerate(entries, start=1):
        line = f"[ENTRY {i:03d}] {entry}"
        vault.write(line + "\n")
        print(line)

    vault.close()
    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    create_archive("new_discovery.txt")
