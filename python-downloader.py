import urllib

outputFolder = './output/'
file = open('examplelinks.txt')

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



