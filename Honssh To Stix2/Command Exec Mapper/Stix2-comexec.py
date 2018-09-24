from stix2 import ObservedData,MemorySink,CustomObservable,properties
from os import listdir
from os.path import isfile, join

@CustomObservable('command-executed', [
('command', properties.StringProperty(required=True)),
])
class NewObservable():
    pass


def command_observable(comm,timestamp):
    com=NewObservable(command=comm)
    obs = ObservedData(first_observed=timestamp,
                       last_observed=timestamp,
                       number_observed=1,
                       objects={'0':com})
    wrt.add(obs)

def main_mapper(blutus):
    file = open(good[blutus], 'r')
    global wrt
    wrt = MemorySink()
    
    for line in file:
        a=line.split(':')
        if a[0].__contains__('Command Executed'):
            b=a[0].split(' ')
            c = str(b[0].replace('_', ''))
            c = c[:4] + '-' + c[4:6] + '-' + c[6:8] + 'T' + c[8:10] + ':' + c[10:12] + ':' + c[12:14] + '.' + c[14:] + 'Z'
            command_observable(a[1],c)
            
        wrt.save_to_file(good[blutus]+'.json')
            

mypath = str("X:/Cyber Security/Mapper")    #  path to folder where logs are stored
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
totalfiles = len(onlyfiles)

print("All files in the folder are : "+str(onlyfiles))

good = []

for x in range(0, totalfiles):
    allfilespath = mypath + '/' + onlyfiles[x]
    good.append(allfilespath)



for x in range (0, totalfiles):
    main_mapper(x)
    