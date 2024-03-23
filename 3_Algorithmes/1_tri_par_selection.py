# tri par selection
# Au lieu d'utiliser la methode l.sort(), on va trier par nous meme
# O[N^2] complexité de l'algorithme

import random

# l = [5, 10, 15, 20, 25, 30, 3, 6, 12, 18, 24]


def generate_random_list(n, min_item, max_item):
    l = []
    for i in range(n):
        l.append(random.randint(min_item, max_item))
    return l


def selection_sort(liste_a_trier):
    for unsorted_index in range(0, len(liste_a_trier) - 1):
        min = liste_a_trier[unsorted_index]
        # print(unsorted_index, l[unsorted_index], 'Min=', min)
        min_index = unsorted_index
        for i in range(unsorted_index + 1, len(liste_a_trier)):
            if liste_a_trier[i] < min:
                min = liste_a_trier[i]
                min_index = i
        liste_a_trier[min_index] = liste_a_trier[unsorted_index]
        liste_a_trier[unsorted_index] = min
    return liste_a_trier


if __name__ == '__main__':
    list2 = generate_random_list(100, -1000, 100)
    print("UNSORTED LIST", list2)

    list2_sorted = selection_sort(list2)
    print("SORTED LIST: ", list2_sorted)
