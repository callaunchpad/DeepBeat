"""

255 = note on
0 = note off
"""

import numpy as np 
import sys, getopt
import png
# import mido
# from mido import MidiFile
import pretty_midi
from os import listdir
from os.path import isfile, join
from feature_extraction import midi_cqt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
         return
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print ('Input folder is "', inputfile)
   # print ('Output folder is "', outputfile)

   while(inputfile[-1:] == "/"):
      inputfile = inputfile[:len(inputfile)-1]

   onlyfiles = [inputfile+"/"+f for f in listdir(inputfile) if (isfile(join(inputfile, f)) and f[-4:] == ".mid")]

   for file in onlyfiles:
   		midi = pretty_midi.PrettyMIDI(file)
   		spect = midi_cqt(midi)
   		spect = (spect - np.min(spect))
   		spect = np.rot90(spect/np.max(spect) * 255)

   		pngWriter = png.Writer(spect.shape[1], spect.shape[0], greyscale = True)
   		outputName = file[:len(file)-3]+"png"
   		output = open(outputName, 'wb')
   		pngWriter.write(output, spect)
   		output.close()



if __name__ == "__main__":
   main(sys.argv[1:])
