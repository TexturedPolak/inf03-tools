import get_last
import start

def main():
    id = get_last.main()
    if id != False:
        return start.main(id, "")
    else:
        return False
    
    
