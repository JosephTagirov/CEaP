hamlet = """And there did seem in him a kind of joy
To hear of it: They are about the court;
And, as I think, they have already order
This night to play before him."""
ralph = """Savages cling to a local god of one tribe or town. The broad ethics of Jesus were quickly narrowed to village theologies, which preach an election or favoritism. And, now and then, an amiable parson, like Jung Stilling, or Robert Huntington, believes in a pistareen-Providence, which, whenever the good man wants a dinner, makes that somebody shall knock at his door, and leave a half-dollar."""
hh = hamlet.split(' ')
rr = ralph.split(' ')
for i in range(len(hh)):
    if hh[i] in rr:
        print(hh[i])
    elif hh[i] not in rr:
        print(hh[i])
