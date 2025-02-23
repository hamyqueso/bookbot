def count_words(text):
    return len(text.split())

def count_characters(text):
    results = {}
    for word in text.split():
        for char in word:
            try:
                results[char.lower()] += 1
            except:
                results[char.lower()] = 1

    return results

def pretty_print(dict):
    resulting_list = []
    for key, value in dict.items():
        if key.isalpha():
            resulting_list.append({"key":key, "num":value})

    # print(sorted(resulting_list, reverse=True, key=lambda x: x["num"]))
    for item in sorted(resulting_list, reverse=True, key=lambda x: x["num"]):
        print(f"{item['key']}: {item['num']}")