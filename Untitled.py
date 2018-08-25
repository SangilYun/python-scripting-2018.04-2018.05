def count_letters(word_list):
    """ See question description """

    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    for letter in ALPHABET:
        count=ALPHABET.count(letter)

        letter_count[letter] = 0

    # enter code here
    for i in range(len(word_list)) :
        for j in word_list[i] :
            print("word_list:",word_list[i])
            letter_count[j] += 1

    max = 0
    max_key = ""
    # print(letter_count.keys())
    for i in letter_count.keys() :
        if max <= letter_count[i] :
            # print("i : ",i)
            # print(letter_count[i])
            max= letter_count[i]
            max_key = i

    return max_key
input_word = "hello world"
input = input_word.split(" ")
# print(input)
# print(count_letters(input))
#
monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"
monty_words = monty_quote.split(" ")
# print(monty_words)
# print(count_letters(monty_words))


# def get_file_lines(file):
#     splitfile = file.split('\n')
#     lst = filter(None, splitfile)
#     print(type(lst))
#     return lst
#
# # Output returned by this function
# print("1 Output:  ", get_file_lines('abcde\nfghij\n'))
#
# # Here is one way to extract contents
# print("2 Contents:  ", list(get_file_lines('abcde\nfghij\n')))
#
# # Another way to extract contents
# L = []
# for line in get_file_lines('abcde\nfghij\n'):
#     L.append(line)
# print("3 Contents:  ",L)
#
# # Output:
# # <class 'filter'>
# # 1 Output:   <filter object at 0x03425EF0>
# # <class 'filter'>
# # 2 Contents:   ['abcde', 'fghij']
# # <class 'filter'>
# # 3 Contents:   ['abcde', 'fghij']


sum = lambda x : x**2
print(sum(2))

a=list(range(3))
b=a

b.append(4)

print(a)
print(b)
