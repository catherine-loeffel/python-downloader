from sys import argv
import urllib

outputFolder = './output/'
inputfile = 'examplelinks.txt'

if len(argv) == 2:
    inputfile = argv[1]

try:
    file = open(inputfile)
    print 'Running Python Downloader...'
    with file as f:
        for line in f:
            filename = outputFolder + line.rsplit('/', 1)[-1].strip()
            print '\ntrying to download: ' + line.strip()
            try:
                urllib.urlretrieve(line, filename)
                print 'saved as ' + filename
            except IOError:
                print 'could not find file'
                pass
except IOError:
    print 'could not open file: ' + inputfile





