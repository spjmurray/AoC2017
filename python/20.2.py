#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# To simplify the problem further, the GPU would like to remove any particles
# that collide. Particles collide if their positions ever exactly match.
# Because particles are updated simultaneously, more than two particles can
# collide at the same time and place. Once particles collide, they are removed
# and cannot collide with anything else after that tick.
#
# For example:
#
# p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>    
# p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
# p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>    (0)   (1)   (2)            (3)
# p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>
#
# p=<-3,0,0>, v=< 3,0,0>, a=< 0,0,0>    
# p=<-2,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
# p=<-1,0,0>, v=< 1,0,0>, a=< 0,0,0>             (0)(1)(2)      (3)   
# p=< 2,0,0>, v=<-1,0,0>, a=< 0,0,0>
#
# p=< 0,0,0>, v=< 3,0,0>, a=< 0,0,0>    
# p=< 0,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
# p=< 0,0,0>, v=< 1,0,0>, a=< 0,0,0>                       X (3)      
# p=< 1,0,0>, v=<-1,0,0>, a=< 0,0,0>
#
# ------destroyed by collision------    
# ------destroyed by collision------    -6 -5 -4 -3 -2 -1  0  1  2  3
# ------destroyed by collision------                      (3)         
# p=< 0,0,0>, v=<-1,0,0>, a=< 0,0,0>
#
# In this example, particles 0, 1, and 2 are simultaneously destroyed at the
# time and place marked X. On the next tick, particle 3 passes through
# unharmed.
#
# How many particles are left after all collisions are resolved?

import collections


def parse_vector(value):
    _, vec = value.split('=')
    return [int(x) for x in vec[1:-1].split(',')]


class Particle(object):
    def __init__(self, config):
        tp, tv, ta = config.strip().split(', ')
        self.p = parse_vector(tp)
        self.v = parse_vector(tv)
        self.a = parse_vector(ta)

    @property
    def manhattan(self):
        return abs(self.p[0]) + abs(self.p[1]) + abs(self.p[2])

    def animate(self):
        for i in xrange(0, 3):
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]


def main():
    # Load in the particle data
    particles = []
    for config in open('20.in'):
        particles.append(Particle(config))

    # Simulate for an arbitrary number of steps
    for _ in xrange(0, 1000):
        # Record the position of each particle at each step
        positions = []
        for particle in particles:
            particle.animate()
            positions.append(tuple(particle.p))
        # Count up based on position ...
        counter = collections.Counter(positions)
        # Select the coordinates of all collisions ...
        collisions = [list(pos) for pos, count in counter.items() if count > 1]
        # Finally update the particle list to include all particles whose
        # postion is not in our list of collisions
        particles = [part for part in particles if part.p not in collisions]

    print len(particles)
                        

if __name__ == '__main__':
    main()

# vi: ts=4 et:
