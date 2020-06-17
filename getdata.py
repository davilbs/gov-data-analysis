import os
import sys
from selenium import webdriver

# Setup for Firefox options
firefoxOptions = webdriver.FirefoxOptions()
firefoxOptions.set_preference("browser.download.folderList", 2)
firefoxOptions.set_preference("browser.download.dir", "/home/davilbs/Code/gov-data-analysis")
firefoxOptions.set_preference("browser.download.useDownloadDir", True)
# Disable save prompt for csv and pdf mime types
firefoxOptions.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv,application/pdf")
# Disable inner pdf reader
firefoxOptions.set_preference("pdfjs.disabled", True)

driver = webdriver.Firefox(options=firefoxOptions)

baseURL = "http://www.dados.gov.br/dataset/"
DATASETS = ["importacoes-e-exportacoes-de-etanol", 
            "importacoes-gas-natural", 
            "b-importacoes-e-exportacoes-de-petroleo",
            "b-importacoes-e-exportacoes-de-derivados-de-petroleo"]

# Download by clicking on the links on each page
for dataset in DATASETS:
    driver.get(baseURL + dataset)

    linkList = driver.find_elements_by_class_name("resource-item")
    for link in range(1, len(linkList)):
        driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/article/div/section[2]/ul/li[{}]/div/a".format(link)).click()
        driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/article/div/section[2]/ul/li[{}]/div/ul/li[2]/a".format(link)).click()

# Create directories and moves tables and pdfs
    files = os.listdir()
    importDir = os.path.join(dataset, "importacao")
    exportDir = os.path.join(dataset, "exportacao")
    if not os.path.isdir(dataset):
        os.mkdir(dataset)
    if not os.path.isdir(importDir):
        os.mkdir(importDir)
    if not os.path.isdir(exportDir):
            os.mkdir(exportDir)
    for f in files:
        if ".csv" in f:
            if "importacao" in f:
                os.rename(f, os.path.join(importDir, f))
            elif "exportacao" in f:
                os.rename(f, os.path.join(exportDir, f))
            else:
                os.rename(f, os.path.join(dataset, f))
        if ".pdf" in f:
            os.rename(f, os.path.join(dataset, f))
