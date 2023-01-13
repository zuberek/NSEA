import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

def fonts(fontsize=10):
    plt.rc('font', size=fontsize)       # controls default text size
    plt.rc('axes', titlesize=fontsize)  # fontsize of the title
    plt.rc('axes', labelsize=fontsize)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=fontsize) # fontsize of the x tick labels
    plt.rc('ytick', labelsize=fontsize) # fontsize of the y tick labels
    plt.rc('legend', fontsize=fontsize) # fontsize of the legend


def axes(cols, axes=None, figure=None, rows=1, scale=6, figsize=None):
    # fonts(10*n_cols)
    if figsize is None:
        figsize=(scale*cols+cols,4*rows+rows)
    fig, axs = plt.subplots(ncols=cols, nrows=rows, figsize=figsize)
    if axes is not None:
        for i, ax in enumerate(axes):
            axs[i].set_title(ax)
    if figure is not None:
        fig.suptitle(figure)
        return fig, axs
    return axs 

def tab(subtitles, title=None, ncols=3, row_size=4, col_size=6):
    if isinstance(subtitles, str):
        subtitles = [subtitles]

    full_rows = len(subtitles)//ncols
    nrows = full_rows if len(subtitles)/ncols<=full_rows else full_rows+1
    figsize=(col_size*ncols, row_size*nrows)

    fig, axs = plt.subplots(ncols=ncols, nrows=nrows, figsize=figsize)
    axs = axs.flatten()

    for i, ax in enumerate(subtitles):
        axs[i].set_title(ax)

    if title is not None:
        fig.suptitle(title)
    return axs 


def row(subtitles, figure=None, scale=6, figsize=None):
    if isinstance(subtitles, str):
        subtitles = [subtitles]
    # fonts(10*n_cols)
    ncols=len(subtitles)
    if figsize is None:
        figsize=(scale*ncols,4)
    fig, axs = plt.subplots(ncols=ncols, nrows=1, figsize=figsize)

    if ncols==1: # if only one subfigure
        axs.set_title(subtitles[0])
    else:
        for i, ax in enumerate(subtitles):
            axs[i].set_title(ax)

    if figure is not None:
        fig.suptitle(figure)
    return axs 

def col(subtitles, figure=None, scale=4, figsize=None):
    if isinstance(subtitles, str):
        subtitles = [subtitles]
    # fonts(10*n_cols)
    nrows=len(subtitles)
    if figsize is None:
        figsize=(6,scale*nrows+nrows)
    fig, axs = plt.subplots(ncols=1, nrows=nrows, figsize=figsize)

    if nrows==1: # if only one subfigure
        axs.set_title(subtitles[0])
    else:
        for i, ax in enumerate(subtitles):
            axs[i].set_title(ax)

    if figure is not None:
        fig.suptitle(figure)
        return fig, axs
    return axs

def annotate(ax: plt.axis, xlabel=None, ylabel=None, title=None):
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)
    if title is not None:
        ax.set_xlabel(title)

    return ax

def save(ax, title, bbox=None):
    ax.get_figure().savefig(f'../../figures/{title}.png',bbox_inches=bbox)


def shape(data, dimensions):
    return pd.DataFrame(data.shape, index=dimensions, columns=['shape']).T