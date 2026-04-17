
eleje = ["asztal", "pók", "tűz"]
vege = ["láb", "háló", "oltó"]

def combine_words(eleje, vege):
    eredmények = []
    for a, b in zip(eleje, vege):
        új_szó = a + b
        eredmények.append(új_szó)
    return eredmények
print(combine_words(eleje,vege))