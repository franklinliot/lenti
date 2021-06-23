def editFormatting(ProductName):
    if (ProductName.find('ACUVUE') != -1):
        ProductName = str.replace(ProductName, "ACUVUE", "Acuvue")
    elif (ProductName.find('DAILIES') != -1):
        ProductName = str.replace(ProductName, "DAILIES", "Dailies")
    elif (ProductName.find('1 Day') != -1):
        ProductName = str.replace(ProductName, "1 Day", "1-Day")
    