#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `utils` module."""

import pytest  # noqa: F401
import read_structure_step  # noqa: F401
from . import build_filenames
import json

@pytest.mark.parametrize("structure", ["3TR_model.mol2", "3TR_model.xyz", "3TR_model.pdb", "3TR_model.sdf"])
def test_format(structure):

    file_name = build_filenames.build_data_filename(structure) 
    parsed_file= read_structure_step.read(file_name)

    reference_name = build_filenames.build_data_filename("3TR_model.json")

    with open(reference_name, 'r') as json_file:
        reference = json.load(json_file)

    assert len(parsed_file["atoms"]["elements"]) == 10
    assert all(atom in ["N", "N", "N", "N", "C", "C", "H", "H", "H", "H"] for atom in parsed_file["atoms"]["elements"])
    assert len(parsed_file["atoms"]["coordinates"]) == 10
    assert all(len(point) == 3 for point in parsed_file["atoms"]["coordinates"])
    assert len(parsed_file["bonds"]) == 10
    assert any(set(bond) == set((2, 1, 'single')) for bond in parsed_file["bonds"])
    assert any(set(bond) == set((5, 1, 'single')) for bond in parsed_file["bonds"])
    assert any(set(bond) == set((7, 1, 'single')) for bond in parsed_file["bonds"])
    assert any(set(bond) == set((2, 3, 'double')) for bond in parsed_file["bonds"])
    assert any(set(bond) == set((3, 4, 'single')) for bond in parsed_file["bonds"])
    assert any(set(bond) == set((3, 6, 'single')) for bond in parsed_file["bonds"])
    assert any(set(bond) == set((5, 8, 'single')) for bond in parsed_file["bonds"])
    assert any(set(bond) == set((6, 9, 'single')) for bond in parsed_file["bonds"])
    assert any(set(bond) == set((6, 10, 'single')) for bond in parsed_file["bonds"])
