
import glob 
from PIL import Image
import sys
import os
from natsort import natsorted

os.remove("IMPORTintoANKI.tsv") #deletes the old tsv-file 

zähler = 1

for file in glob.glob("/Users/florianschwab/Desktop/Import Index Cards/*.jpg"): #this should be the path of the folder where the good notes jpg flashcards are 
    filesplit = file.split('/')
    filesplit = filesplit[5]
    filesplit = filesplit.split(' ')
    filesplit = filesplit[1]
    filesplit = filesplit.split('-')
    filesplit = filesplit[0]
    
    img = Image.open(file)
    area1 = (0,0,1668,1077)
    croppedimage1 = img.crop(area1)
    area2 = (0,1077,1668,2154)
    croppedimage2 = img.crop(area2)
    
    #the path below is where Anki stores the pictures with their names and searches for them with the .tsv file 
    croppedimage1.save(r'/Users/florianschwab/Library/Application Support/Anki2/User 1/collection.media/'+str(filesplit)+str(zähler)+'.png')
    croppedimage2.save(r'/Users/florianschwab/Library/Application Support/Anki2/User 1/collection.media/'+str(filesplit)+str(zähler+1)+'.png')
    
    #this path is a folder that stores the exact same pictures just temporarily and deletes them after used
    croppedimage1.save(r'/Users/florianschwab/Desktop/Überbrückung/'+str(filesplit)+str(zähler)+'.png')
    croppedimage2.save(r'/Users/florianschwab/Desktop/Überbrückung/'+str(filesplit)+str(zähler+1)+'.png')
    
    zähler+=2
    
    print(filesplit,zähler)
    print(filesplit,zähler+1)
    
if __name__ == '__main__':
    file_path = "/Users/florianschwab/Desktop/Überbrückung" #change path for the folder that just stores temporarily
    if len(sys.argv) > 1:
        file_path = sys.argv[1]

    files = [x for x in natsorted(os.listdir(file_path)) if x.endswith(('jpg', 'jpeg','gif', 'png'))]

    if len(files) % 2 != 0:
        print("Odd number of files in directory %s, results might be off." % (file_path))

    pairs = zip(files[0::2], files[1::2]) #

    with open('IMPORTintoANKI.tsv', 'w') as output_file: #this is the name of the .tsv file that should be imported into anki
        for pair in pairs:
            output_file.write('<img src="%s" />\t<img src="%s" />%s' % (pair[0], pair[1], os.linesep)) 
            
for filename in os.listdir("/Users/florianschwab/Desktop/Überbrückung"): #the folder gets deleted
    os.remove("/Users/florianschwab/Desktop/Überbrückung/"+str(filename))
    
for filename in os.listdir("/Users/florianschwab/Desktop/Import Index Cards"): #the old flashcards that just got imported are deleted (optional)
    os.remove("/Users/florianschwab/Desktop/Import Index Cards/"+str(filename))
    
print("Finished")
