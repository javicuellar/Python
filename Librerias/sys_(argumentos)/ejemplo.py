from sys import argv

def main():
    print("Argumento 1: ", argv[0])
    
    if len(argv) > 1:
        for argumento in argv[1:]:
            print("argumento: ", argumento)
    else:
        print("No hay más argumentos.")
       
if __name__ == "__main__":
    main()