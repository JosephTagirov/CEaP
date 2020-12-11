ralph = 'It chanced during one winter, a few years ago, that our cities were bent on discussing the theory of the Age. By an odd coincidence, four or five noted men were each reading a discourse to the citizens of Boston or New York, on the Spirit of the Times. It so happened that the subject had the same prominence in some remarkable pamphlets and journals issued in London in the same season. To me, however, the question of the times resolved itself into a practical question of the conduct of life. How shall I live? We are incompetent to solve the times. Our geometry cannot span the huge orbits of the prevailing ideas, behold their return, and reconcile their opposition. We can only obey our own polarity. Tis fine for us to speculate and elect our course, if we must accept an irresistible dictation.'
list1=ralph.split()
a = [list1.count(list1[i]) for i in range(len(list1))]
for i in range(len(a)):
    print(list1[i], a[i])
