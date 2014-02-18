#class to hold all functionality between words

import urllib2
class WordChecker:
    #returns true if the two words match, false otherwise
    #this is accomplished by making a request to http://stevehanov.ca/cgi-bin/poet.cgi?WORD

    rhymeRequest = "http://stevehanov.ca/cgi-bin/poet.cgi?"
    def isRhyme(self, word1, word2):
        #make a request for word1
        req1 = urllib2.Request(self.rhymeRequest + word1)
        response1 = urllib2.urlopen(req1)
        page1 = response1.read()
        lines1 = page1.splitlines()

        #make a request for word 2
        req2 = urllib2.Request(self.rhymeRequest + word2)
        response2 = urllib2.urlopen(req2)
        page2 = response2.read()
        lines2 = page2.splitlines()

        #if the two words have a word incommon they must rhyme
        if(lines1[1] == lines2[1]):
            return True
        return False
