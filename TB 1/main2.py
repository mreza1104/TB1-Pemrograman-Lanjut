import re

def main():
  
    with open("code.txt", "r") as file:
       
        col_row = list(map(int, file.readline().split()))
        row = col_row[0]
        col = col_row[1]
        
     
        matrix = []
        for i in range(row):
            matrix_item = file.readline().rstrip()
            rw = list(matrix_item) + [' '] * (col - len(matrix_item))
            matrix.append(rw)

    
    deco_script = ""
    for i in list(zip(*matrix)):
        deco_script += "".join(i)

    
    decoded_script = re.sub(r'\b[^a-zA-Z0-9]+\b', " ", deco_script)

    # Menampilkan output
    print(decoded_script)

if __name__ == "__main__":
    main()
