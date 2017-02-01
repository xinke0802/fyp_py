import collections

import matplotlib.pyplot as plt
import networkx as nx


class GraphVizUtils:
  def displayGraphDegreeDist(self, G):
    # https://networkx.github.io/documentation/development/examples/drawing/degree_histogram.html

    degree_sequence = sorted(nx.degree(G).values(), reverse=True)  # degree sequence

    # print "Degree sequence", degree_sequence
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())

    fig, ax = plt.subplots()
    plt.bar(deg, cnt, width=0.80, color='b')

    plt.title("Degree Histogram")
    plt.ylabel("Count")
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.4 for d in deg])
    ax.set_xticklabels(deg)

    plt.show()
