import os

dataDirs = ["importacoes-e-exportacoes-de-etanol", 
            "importacoes-gas-natural", 
            "b-importacoes-e-exportacoes-de-petroleo",
            "b-importacoes-e-exportacoes-de-derivados-de-petroleo"]


for directory in dataDirs:
    if os.path.isdir(directory):
        importTables = os.listdir(os.path.join(directory, "importacao"))
        exportTables = os.listdir(os.path.join(directory, "exportacao"))
        for table in importTables:
            if not "new" in table:
                f = open(os.path.join(directory, ("importacao/" + table)), "r", encoding="ISO-8859-1")
                rows = f.readlines()
                f.close()
                newF = open(os.path.join(directory, ("importacao/" + table)), "w+", encoding="utf-8")
                newF.writelines(rows)
                newF.close()
