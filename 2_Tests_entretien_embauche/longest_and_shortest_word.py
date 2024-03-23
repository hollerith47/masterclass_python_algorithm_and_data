# Trouver le mot le plus court et le plus long dans une phrase
# le premier par ordre alphabetique
def longest_and_shortest_string(str):
    words_array = str.lower().split()
    longest = max(words_array, key=len)
    shortest = min(words_array, key=len)
    return shortest, longest


#  trie par odre alphabetique
def get_min_and_max_string_sorted(str):
    words_array = str.lower().split(" ")
    min_word, max_word = longest_and_shortest_string(str)
    
    all_min_words = [w.lower() for w in words_array if len(w) == len(min_word)]
    all_max_words = [w.lower() for w in words_array if len(w) == len(max_word)]
    
    all_min_words.sort()
    all_max_words.sort()
    
    return all_min_words[0], all_max_words[0]


s = "Un aa chasseu sachant chasser sans son chien est un bon chasseu"
# min_word, max_word = longest_and_shortest_string(s)
min_word, max_word = get_min_and_max_string_sorted(s)
print("Mot le plus petit", min_word)
print("Mot le plus long", max_word, flush=True)
