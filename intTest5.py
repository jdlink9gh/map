import random
import math


class RoadNetwork:
    def __init__(self, x_max=10, y_max=10, z_max=10, x_min=0, y_min=0, z_min=0, acceptable_radius=2):
        self.node_dict = {}
        self.x_min = x_min
        self.y_min = y_min
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

    def generate_network(self, num_nodes):
        for node_id in range(0, num_nodes):
            x = random.uniform(self.x_min, self.x_max)
            y = random.uniform(self.y_min, self.y_max)
            z = 0
            # z = random.uniform(self.z_min, self.z_max)
            self.update_nodes(node_id, (x, y, z))

    # def check_radius(self, node_A_coords, node_B_coords):
    #     node_AX = node_A_coords[0]
    #     node_AY = node_A_coords[1]
    #
    #     node_BX = node_B_coords[0]
    #     node_BY = node_B_coords[1]
    #
    #     radius = math.sqrt(math.pow((node_AX - nodeBX), 2) + math.pow((node_AY - nodeBY), 2))

    def connect_nearest_neighbor(self, node_ref):
        max_radius = math.sqrt(math.pow((self.x_max - self.x_min), 2) + math.pow((self.y_max - self.y_min), 2))

        nearest = None

        for nodeB in self.node_dict:
            node_ax = self.node_dict[node_ref]['coords'][0]
            node_bx = self.node_dict[nodeB]['coords'][0]
            node_ay = self.node_dict[node_ref]['coords'][1]
            node_by = self.node_dict[nodeB]['coords'][1]
            temp_radius = math.sqrt(math.pow((node_ax - node_bx), 2) + math.pow((node_ay - node_by), 2))

            if max_radius > temp_radius > 0:
                nearest = nodeB
                max_radius = temp_radius

        return nearest

    def assign_neighbor(self):
        for node_ref in self.node_dict.keys():
            neighbor = self.connect_nearest_neighbor(node_ref)
            self.node_dict[node_ref]['neighbors'].add(neighbor)
            self.node_dict[neighbor]['neighbors'].add(node_ref)


def main():

    print('Test 3')
    graph3 = RoadNetwork()
    num_nodes = 100
    graph3.generate_network(num_nodes)
    graph3.assign_neighbor()

    graph3.print_network()


if __name__ == "__main__":
    main()
