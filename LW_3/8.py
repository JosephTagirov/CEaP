paragraph = """Cold frost and sunshine: day of wonder!
But you, my friend, are still in slumber —
Wake up, my beauty, time belies:
You dormant eyes, I beg you, broaden
Toward the northerly Aurora,
As though a northern star arise!"""
a = paragraph.split(" ")
b = {}
for i in range(len(a)):
    b[a[i]] = i
print(b)
