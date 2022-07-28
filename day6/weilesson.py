import random
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df=pd.DataFrame(columns=['A体重','B体重'])

for i in range(1,32):
    wei_a=random.uniform(80,84)
    wei_b=random.uniform(78,82)
    df.loc[str(i)+"日"]=[wei_a,wei_b]
df.plot(figsize=(15,8))
plt.ylim(70,90)
plt.grid()
plt.show()
