def rem(l,word):
    for i in l:
      l.remove(word)
      return l



l=["hariom","ravi","pankaj", "ansh","an"]

a=rem(l,"an")
print(a)

