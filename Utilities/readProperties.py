import configparser

config=configparser.ConfigParser(interpolation=None)
config.read(".\\Configurations\\config.ini")

class readConfig():
    @staticmethod
    def getURL():
        url=config.get("main", 'baseURL')
        return url;
    @staticmethod
    def getProductURL():
        prodURL=config.get("main", "productURL")
        return prodURL;

    @staticmethod
    def getMainPageTitle():
        title=config.get("main", "mainpageTitle")
        return title
    
    @staticmethod
    def getProductName():
        productname=config.get("main", "productname")
        return productname;

    @staticmethod
    def getProductpageURL():
        productpageURL=config.get("main", "productpageURL")
        return productpageURL;

    @staticmethod
    def getProductpageTitle():
        productpagetitle=config.get("main", "prodPageTitle")
        return productpagetitle;


    @staticmethod
    def get_iqooTornadoGreen_page_title():
        iqooTG_page_title=config.get("main", "iqooTornadoGreen_page_title")
        return iqooTG_page_title