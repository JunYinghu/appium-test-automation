class GetPath(object):
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def getPath(self, section, flag):
        getElemPath = self.config.get(section, flag)
        return getElemPath