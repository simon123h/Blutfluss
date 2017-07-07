from compartment import Compartment


# a terminal compartment, such as a set of muscle arteries
class TerminalVessel(Compartment):

    # constructor
    def __init__(self, R=0., L=0., C=0., P1=0., Q2=0., P2=0., Q1=0.):
        # physical inital values
        R = 10000000.             # viscosity
        L = 1.0                 # inertia
        C = 0.4 / R             # compliance
        Q1 = 0.0003                 # boundary Q  0.3 mm/s
        Q2 = 0.0003                 # initial Q2
        P1 = 2500.              # initial P1
        P2 = 2500.              # boundary P
        # call parent constructor with default values
        super(TerminalVessel, self).__init__(R=R, L=L, C=C, P1=P1, Q2=Q2, P2=P2, Q1=Q1)
        self.y = [P1]
        self.r.set_initial_value(self.y, Compartment.t0)

    def setInitial(self, P1, Q2):
        self.y = [P1]
        self.r.set_initial_value(self.y, Compartment.t0)

    # output flow is determined by Ohm's law (reduced form of the rhs)
    @property
    def Q2(self):
        return (self.P1 - self.P2) / self.R

    # the rhs of terminal vessel, reduced form of the Compartment rhs
    def rhs(self, t, y):
        return [(self.Q1 - self.Q2) / self.C]
