import os


class StringFormatter:
    def shortFileString(self, path):
        if self.isNone(path):
            return None
        if self.isEmpty(path):
            return ''
        self.isPath(path)
        short = os.path.basename(path)
        name = os.path.splitext(short)[0]
        newFile = name + '.tmp'
        return newFile.upper()

    def isPath(self, path):
        if os.path.isfile(path):
            return True
        raise ValueError

    def isEmpty(self, path):
        if path is '':
            return True
        else:
            return False

    def isNone(self, path):
        if path is None:
            return True
        else:
            return False
