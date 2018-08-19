# File for the TTPhysics system

class System():
    def __init__(self):
        '''Initialize empty physics system.'''
        self.nodes = []
        self.springs = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_node_collection(self, nodecollection):
        for node in nodecollection:
            self.nodes.append(node)

    def add_spring(self, spring):
        self.springs.append(spring)

    def add_spring_collection(self, springcollection):
        for spring in springcollection:
            self.springs.append(spring)

    def update(self, timestepinmilliseconds):
        #try:
            tsinseconds = timestepinmilliseconds / 1000
            for node in self.nodes:
                node.acceleration.set_dimensions(0,0)
            self.apply_hookes_law(tsinseconds)
            self.update_nodes(tsinseconds)
        #except:
        #    print("Error during physics system update")

    def apply_hookes_law(self, timestep, damping = True):
        print("Springs: ", str(self.springs))
        for spring in self.springs:
            try:
                d = spring.direction()
                displacement = d.magnitude() - spring.length
                unit = d.normalize()

                # Following line affects the spring's B node
                spring.b.apply_force(unit * (-spring.stiffness * displacement))
                if damping:
                    spring.b.apply_force(spring.b.velocity * -spring.damping)
            except Exception as err:
                raise RuntimeError("Error during spring update: ", str(err))
            except:
                print("Unidentified error during spring update")


    # Coulomb's law? Isn't this a bit slow?
    def apply_repulsion(self, timestep):
        for node in self.nodes:
            # Repulsion: smaller distance = larger repulsion between nodes
            pass

    def update_nodes(self, timestep):
        print("Nodes: ", str(self.nodes))
        for node in self.nodes:
            try:
                node.update_properties(timestep)
                node.update_wrapper_position()
            except Exception as err:
                raise RuntimeError("Error during node update: ", str(err))
            except:
                print("Unidentified error during node update")