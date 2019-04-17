# Enter your code here. Read input from STDIN. Print output to STDOUT
import random
import math


class Road_Network:
    def __init__(self, x_max=10, y_max=10, z_max=10, x_min=0, y_min=0, z_min=0, acceptable_radius=2):
        self.node_dict = {}
        self.x_min = x_min
        self.y_min = y_min
        self.z_min = z_min
        self.x_max = x_max
        self.y_max = y_max
        self.z_max = z_max
        self.acceptable_radius = acceptable_radius

    def update_nodes(self, node_id, coords):
        if node_id not in self.node_dict:
            self.node_dict[node_id] = {
                'coords': coords,
                'neighbors': set()
            }

    def update_neighbors(self, node_id, neighbor_list):
        for neighbor in neighbor_list:
            self.node_dict[node_id]['neighbors'].add(neighbor)
            self.node_dict[neighbor]['neighbors'].add(node_id)

    def print_network(self):
        edge_list = []
        for node_id in sorted(self.node_dict.keys()):
            for axis in self.node_dict[node_id]['coords'][:-1]:
                print('{0:.2f}'.format(axis) + ',', end=' ')
            print('{0:.2f}'.format(self.node_dict[node_id]['coords'][-1]))

            for neighbor in sorted(self.node_dict[node_id]['neighbors']):
                if neighbor > node_id:
                    edge_list.append(str(node_id) + ', ' + str(neighbor))

        for edges in edge_list:
            print(edges)

    def generate_network(self, num_nodes, num_neighbors=None):
        for node_id in range(0, num_nodes):
            x = random.uniform(self.x_min, self.x_max)
            y = random.uniform(self.y_min, self.y_max)
            z = 0
            # z = random.uniform(self.z_min, self.z_max)
            self.update_nodes(node_id, (x, y, z))

        # node_set = set(self.node_dict.keys())

        # for node_id in sorted(node_set):
        #     node_set.remove(node_id)
        #     neighbor_list = list(random.sample(node_set, len(node_set)))[0:num_neighbors-1]
        #     self.update_neighbors(node_id, neighbor_list)
        #     node_set.add(node_id)

    def check_radius(self, node_A_coords, node_B_coords):
        node_AX = node_A_coords[0]
        node_AY = node_A_coords[1]

        node_BX = node_B_coords[0]
        node_BY = node_B_coords[1]

        radius = math.sqrt(math.pow((node_AX - nodeBX), 2) + math.pow((node_AY - nodeBY), 2))

        # if radius > self.acceptable_radius:
        # return True
        # else:
        # return False

    def connect_nearest_neighbor(self, node_ref):
        max_radius = math.sqrt(math.pow((self.x_max - self.x_min), 2) + math.pow((self.y_max - self.y_min), 2))

        nearest = None

        # for nodeA in self.node_dict:
        #     if nodeA not in nearest:
        #         nearest[nodeA] = None
        for nodeB in self.node_dict:
            nodeAX = self.node_dict[node_ref]['coords'][0]
            nodeBX = self.node_dict[nodeB]['coords'][0]
            nodeAY = self.node_dict[node_ref]['coords'][1]
            nodeBY = self.node_dict[nodeB]['coords'][1]
            temp_radius = math.sqrt(math.pow((nodeAX - nodeBX), 2) + math.pow((nodeAY - nodeBY), 2))

            if temp_radius < max_radius and temp_radius > 0:
                nearest = nodeB
                max_radius = temp_radius

        return nearest

    def assign_neighbor(self):
        for node_ref in self.node_dict.keys():
            neighbor = self.connect_nearest_neighbor(node_ref)
            self.node_dict[node_ref]['neighbors'].add(neighbor)
            self.node_dict[neighbor]['neighbors'].add(node_ref)


def main():
    # print('Test 1')
    # graph1 = Road_Network()

    # graph1.update_nodes(0, (2, 3.1, 1.2))
    # graph1.update_nodes(1, (3.5, 2.6, 10.1))
    # graph1.update_nodes(2, (4.1, 3.4, 7.44))

    # graph1.update_neighbors(0, [1])
    # graph1.update_neighbors(1, [2])

    # graph1.print_network()
    # print()

    # print('Test 2')
    # graph2 = Road_Network()
    # num_nodes = random.randint(5, 10)
    # num_neighbors = 3
    # graph2.generate_network(num_nodes, num_neighbors)

    # graph2.print_network()

    print('Test 3')
    graph3 = Road_Network()
    num_nodes = 100
    graph3.generate_network(num_nodes)
    graph3.assign_neighbor()

    graph3.print_network()


if __name__ == "__main__":
    main()