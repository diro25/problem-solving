import sys
faces_map = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}
input_data = sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    shapes = input_data[1:]
    
    total_faces = 0
    
    for shape in shapes:
        total_faces += faces_map[shape]
    print(total_faces)