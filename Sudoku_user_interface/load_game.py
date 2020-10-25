import string
import os
import json

def codify_files(filename):

    inflie= open(filename, 'r')

    info= json.load(inflie)
    print(info['time'])
    
    for i in range(1, len(info['game'])):
        print(info['game'][str(i)])
    #print(info['game'])

    # #info= inflie.read()
    # # info_dict= dict(info)
    # #print(info)
    # #a=info.split(',')
    # #print(info)
    # temp= info[1:(len(info)-1)]
    # #print(temp)
    # #print(info[info.find(',')])
    # time_dict={}
    # time_dict[temp[1:(temp.find(':')-1)]]= temp[(temp.find(':')+2):(temp.find(','))]
    # #time_dict['time']= int(time_dict['time'])
    # #print(time_dict)
codify_files('prueba2.json')




# WORDLIST_FILENAME = "cowboys.txt"

# def load_words():
    
#     print("Loading word list from file...")
#     # inFile: file
    
#     inFile = open(WORDLIST_FILENAME, 'r')
#     # line: string
#     line = inFile.readline()
#     line=str.lower(line)
#     # wordlist: list of strings
#     wordlist = line.split()
#     print("  ", len(wordlist), "words loaded.")
#     return wordlist