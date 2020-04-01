# INPUT FORM
# [("a", 1), ("a", 3), ("a", 5), ("b", 2), ("b", 6), ("c", 1), ("c", 2), ("c", 3), ("c", 4), ("c", 5), ("d", 4), ("d", 5), ("d", 6), ("d", 7), ("e", 1), ("e", 3), ("e", 5), ("e", 6)]
# BY TANISHQ GUPTA

visitors = eval(input())
k = int(input())
websites_visitors = {}
for i, j in visitors:
    if i not in websites_visitors:
        websites_visitors[i] = set()
    websites_visitors[i].add(j)
all_websites = list(websites_visitors.keys())
updated_dictionary = {}
for i in range(len(all_websites)):
    for j in range(i+1, len(all_websites)):
        common = websites_visitors[all_websites[i]] | websites_visitors[all_websites[j]]
        not_common = websites_visitors[all_websites[i]] & websites_visitors[all_websites[j]]
        similarity = len(not_common) / len(common)
        updated_dictionary[(all_websites[i], all_websites[j])] = similarity
print(updated_dictionary)
values = list(updated_dictionary.values())
values.sort(reverse=True)
print(values)
for i in range(1, k+1):
    for key, value in updated_dictionary.items():
        if value == values[i-1]:
            print(key, end=' ')