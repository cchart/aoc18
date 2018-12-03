import sys  
import os

def main():
    if len(sys.argv) > 1:
        inputfile = sys.argv[1]
    else:
        inputfile = 'input'
    if not os.path.isfile(inputfile):
        print("File path {} does not exist. Exiting...".format(inputfile))
        sys.exit()

    frq = 0 # starting frequency drift
    with open(inputfile) as f:
        l = f.readline()
        while l:
            frq += int(l)
            l = f.readline()
    
    print ("Final Frequency:\n{}\n\n".format(frq))
        


if __name__ == '__main__':
    main()
