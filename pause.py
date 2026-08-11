import subprocess
import get_last
def main():
    id = get_last.main()
    if get_last != False:
        subprocess.run(("podman", "stop", id))
        print(f"Wstrzymano kontener {id}")
        return True
    else:
        return False