import re

class FileNameExtractor:
    def extract_file_name(self, dirty_file_name):
        m = re.match(r"(\d+)\_(\w+)\.(\w+)\.(\w+)", dirty_file_name)
        return (str(m.groups()[1]) + '.' + str(m.groups()[2]))
		
f = FileNameExtractor()
print (f.extract_file_name("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION"))
print (f.extract_file_name("1_FILE_NAME.EXTENSION.OTHEREXTENSIONadasdassdassds34"))