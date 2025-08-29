import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_process(title, shrink=False, expand=False):
    fig, ax = plt.subplots(figsize=(3,3))
    
    # Draw coordinate axes
    ax.arrow(0,0,-1.2,0,head_width=0.1,head_length=0.1,fc='k',ec='k')
    ax.arrow(0,0, 1.2,0,head_width=0.1,head_length=0.1,fc='k',ec='k')
    ax.arrow(0,0,0,-1.2,head_width=0.1,head_length=0.1,fc='k',ec='k')
    ax.arrow(0,0,0, 1.2,head_width=0.1,head_length=0.1,fc='k',ec='k')

    # Draw squares to represent pixels
    outer = patches.Rectangle((-0.5,-0.5),1,1,fill=False,color="red",linewidth=3)
    ax.add_patch(outer)

    if shrink:
        inner = patches.Rectangle((-0.25,-0.25),0.5,0.5,fill=False,color="blue",linewidth=2)
        ax.add_patch(inner)
        ax.text(0,-1.4,"Downsampling",ha="center")
    elif expand:
        bigger = patches.Rectangle((-0.75,-0.75),1.5,1.5,fill=False,color="green",linewidth=2)
        ax.add_patch(bigger)
        ax.text(0,-1.4,"Upsampling",ha="center")
    else:
        ax.text(0,-1.4,title,ha="center")
    
    ax.set_xlim(-1.5,1.5)
    ax.set_ylim(-1.5,1.5)
    ax.axis("off")
    plt.title(title)
    plt.show()

# Draw diagrams
draw_process("Downsampling Example", shrink=True)
draw_process("Upsampling Example", expand=True)
