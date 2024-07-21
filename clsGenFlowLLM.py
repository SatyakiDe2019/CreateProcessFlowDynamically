###############################################################
####                                                       ####
#### Written By: Satyaki De                                ####
#### Written Date:  17-Jul-2024                            ####
#### Modified Date: 21-Jul-2024                            ####
####                                                       ####
#### Objective: This script will publish flow diagram      ####
#### with stunning visual pallatte based on the input      ####
#### topics provided from the command prompt.              ####
####                                                       ####
###############################################################

from clsConfigClient import clsConfigClient as cf
import clsL as log
import logging
from datetime import datetime, timedelta
import random
import time

import clsTemplate as ct

import os
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from openai import OpenAI
from textwrap import wrap
import numpy as np
import math

# Disabling Warning
def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

########################################################
################    Global Area   ######################
########################################################

fileDBPath = cf.conf['DB_PATH']

var1 = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print('*' *60)
DInd = cf.conf['DEBUG_IND']

templateVal_1 = ct.templateVal_1
templateVal_2 = ct.templateVal_2
templateVal_3 = ct.templateVal_3
templateVal_4 = ct.templateVal_4
templateVal_5 = ct.templateVal_5

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Initialize the OpenAI client
client = OpenAI(api_key=cf.conf['OPEN_AI_KEY'])
########################################################
################  End Of Global Area   #################
########################################################

class clsGenFlowLLM:
    def __init__(self):
        self.modelName = cf.conf['MODEL_NAME']
        self.ouputPath = str(cf.conf['OUTPUT_PATH'])

    def summarizeToFourWords(self, sentence):
        try:
            modelName = self.modelName
            content_3 = templateVal_4
            content_4 = f"" + templateVal_5 + str(sentence)

            response = client.chat.completions.create(
                model=modelName,
                messages=[
                    {"role": "system", "content": content_3},
                    {"role": "user", "content": content_4}
                ],
                n=1,
                temperature=0.1,
            )

            summary = response.choices[0].message.content.strip().split('\n')

            # If summary is a list, join it into a string
            if isinstance(summary, list):
                summary = ' '.join(summary)

            summary = ' '.join(summary.replace('.', '').split()[:4])

            return summary

        except Exception as e:
            return f"Error: {str(e)}"

    def generateFlowchart(self, srcDesc, debugInd, varVa):
        try:
            modelName = self.modelName
            ouputPath = self.ouputPath

            content_1 = templateVal_1
            content_2 = templateVal_2 + " " + srcDesc + ". " + templateVal_3

            # Use OpenAI to generate flowchart steps
            response = client.chat.completions.create(
                model=modelName,
                messages=[
                    {"role": "system", "content": content_1},
                    {"role": "user", "content": content_2}
                ],
                temperature=0.7,
            )

            steps = response.choices[0].message.content.strip().split('\n')

            # Create a new directed graph
            G = nx.DiGraph()

            # Add nodes and edges based on the generated steps
            for i, step in enumerate(steps):
                step_parts = step.split(': ', 1)
                if len(step_parts) == 2:
                    step_number, step_description = step_parts
                    G.add_node(i, description=step_description)
                    if i > 0:
                        G.add_edge(i-1, i)

            # Calculate layout
            num_nodes = len(G.nodes())
            rows = math.ceil(math.sqrt(num_nodes))
            cols = math.ceil(num_nodes / rows)

            # Calculate figure size
            fig_width = max(12, cols * 4)
            fig_height = max(8, rows * 3)

            # Create the plot
            fig, ax = plt.subplots(figsize=(fig_width, fig_height))

            # Generate a list of soft, pleasing colors
            colors = plt.cm.Pastel1(np.linspace(0, 1, num_nodes))

            # Calculate positions for nodes
            pos = {}
            for i in range(num_nodes):
                row = i // cols
                col = i % cols
                x = col / (cols - 1) if cols > 1 else 0.5
                y = 1 - (row / (rows - 1) if rows > 1 else 0.5)
                pos[i] = (x, y)

            # Draw arrows
            for edge in G.edges():
                start = pos[edge[0]]
                end = pos[edge[1]]
                ax.arrow(start[0], start[1], end[0]-start[0], end[1]-start[1],
                         head_width=0.03, head_length=0.05, fc='gray', ec='gray', linewidth=2)

            # Draw nodes and labels
            for i, (node, (x, y)) in enumerate(pos.items()):
                srcDesc = G.nodes[node]['description']
                wrapped_text = '\n'.join(wrap(srcDesc, width=15))

                circle = Circle((x, y), radius=0.08, fill=True, facecolor=colors[i], edgecolor='black', zorder=2)
                ax.add_patch(circle)

                ax.text(x, y, wrapped_text, ha='center', va='center', wrap=True, fontsize=8, zorder=3)

                if i == 0:
                    ax.text(x, y+0.11, "Start", ha='center', va='bottom', fontweight='bold')
                elif i == num_nodes - 1:
                    ax.text(x, y-0.11, "End", ha='center', va='top', fontweight='bold')

            # Set plot limits and remove axes
            ax.set_xlim(-0.1, 1.1)
            ax.set_ylim(-0.1, 1.1)
            ax.axis('off')

            # Getting the Short Description of the Image
            resDesc = self.summarizeToFourWords(srcDesc)

            plt.title(f"Flowchart: {resDesc}")
            plt.tight_layout()

            var = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            filename = f"flowchart_{resDesc.replace(' ', '_')}_{var}.png"
            print('Filename:')
            print(filename)
            plt.savefig(ouputPath+filename, format='png', dpi=300, bbox_inches='tight')
            plt.close()
            print(f"Flowchart generated as '{filename}'")

            return 0

        except Exception as e:
            x = str(e)
            print(x)

            logging.info(x)

            return 1
