import time
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class RansomWatchHandler(FileSystemEventHandler):

    def on_created(self, event):
        if not event.is_directory:
            print(f"[CREATE] {event.src_path}")

    def on_modified(self, event):
        if not event.is_directory:
            print(f"[MODIFY] {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"[DELETE] {event.src_path}")

    def on_moved(self, event):
        if not event.is_directory:
            print(
                f"[RENAME] {event.src_path} -> {event.dest_path}"
            )


def start_monitor(path):

    target = Path(path).resolve()

    if not target.exists():
        print(f"[ERROR] Directory does not exist: {target}")
        return

    if not target.is_dir():
        print(f"[ERROR] Path is not a directory: {target}")
        return

    print("=" * 60)
    print("RANSOMWATCH FILE MONITOR")
    print("=" * 60)
    print(f"Monitoring: {target}")
    print("Press CTRL+C to stop")
    print("=" * 60)

    event_handler = RansomWatchHandler()

    observer = Observer()
    observer.schedule(
        event_handler,
        str(target),
        recursive=True
    )

    observer.start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n[!] Stopping monitor...")

        observer.stop()

    observer.join()