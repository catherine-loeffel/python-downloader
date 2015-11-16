from sys import argv
import urllib

# default constants
outputFolder = './output/'
inputFile = 'examplelinks.txt'

# read file from argument or keeping default
if len(argv) == 2:
    inputFile = argv[1]
print 'Running Python Downloader...'

try:
    file = open(inputFile)
    # looping over the file: line by line
    with file as f:
        for line in f:
            # taking everything after the last / as filename
            # outputFolder has to exist beforehand
            filename = outputFolder + line.rsplit('/', 1)[-1].strip()
            print '\nTrying to download: ' + line.strip()
            try:
                # downloading file, continues with error message when not found
                urllib.urlretrieve(line, filename)
                print 'Saved as ' + filename
            except IOError:
                print 'Could not find file'
                pass
except IOError:
    print 'Could not open file: ' + inputFile





