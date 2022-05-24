def find_anagrams(word1, word2):

    if(sorted(word1)==sorted(word2)):
      return True
    else:
      return False

find_anagrams("hello", "hello")
find_anagrams("won", "now")
find_anagrams("ello", "hllo")

print(find_anagrams("hello", "hello")) 
print(find_anagrams("won", "now")) 
print(find_anagrams("ello", "hllo"))