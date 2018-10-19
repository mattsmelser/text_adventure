from vertex import Vertex

class Graph:
  def __init__(self):
    self.graph_dict = {}

  def add_vertex(self, node):
    self.graph_dict[node.value] = node

  def add_edge(self, from_node, to_node):
    self.graph_dict[from_node.value].add_edge(to_node.value)
    self.graph_dict[to_node.value].add_edge(from_node.value)

  def explore(self):
    print("""\n\nWelcome to Sanctuary...\n
    You have arrived in The Rogue Encampment and are greeted with scowled looks from the towns folk.
    Perhaps you should speak with the townspeople before heading out on your adventure.""")
    #FILL IN EXPLORE METHOD BELOW
    current_location = 'Rogue Encampment'
    path_total = 0
    print("\nYou are currently in The {0}\n".format(current_location))
    while current_location is not 'Catacombs Level 4':
      node = self.graph_dict[current_location]
      for connected_room, weight in node.edges.items():
        key = connected_room[0]
        print("enter {0} for {1}".format(key, connected_room))
      valid_choices = [room[:1] for room in node.edges.keys()]
      choice = input("\nWhere would you want to go now? ")
      if choice not in valid_choices:
        print("please select from these choices: {0}".format(valid_choices))
      else:
        for room in node.edges.keys():
          if room.startswith(choice):
            current_location = room
            path_total += node.edges[room]
        print("\n*** You have chosen: {0} ***\n".format(current_location))
    print("You successfully defeated Andariel and completed Act 1.")
    
        
          
      
    #return self.graph_dict[current_room]
    
  
  """def print_map(self):
    print("\nMAP LAYOUT\n")
    for node_key in self.graph_dict:
      print("{0} connected to...".format(node_key))
      node = self.graph_dict[node_key]
      print("")
    print("")"""

def build_graph():
  graph = Graph()
  
  
  # MAKE LOCATIONS INTO VERTICES BELOW...
  rogue_encampment = Vertex("Rogue Encampment")
  blood_moor = Vertex("Blood Moor")
  den_of_evil = Vertex("Den Of Evil")
  cold_plains = Vertex("Cold Plains")
  cave_1 = Vertex("Cave Level 1")
  cave_2 = Vertex("Cave Level 2")
  burial_grounds = Vertex("Burial Grounds")
  crypt = Vertex("Crypt")
  mausoleum = Vertex("Mausoleum")
  stony_field = Vertex("Stony Field")
  tristram = Vertex("Tristram")
  underground_passage_1 = Vertex("Underground Passage Level 1")
  underground_passage_2 = Vertex("Underground Passage Level 2")
  dark_wood = Vertex("Dark Wood")
  black_marsh = Vertex("Black Marsh")
  tower_1 = Vertex("Forgotten Tower Level 1")
  tower_2 = Vertex("Forgotten Tower Level 2")
  tower_3 = Vertex("Forgotten Tower Level 3")
  tower_4 = Vertex("Forgotten Tower Level 4")
  tower_5 = Vertex("Forgotten Tower Level 5")
  tamoe_highland = Vertex("Tamoe Highland")
  monastary_gate = Vertex("Monastary Gate")
  outer_cloister = Vertex("Outer Cloister")
  barracks = Vertex("Barracks")
  jail_1 = Vertex("Jail Level 1")
  jail_2 = Vertex("Jail Level 2")
  jail_3 = Vertex("Jail Level 3")
  inner_cloister = Vertex("Inner Cloister")
  cathedral = Vertex("Cathedral")
  catacombs_1 = Vertex("Catacombs Level 1")
  catacombs_2 = Vertex("Catacombs Level 2")
  catacombs_3 = Vertex("Catacombs Level 3")
  catacombs_4 = Vertex("Catacombs Level 4")





  # ADD ROOMS TO GRAPH BELOW...
  graph.add_vertex(rogue_encampment)
  graph.add_vertex(blood_moor)
  graph.add_vertex(den_of_evil)
  graph.add_vertex(cold_plains)
  graph.add_vertex(cave_1)
  graph.add_vertex(cave_2)
  graph.add_vertex(burial_grounds)
  graph.add_vertex(crypt)
  graph.add_vertex(mausoleum)
  graph.add_vertex(stony_field)
  graph.add_vertex(tristram)
  graph.add_vertex(underground_passage_1)
  graph.add_vertex(underground_passage_2)
  graph.add_vertex(dark_wood)
  graph.add_vertex(black_marsh)
  graph.add_vertex(tower_1)
  graph.add_vertex(tower_2)
  graph.add_vertex(tower_3)
  graph.add_vertex(tower_4)
  graph.add_vertex(tower_5)
  graph.add_vertex(tamoe_highland)
  graph.add_vertex(monastary_gate)
  graph.add_vertex(outer_cloister)
  graph.add_vertex(barracks)
  graph.add_vertex(jail_1)
  graph.add_vertex(jail_2)
  graph.add_vertex(jail_3)
  graph.add_vertex(inner_cloister)
  graph.add_vertex(cathedral)
  graph.add_vertex(catacombs_1)
  graph.add_vertex(catacombs_2)
  graph.add_vertex(catacombs_3)
  graph.add_vertex(catacombs_4)




  # ADD EDGES BETWEEN ROOMS BELOW...
  graph.add_edge(rogue_encampment, blood_moor)
  graph.add_edge(blood_moor, den_of_evil)
  graph.add_edge(blood_moor, cold_plains)
  graph.add_edge(cold_plains, cave_1)
  graph.add_edge(cave_1, cave_2)
  graph.add_edge(cold_plains, burial_grounds)
  graph.add_edge(burial_grounds, crypt)
  graph.add_edge(burial_grounds, mausoleum)
  graph.add_edge(cold_plains, stony_field)
  graph.add_edge(stony_field, tristram)
  graph.add_edge(stony_field, underground_passage_1)
  graph.add_edge(underground_passage_1, underground_passage_2)
  graph.add_edge(underground_passage_1, dark_wood)
  graph.add_edge(dark_wood, black_marsh)
  graph.add_edge(black_marsh, tower_1)
  graph.add_edge(tower_1, tower_2)
  graph.add_edge(tower_2, tower_3)
  graph.add_edge(tower_3, tower_4)
  graph.add_edge(tower_4, tower_5)
  graph.add_edge(black_marsh, tamoe_highland)
  graph.add_edge(tamoe_highland, monastary_gate)
  graph.add_edge(monastary_gate, outer_cloister)
  graph.add_edge(outer_cloister, barracks)
  graph.add_edge(barracks, jail_1)
  graph.add_edge(jail_1, jail_2)
  graph.add_edge(jail_2, jail_3)
  graph.add_edge(jail_3, inner_cloister)
  graph.add_edge(inner_cloister, cathedral)
  graph.add_edge(cathedral, catacombs_1)
  graph.add_edge(catacombs_1, catacombs_2)
  graph.add_edge(catacombs_2, catacombs_3)
  graph.add_edge(catacombs_3, catacombs_4)


  
  

  # DON'T CHANGE THIS CODE
  #graph.print_map()
  return graph
