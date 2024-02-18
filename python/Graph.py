import matplotlib.pyplot as plt

def graph( figwidth = 8, x_pos = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'], x = [a for a in range(7)], y = [b for b in range(7)], x_label = 'week', y_label = 'percentage', graph_title = 'week graph'):
    plt.figure().set_figwidth(figwidth)
    
    plt.xticks(x,x_pos)
    plt.plot(x,y,color = "green", linestyle= "dashed", linewidth = "1", marker ="o", markerfacecolor = "blue", markersize = "6")
    
    plt.ylim(0,100)

    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.title(graph_title)
