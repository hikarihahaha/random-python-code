import matplotlib.pyplot as plt
Marks=[67,88,63, 77, 65]
Subject=["English","Physics","Chemistry","Biology","Maths"]
plt.axis("equal")
plt.pie(Marks,labels=Subject,explode=[0,0,0,0,0.2],autopct="%1.2f%%")
plt.show()