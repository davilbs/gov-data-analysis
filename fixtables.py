import os

dataDirs = ["importacoes-e-exportacoes-de-etanol", 
            "importacoes-gas-natural", 
            "b-importacoes-e-exportacoes-de-petroleo",
            "b-importacoes-e-exportacoes-de-derivados-de-petroleo"]
#  ORIGINAL
def fixEncoding(filepath):
    f = open(filepath, "r", encoding="ISO-8859-1")
    rows = f.readlines()
    f.close()
    newF = open(filepath, "w+", encoding="utf-8")
    newF.writelines(rows)
    newF.close()
    f = open(filepath, "r", encoding="utf-8")
    rows = f.readlines()
    f.close()
    newF = open(filepath, "w", encoding="utf-8")
    newRows = []
    for row in rows:
        newRow = row.replace(",", ".").replace("Ã", "A").replace("Ç", "C").replace("É", "E").replace("Ó", "O")
        print("Row : " + row)
        print("newRow : " + newRow)
        newRows.append(newRow)
    newF.writelines(newRows)
    newF.close()

def fixTables(directory, flow):
    importTables = os.listdir(os.path.join(directory, flow))
    for table in importTables:
        filepath = os.path.join(directory, (flow + "/" + table))
        print("Filepath : " + filepath)
        fixEncoding(filepath)

for directory in dataDirs:
    for flow in os.listdir(directory):
        fPath = os.path.join(directory, flow)
        if os.path.isdir(fPath):
            print("Fixing : " + directory + " " + flow)
            fixTables(directory, flow)
            