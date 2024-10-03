
# MetadataExtractor

## Overview
**MetadataExtractor** is a Python class designed to extract metadata from various file formats including:

- `.h5` (HDF5)
- `.xrdml` (XRDML XML-based)
- `.dm4` (DigitalMicrograph)
- `.ibw` (Igor Binary Wave)


## Installation of Dependencies

```bash
pip install -r requirements.txt
```

## Running the extractor

```python
from MetadataExtractor import MetadataExtractor
import json
from pprint import pprint

extract = MetadataExtractor("path/to/file")
metadata = extract.get_metadata()
print(metadata) 
pprint(metadata) # Pretty Print likewise
print(json.dumps(metadata, indent=4)) # Print metadata in JSON format
```