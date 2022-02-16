# cit1113
# Alex Brown
# Lecture G

"""
# Pseudocode that calculates volume of a cube given an edge length

start
    output "Enter edge length of cube"
    input edge
    set volume = edge ** 3
    output "Volume of cube with edge length", edge, "is", volume
end
"""




def cubeVolume(edge = None):
    # Python function that calculated volume of a cube given an edge length
    if (edge==None):
        # If no edge value is given, the function will prompt the user for an edge length
        print("Enter edge length of cube")
        edge = float(input(">"))

    volume = edge ** 3
    return volume

def main():
    # Main function
    print(cubeVolume())

if __name__ == "__main__":
    # Run main if being run as script
    main()