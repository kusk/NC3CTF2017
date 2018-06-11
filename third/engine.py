import binascii
import os
import hashlib
import random
from collections import defaultdict
dd = open("root", "wb")

print("Laver dd")
dd.write("FjolletFS0.1".encode('ascii'))
fill = 0
while fill < 15: #mb
	dd.write(b"\x00"*1000000)
	fill += 1
print("----"*20)
dd.seek(0)
#placeringer = {}
placeringer = defaultdict(list)
filnavne = defaultdict(list)

def search_offset_table(myDict, lookup):
    for key, value in myDict.items():
        for v in value:
            if lookup in v:
                return key

def search_offset():
	c = 0
	while c == 0:
		num = random.randint(20,2200)
		#print(search(d, '5'))
		if search_offset_table(placeringer, str(num)) == None:
			return str(num)
			c=1


for root, directories, filenames in os.walk('filsystem/'):
	for directory in directories:
		print(os.path.join(root, directory))
		print(os.path.getsize(os.path.join(root, directory)))

	for filename in filenames: 
		path_fil = os.path.join(root,filename)
		file_id = hashlib.md5(path_fil.encode('utf-8')).hexdigest()
		print("Filnavn: "+os.path.join(root,filename)+" / Filesize: "+str(os.path.getsize(os.path.join(root,filename)))+" / ID: "+file_id)
		filnavne[file_id].append(os.path.join(root,filename))

		if(os.path.getsize(os.path.join(root,filename)) < 4096):
			offset = search_offset()
			offset_set = int(offset) * 4096
			print("Cluster: "+str(offset)+" / Offset: "+str(offset_set))
			dd.seek(offset_set)
			filen = open(os.path.join(root,filename), 'rb')
			dd.write(filen.read(4096))
			filen.close()
			#placeringer[file_id] = str(offset)
			placeringer[file_id].append(offset)
		else:
			filesize = os.path.getsize(os.path.join(root,filename))
			seeker = 0
			while seeker < filesize:
				if seeker+4096 > filesize:
					print("Seeker: "+str(seeker))
					offset = search_offset()
					offset_set = int(offset) * 4096
					print("Cluster: "+str(offset)+" / Offset: "+str(offset_set))
					dd.seek(offset_set)
					filen = open(os.path.join(root,filename), 'rb')
					filen.seek(seeker)
					dd.write(filen.read(4096))
					filen.close()
					print("sidste")
					placeringer[file_id].append(offset)
					seeker = seeker+4096
					break
				else:
					#print("Seeker: "+str(seeker))
					offset = search_offset()
					offset_set = int(offset) * 4096
					#print("Cluster: "+str(offset)+" / Offset: "+str(offset_set))
					dd.seek(offset_set)
					filen = open(os.path.join(root,filename), 'rb')
					filen.seek(seeker)
					dd.write(filen.read(4096))
					filen.close()

					placeringer[file_id].append(offset)
					seeker = seeker+4096



		print()



print("filetable:")
#print(filnavne)
dd.seek(512)
for filID, filnavn  in filnavne.items():
	print(filID+"/"+str(filnavn))
	dd.write(filID.encode('ascii'))
	dd.write(b"\x00")
	fil = str(filnavn).strip("['']")
	dd.write(fil.encode('ascii'))
	dd.write(b"\x00\xFF\xFF")

dd.write(b"\x00\xFF\x00")
print("offsettable:")


for filID, offsets in placeringer.items():
	dd.write(filID.encode('ascii'))
	dd.write(b"\x00")
	off = str(offsets).replace("['",'').replace("']",'').replace("'",'').replace(",",'').encode('ascii')
	dd.write(off)
	dd.write(b"\x00\xFF")


#print(placeringer)
dd.close()

#7b47592a50a673eaa055bce107328350/['filsystem/pics/dwm-20120806.png'] flag