def prefix_finder(string_to_process):
    prefixes = list()
    prefixes.append(string_to_process)
    letter_list = list(string_to_process)
    for w in range(len(letter_list)):
        letter_list.pop()
        if letter_list:
            prefixes.append("".join(letter_list))
    return prefixes


def suffix_finder(string_to_process):
    suffixes = list()
    suffixes.append(string_to_process)
    letter_list = list(string_to_process)[::-1]
    for w in range(len(letter_list)):
        letter_list.pop()
        if letter_list:
            suffixes.append("".join(letter_list[::-1]))
    return suffixes


def similarity_score_calculator(prefix_list, suffix_list):
    similarity_score = 0
    for suffix in suffix_list:
        if suffix[0] != prefix_list[0][0]:
            continue
        elif suffix in prefix_list:
            similarity_score += len(suffix)
        else:
            check_word = suffix[:-1]
            for w in range(len(check_word)):
                if check_word in prefix_list:
                    similarity_score += len(check_word)
                    break
                elif check_word:
                    # check_word = suffix[:-1] yaptıktan sonra check_word
                    # boş gelmesi ihtimaline karşı
                    check_word = check_word[:-1]
                    # suffix in sonundan bir harf çıkartıp kontrol edildiğinde
                    # prefix listesinde çıkmıyorsa harf bitene kadar suffix
                    # sonundan harf çıkartıp kontrole devam etmek için
    return similarity_score


if __name__ == '__main__':

    test_case_number = int(input("How many test case do you need?: "))

    strings_to_process = []
    print("Please enter your test cases:")
    for i in range(test_case_number):
        strings_to_process.append(input())

    for elem in strings_to_process:
        prefix_list_of_string = prefix_finder(elem)
        suffix_list_of_string = suffix_finder(elem)
        print(similarity_score_calculator(prefix_list_of_string,
                                          suffix_list_of_string))
