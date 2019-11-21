"""
The public interface to the read_structure_step SEAMM plugin
"""

from . import utils
from . import formats

def read(file_name, extension=None):
    """
    Calls the appropriate functions to parse the requested file.

    Parameters
    ----------
    file_name: str
        Name of the file

    extension: str, optional, default: None

    Returns
    -------
    dict
        A SEAMM structure with the structure information contained in the input files. 
    """

    if type(file_name) is not str:
        raise TypeError('read_structure_step: The file name must be a string, but a %s was given. ' % str(type(file_name)))

    if file_name == '':
        raise NameError('read_structure_step: The file name for the structure file was not specified.')

    if extension is None:
        try:
            extension = utils.guess_extension(file_name, use_file_name=True)

        except:
            extension = utils.guess_extension(file_name, use_file_name=False)

    else:
        extension = utils.sanitize_file_format(extension)

    if extension not in formats.registries.REGISTERED_READERS.keys():
        raise KeyError('read_structure_step: the file format %s was not recognized.' % extension)

    reader = formats.registries.REGISTERED_READERS[extension]
    
    return reader(file_name)
