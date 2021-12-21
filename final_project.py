import math
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn import naive_bayes
color = ['black', 'white', 'saddlebrown', 'red', 'peru', 'darkorange', 'gold', 'khaki', 'yellow', 'lawngreen', 'darkgreen', 'cyan', 'deepskyblue', 'steelblue', 'royalblue', 'navy', 'indigo', 'darkviolet', 'purple', 'magenta', 'crimson']

def read_data(filename):
    data_set = []
    with open(filename, 'r') as f:
        lines = csv.reader(f)
        keys = []
        for line in lines:
            if line and not line[0].strip().startswith('#'):
                dict = {}
                for idx, val in enumerate(line):
                    if val.strip().replace('.', '').isdecimal():
                        val = float(val)
                    dict[keys[idx].replace('#', '')] = val
                data_set.append(dict)
            else:
                keys = [val.replace('"', '') for val in line]
    return data_set

def get_corr(x, y):
    m_x, m_y = [], []
    for val in x:
        m_x.append(sum(val)/len(val))
    for val in y:
        m_y.append(sum(val)/len(val))
    return np.corrcoef(np.vstack((np.array(m_x), np.array(m_y))))

def get_transpose(deg, xs):
    M = np.empty((0, len(xs)))
    for i in range(deg+1):
        M = np.vstack((xs**i, M))
    return M.T

if __name__ == '__main__':
    tfr = read_data("TFR.csv")
    rep = read_data("avgREP.csv")

    # correlation tfr-rep
    tfr_val, rep_val = [], []
    for i in range(len(rep)):
        tfr_val.append(list(tfr[i].values())[7:])
        rep_val.append(list(rep[i].values())[1:])
    tfr_val, rep_val = np.array(tfr_val).T, np.array(rep_val).T

    corr_tfr_rep = get_corr(tfr_val, rep_val)

    plt.figure()
    plt.title(f'Correlation between Total Fertility Rate and Real Estate Price ({corr_tfr_rep[0][1]:.3f})')
    plt.xlim([np.min(tfr_val)-0.3, np.max(tfr_val)+0.3])
    plt.xlabel('Total Fertility Rate (One per childbearing woman)')
    plt.ylim([np.min(rep_val)-20, np.max(rep_val)+20])
    plt.ylabel('Real Estate Price (2017.4Q=100))')
    plt.grid()
    for i in range(len(tfr_val)):
        plt.scatter(tfr_val[i], rep_val[i], marker='.', c=color[i], edgeColor="black", s=200, label=str(2006+i))
    plt.legend()
    plt.show()


    # correlation tfr-div
    tfr_val= []
    for i in range(len(tfr)):
        tfr_val.append(list(tfr[i].values())[1:])
    tfr_val = np.array(tfr_val).T

    div = read_data('divorce.csv')
    div_val = []
    for i in range(len(div)):
        div_val.append(list(div[i].values())[1:])
    div_val = np.array(div_val).T

    corr_tfr_div = get_corr(tfr_val, div_val)

    plt.figure()
    plt.title(f'Correlation between Total Fertility Rate and Divorce Rate ({corr_tfr_div[0][1]:.3f})')
    plt.xlim([np.min(tfr_val)-0.3, np.max(tfr_val)+0.3])
    plt.xlabel('Total Fertility Rate (One per childbearing woman)')
    plt.ylim([np.min(div_val)-0.5, np.max(div_val)+0.5])
    plt.ylabel('Crude Divorce Rate')
    plt.grid()
    for i in range(len(tfr_val)):
        plt.scatter(tfr_val[i], div_val[i], marker='.', c=color[-i], edgeColor="black", s=200, label=str(2000+i))
    plt.legend()
    plt.show()


    # Predict tfr to 2035
    xsp = np.linspace(-2, 45, 200)
    year = np.array([i for i in range(21)])
    tfr_val = np.array(list(tfr[0].values())[1:])

    exp_fit = np.polyfit(year, np.log(tfr_val), 1)
    exp_y = np.exp(exp_fit[1])*np.exp(exp_fit[0]*xsp)

    coeff = np.matmul(np.linalg.pinv(get_transpose(2, year)), tfr_val)
    poly_y = np.matmul(get_transpose(2, xsp), coeff)
    y2 = []
    for i, v in enumerate(exp_y):
        y2.append(math.sqrt((v**2 + poly_y[i]**2)/2))

    coeff = np.matmul(np.linalg.pinv(get_transpose(3, year)), tfr_val)
    poly_y = np.matmul(get_transpose(3, xsp), coeff)
    y3 = []
    for i, v in enumerate(exp_y):
        y3.append(math.sqrt((v**2 + poly_y[i]**2)/2))

    plt.figure()
    plt.title('Prediction of Total Fertility Rate using Curve Fitting')
    plt.xlim([-2, 35])
    plt.xlabel('year (0: 2000)')
    plt.ylim([np.min(tfr_val)-0.3, np.max(tfr_val)+0.3])
    plt.ylabel('Total Fertility Rate (One per childbearing woman)')
    for i in range(len(tfr_val)):
        plt.scatter(i, tfr_val[i], marker='o', c='red')
    plt.plot(xsp, exp_y, 'r-', label='exp')
    plt.plot(xsp, y2, 'b-', label='2*exp')
    plt.plot(xsp, y3, 'g-', label='3*exp')
    plt.legend()
    plt.show()
