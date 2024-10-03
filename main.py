import json
import numpy as np
import h5py
import xml.etree.ElementTree as ET
import hyperspy.api as hs
from igor2 import binarywave
from pprint import pprint

# JSON Encoder for numpy types and complex numbers
class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        # Handle numpy integer types
        if isinstance(obj, np.integer):
            return int(obj)
        # Handle numpy floating-point types
        elif isinstance(obj, np.floating):
            return float(obj)
        # Handle numpy arrays
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        # Handle bytes by decoding them to UTF-8 strings
        elif isinstance(obj, bytes):
            return obj.decode("utf-8")
        # Handle complex numbers by returning a list of [real, imaginary]
        elif isinstance(obj, complex):
            return [obj.real, obj.imag]
        # Fallback to the default JSON encoding for other types
        else:
            return super(MyEncoder, self).default(obj)


class MetadataExtractor:
    """
    Class to extract metadata from various file formats (.h5, .xrdml, .dm4, .ibw).
    It supports length checks on the values to filter out data based on size.
    """

    def __init__(self, file_name):
        """
        Constructor that initializes the extractor with the file name.
        :param file_name: Name of the file from which metadata will be extracted.
        """
        self.file_name = file_name

    # Function to read .h5 (HDF5) files with the length check
    def read_h5_file(self):
        """
        Reads an HDF5 (.h5) file and extracts metadata while skipping values with length > 10.
        :return: A dictionary containing the metadata.
        """
        def extract_h5_data(name, obj):
            # Extract attributes where the length of the value is <= 10
            attrs = {k: v for k, v in obj.attrs.items() if len(str(v)) <= 10}
            return {name: attrs}

        with h5py.File(self.file_name, 'r') as f:
            metadata = {}
            # Visit all items in the HDF5 file and collect metadata
            f.visititems(lambda name, obj: metadata.update(extract_h5_data(name, obj)))
        return metadata

    # Function to read .xrdml (XRDML) files with the length check
    def read_xrdml_file(self):
        """
        Reads an XRDML (.xrdml) XML-based file and extracts metadata while skipping values with length > 10.
        :return: A dictionary containing the metadata.
        """
        tree = ET.parse(self.file_name)
        root = tree.getroot()

        # Extract metadata from XML elements, skipping those with value length > 10
        metadata = {}
        for elem in root.iter():
            if elem.text and len(elem.text) <= 10:
                metadata[elem.tag] = elem.text
        return metadata

    # Function to read .dm4 (DigitalMicrograph) files with the length check
    def read_dm4_file(self):
        """
        Reads a DigitalMicrograph (.dm4) file and extracts metadata while skipping values with length > 10.
        :return: A dictionary containing the metadata.
        """
        s = hs.load(self.file_name)  # Load the .dm4 file using HyperSpy
        metadata = s.metadata.as_dictionary()  # Extract metadata as a dictionary

        # Filter out metadata entries with value lengths > 10
        filtered_metadata = {k: v for k, v in metadata.items() if len(str(v)) <= 10}
        return filtered_metadata

    # Helper function to extract parameters from wave data
    def _read_parms(self, wave):
        """
        Helper function to extract parameters from the wave data in an .ibw file, skipping values > 10 characters.
        :param wave: The wave data extracted from the .ibw file.
        :return: A dictionary containing the metadata.
        """
        parm_dict = {}
        parm_string = wave['note']
        # Decode the byte-string if necessary
        if isinstance(parm_string, bytes):
            try:
                parm_string = parm_string.decode("utf-8")
            except UnicodeDecodeError:
                parm_string = parm_string.decode("ISO-8859-1")  # Fallback for older encoding

        parm_string = parm_string.rstrip("\r").replace(".", "_")
        parm_list = parm_string.split("\r")

        for pair_string in parm_list:
            temp = pair_string.split(":")
            if len(temp) == 2:
                temp = [item.strip() for item in temp]
                try:
                    num = float(temp[1])
                    # Skip the value if it is infinity or too long
                    if np.isinf(num):
                        continue
                    if len(str(num)) <= 10:
                        parm_dict[temp[0]] = int(num) if num == int(num) else num
                except ValueError:
                    if len(temp[1]) <= 10:
                        parm_dict[temp[0]] = temp[1]

        return parm_dict

    # Function to read .ibw (Igor Binary Wave) files with the length check
    def read_ibw_file(self):
        """
        Reads an Igor Binary Wave (.ibw) file and extracts metadata while skipping values with length > 10.
        :return: A dictionary containing the metadata.
        """
        with open(self.file_name, "rb") as f:
            ibw_obj = binarywave.load(f)  # Load the .ibw file using igor2

        wave = ibw_obj['wave']  # Extract wave data

        # Extract parameters from the wave
        metadata = self._read_parms(wave)
        return metadata

    # Unified function to handle different file types
    def get_metadata(self):
        """
        Determines the file type based on the file extension and calls the appropriate method to extract metadata.
        :return: A dictionary containing the metadata.
        """
        if self.file_name.endswith('.h5'):
            return self.read_h5_file()
        elif self.file_name.endswith('.xrdml'):
            return self.read_xrdml_file()
        elif self.file_name.endswith('.dm4'):
            return self.read_dm4_file()
        elif self.file_name.endswith('.ibw'):
            return self.read_ibw_file()
        else:
            raise ValueError("Unsupported file format")
