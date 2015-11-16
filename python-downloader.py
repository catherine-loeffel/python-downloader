import urllib

outputFolder = './output/'
file = open('examplelinks.txt')

print 'Running Python Downloader...'
with file as f:
    for line in f:
        filename = outputFolder + line.rsplit('/', 1)[-1].strip()
        print 'downloading ' + line + ' as ' + filename
        urllib.urlretrieve(line, filename)


