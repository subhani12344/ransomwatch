import sys

from ransomwatch.monitor.file_monitor import start_monitor


def main():

    if len(sys.argv) < 3:
        print("Usage:")
        print("python -m ransomwatch.main monitor <directory>")
        return

    command = sys.argv[1]
    path = sys.argv[2]

    if command == "monitor":
        start_monitor(path)

    else:
        print(f"[ERROR] Unknown command: {command}")


if __name__ == "__main__":
    main()