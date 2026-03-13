#!/usr/bin/env python3


class Alert:
    def __init__(self, filename: str, response: str, status: str) -> None:
        self.alert = f"CRISIS ALERT: Attempting access to '{filename}'...\n"
        self.response = f"RESPONSE: {response}\n"
        self.status = f"STATUS: crisis handled, {status}"
        self.ret = self.alert + self.response + self.status

    def __str__(self) -> str:
        return self.ret


def crisis_handler(filename: str) -> None:
    try:
        with open(filename, 'r') as vault:
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
            data = vault.read().strip()
            print(f"SUCCESS: Archive recovered - ``{data}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(Alert(
            filename,
            response="Archive not found in storage matrix",
            status="system stable"))
    except PermissionError:
        print(Alert(
            filename,
            response="Security protocols deny access",
            status="security maintained"))
    except Exception as e:
        print(Alert(
            filename,
            response=f"Unexpected anomaly encountered - {e}",
            status="damage contained"
        ))


def crisis_response_system() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    crisis_handler("lost_archive.txt")
    print()
    crisis_handler("classified_vault.txt")
    print()
    crisis_handler("standard_archive.txt")
    print()
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    crisis_response_system()
