from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':

    output_file('simple_plot.html')
    fig = figure()

    total_val = int(input('How many values do you want to plot?'))
    x_val = list(range(total_val))
    
    y_val = []
    for i in x_val:
    
        val = int(input(f'y value for {i} '))
        y_val.append(val)

    fig.line(x_val, y_val, line_width=2)
    show(fig)