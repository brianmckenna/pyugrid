#!/usr/bin/env python

"""
DataSet object, used to hold data associated with a ugrid
"""

from __future__ import (absolute_import, division, print_function)

import numpy as np


class DataSet(object):
    """
    A class to hold the data associated with nodes, edges, etc.

    It holds an array of the data, as well as the attributes associated
     with that data (attributes get stored in the netcdf file)

    """
    def __init__(self, name, location='node', data=None, attributes=None):
        """
        create a data_set object
        :param name: the name of the data (depth, u_velocity, etc.)
        :type name: string

        :param location: the type of grid element: 'node', 'edge', or 'face'
        the data is assigned to

        :param data: the data
        :type data: 1-d numpy array, or something compatible (list, etc.)

        """
        self.name = name

        if location not in ['node', 'edge', 'face', 'boundary']:
            raise ValueError("location must be one of:"
                             "'node', 'edge', 'face', 'boundary'")
        # Must be 'node', 'edge', of 'face' (eventually 'volume').
        self.location = location

        if data is None:
            # Could be any data type.
            self._data = np.zeros((0,), dtype=np.float64)
        else:
            self._data = np.asarray(data)

        self.attributes = {} if attributes is None else attributes

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = np.asarray(data)

    @data.deleter
    def data(self):
        self._data = self._data = np.zeros((0,), dtype=np.float64)

    def __str__(self):
        return ("DataSet object: {0:s}, on the {1:s}s, and {2:d} data points\n"
                "Attributes: {3}".format(self.name, self.location,
                                         len(self.data), self.attributes))
