from scrape import *
import matplotlib.pyplot as plt


x_pos=[]
for i in d1['country']:
    x_pos.append(i)

plt.bar(d1['country'],d1['deaths'],color='blue')
plt.xlabel("Country List")
plt.ylabel("Number of Deaths")
plt.title("Death Number of Each Country by 3/29/2022")
plt.tick_params(axis='x', rotation=90)
plt.show()


plt.bar(d3['country'],d3['population'],color='green')
plt.xlabel("Country List")
plt.ylabel("Population")
plt.title("Population of Each Country by 3/29/2022")
plt.tick_params(axis='x', rotation=90)
plt.show()

plt.bar(x_pos,d2['dose_total'],color='pink')
plt.xlabel("Country List")
plt.ylabel('Dose Number')
plt.title("Dose Number of Each Country by 3/29/2022")
plt.tick_params(axis='x', rotation=90)
plt.show()

plt.bar(d3['country'],d3['recovered'],color='red')
plt.xlabel("Country List")
plt.ylabel("Recovered Number")
plt.title("Recovered Number of Each Country by 3/29/2022")
plt.tick_params(axis='x', rotation=90)
plt.tick_params(axis='y', rotation=45)
plt.show()


plt.plot(d3['country'],d3['recovered']/d3['population'],color='black')
plt.title('Plot for Recovered Rate of Each Country by 3/29/2022')
plt.tick_params(axis='x', rotation=90)
plt.show()


