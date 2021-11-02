# -*- coding: utf-8 -*-

from particle import Particle, data


def test_load_particle_table(benchmark):
    benchmark(Particle.load_table, data.basepath / "particle2018.csv")


def test_load_nuclei_append(benchmark):
    benchmark(Particle.load_table, data.basepath / "nuclei2020.csv", append=True)


def test_from_pdgid(benchmark):
    Particle.all()

    benchmark(Particle.from_pdgid, 311)
