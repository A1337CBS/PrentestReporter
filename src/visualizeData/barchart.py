
import matplotlib.pyplot as plt
import numpy as np
from src.models.Vulnerability import Vulnerability
from src.models.Project import Project
from src.common.Database import Database
Database.initialize()

label = ['Critical', 'High', 'Medium', 'Low', 'Info']
report_id = "baf03af5f64e438a9bad9b161863782b"

no_vulns = Vulnerability.getVulnerabilitiesSeverities(report_id=report_id)
print(no_vulns)

def plot_bar_x():
    # this is for plotting purpose
    index = np.arange(len(label))
    yindex = range(0,max(no_vulns)+1)
    plt.bar(index, no_vulns, color=['purple','red','orange','blue','green'])
    plt.xlabel('Severity', fontsize=10)
    plt.ylabel('No. of Vulnerabilities', fontsize=10)
    plt.xticks(index, label, fontsize=10, rotation=0)
    yint = [0,1,2,3,4,5]
    plt.yticks(yindex, yindex, fontsize=10, rotation=0)
    plt.title('Vulnerabilities by severity')
    #plt.show()
    plt.savefig('bargraph.png')

plot_bar_x()
