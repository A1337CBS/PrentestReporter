
import matplotlib.pyplot as plt
import numpy as np

label = ['Critical', 'High', 'Medium', 'Low', 'Info']

no_vulns = [
    1, 2, 5, 6, 3
]

def plot_bar_x():
    # this is for plotting purpose
    index = np.arange(len(label))
    yindex = range(0,max(no_vulns)+1)
    print(yindex)
    plt.bar(index, no_vulns, color=['purple','red','orange','blue','green'])
    plt.xlabel('Severity', fontsize=10)
    plt.ylabel('No. of Vulnerabilities', fontsize=10)
    plt.xticks(index, label, fontsize=10, rotation=0)
    yint = [0,1,2,3,4,5]
    plt.yticks(yindex, yindex, fontsize=10, rotation=0)
    plt.title('Vulnerabilities by severity')
    plt.show()

plot_bar_x()