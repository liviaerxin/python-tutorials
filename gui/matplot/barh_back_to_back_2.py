import numpy as np
import matplotlib.pyplot as plt
from typing import List, Union

def pyramid_plot(ylabels: Union[List, np.ndarray], data_left, title_left, data_right, title_right, fig=None, **kwargs):
    if(fig is None):
        fig = plt.figure()

    y_pos = np.arange(len(ylabels))
    #empty_ticks = tuple('' for n in ylabels)
    
    height = 1
    axes_left = fig.add_subplot(121)
    axes_left.barh(y_pos, data_left, height=height, **kwargs)
    axes_left.invert_xaxis()
    axes_left.set(yticks=y_pos, yticklabels=ylabels)
    axes_left.yaxis.tick_right()
    axes_left.set(title=title_left)

    axes_right = fig.add_subplot(122)
    axes_right.barh(y_pos, data_right, height=height, **kwargs)
    axes_right.set(yticks=y_pos, yticklabels=[])
    axes_right.set(title=title_right)

    return fig
    
# Example data
people = ['Tom', 'Dick', 'Harry', 'Slim', 'Jim']
performance = 3 + 10 * np.random.rand(len(people))
salary = np.linspace(30,60,len(people))

print(f"people: {people}")
print(f"salary: {salary}")
print(f"performance: {performance}")

# Plot the data
pyrfig = plt.figure(1)
pyrfig = pyramid_plot(people, salary, 'Salary (thousands)', performance, 'Performance', pyrfig, align='center', alpha=0.4)
pyrfig.suptitle('Pyramid Plot')
#pyrfig.set_figwidth(1.5*pyrfig.get_figheight())
plt.show(pyrfig)