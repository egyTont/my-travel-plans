import urllib
import time
def reading():
    quote=open("C:\Users\DEADpc\Desktop\New folder\movie_quotes.txt")
    content_of_file=quote.read()
    #print content_of_file
    quote.close
    spell_check(content_of_file)
def spell_check(words_to_check):
    connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+words_to_check)
    output=connection.read()
    #print output
    connection.close()
    if "true" in output:
        print ("A curse word in the text no cursing on my watch")
    elif "false" in output:
        print ("No curse word found")
    else:
        print (" i am a stupid program i cant do anything right")
    time.sleep(10)
reading()
    
