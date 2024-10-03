
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

### For h5 File type

```python
from ex_h5 import H5MetadataExtractor
import json
from pprint import pprint

process_file = H5MetadataExtractor("path/to/file")
metadata = process_file.extract()

print(metadata)
pprint(metadata)  # Pretty Print likewise
print(json.dumps(metadata, indent=4))  # Print metadata in JSON format
```
### For xrdml file type

```python
from ex_xrdml import XRDMLMetadataExtractor
import json
from pprint import pprint

process_file = XRDMLMetadataExtractor("path/to/file")
metadata = process_file.extract()

print(metadata)
pprint(metadata)  # Pretty Print likewise
print(json.dumps(metadata, indent=4))  # Print metadata in JSON format

```
### For dm4 file type

```python
from ex_dm4 import DM4MetadataExtractor
import json
from pprint import pprint

process_file = DM4MetadataExtractor("path/to/file")
metadata = process_file.extract()

print(metadata)
pprint(metadata)  # Pretty Print likewise
print(json.dumps(metadata, indent=4))  # Print metadata in JSON format
```
### For ibw file type

```python
from ex_ibw import IBWMetadataExtractor
import json
from pprint import pprint

process_file = IBWMetadataExtractor("path/to/file")
metadata = process_file.extract()

print(metadata)
pprint(metadata)  # Pretty Print likewise
print(json.dumps(metadata, indent=4))  # Print metadata in JSON format
```

## 