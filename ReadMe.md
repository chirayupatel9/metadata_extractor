
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
from materials.AFM.bandexcitation.h5 import H5
import json
from pprint import pprint

process_file = H5("path/to/file")
metadata = process_file.extract()

print(metadata)
pprint(metadata)  # Pretty Print likewise
print(json.dumps(metadata, indent=4))  # Print metadata in JSON format
```
### For xrdml file type

```python
from materials.Xray.panalytical.xrdml import XRDML
import json
from pprint import pprint

process_file = XRDML("path/to/file")
metadata = process_file.extract()

print(metadata)
pprint(metadata)  # Pretty Print likewise
print(json.dumps(metadata, indent=4))  # Print metadata in JSON format

```
### For dm4 file type

```python
from materials.EM.dm.dm4 import DM4
import json
from pprint import pprint

process_file = DM4("path/to/file")
metadata = process_file.extract()

print(metadata)
pprint(metadata)  # Pretty Print likewise
print(json.dumps(metadata, indent=4))  # Print metadata in JSON format
```
### For ibw file type

```python
from materials.AFM.oxfordAFM.ibw import IBW
import json
from pprint import pprint

process_file = IBW("path/to/file")
metadata = process_file.extract()

print(metadata)
pprint(metadata)  # Pretty Print likewise
print(json.dumps(metadata, indent=4))  # Print metadata in JSON format
```

## 