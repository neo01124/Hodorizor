import subprocess
from scikits.audiolab import Sndfile
import os
import numpy as np

def convertAndRemoveVoice(inputfile):
	#print strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
	song_folder = os.getcwd()+'/'
	
	print inputfile[-3:]
	mp3_file = song_folder + inputfile
	wav_file = song_folder + inputfile[:-4] + '.wav'	#'song.wav'
	command = "ffmpeg " + "-i " +'"'+ mp3_file +'"'+" -y " + " -ac 2 " + " -ar 44100 " +'"'+ wav_file +'"'
	#print '\n'
	print command
	try:
		p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
		output = p.communicate()[0]
		#lyricfileess = song_folder + inputfile.replace('.mp3','_beatSynced.json')
		#origfileess = song_folder + inputfile.replace('.mp3','_original.json')
	except:
		print 'wav conversion problem'
		return 0
	original_wav = Sndfile(wav_file, 'r')
	audio = original_wav.read_frames(original_wav.nframes)
	#return audio
	#audio /= float(np.max(abs(audio)))  # normalize audio
	#outputAudio = np.zeros(original_wav.nframes)
	#print type(outputAudio)
	#for idx,frame in enumerate(audio):
		#print idx
		#print frame
	outputAudio = (audio[:,0]-audio[:,1])/2
	#print len(audio)
	print 2	
	new_filename = wav_file.replace('.wav','_VocalRemoved.wav')
	print new_filename
	output_wav = Sndfile(new_filename, 'w', original_wav.format, 1, original_wav.samplerate)
	output_wav.write_frames(outputAudio)
	output_wav.close()
	#original_wav.close()
	return 1
