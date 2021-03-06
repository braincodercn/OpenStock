import graphviz

from graphviz import Digraph
from absl import app
from absl import flags
from absl import logging

FLAGS = flags.FLAGS

def make_graph():
    g = Digraph("Roadmap_of_Task_based_Framework")
    g.node('System')
    g.node('Data Sources')
    g.node('Manager')
    g.node('App Layer')
    g.view()
    
def main(argv):
    del argv
    make_graph()

if __name__ == '__main__':
    app.run(main)

