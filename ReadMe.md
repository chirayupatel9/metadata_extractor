
## Installation

```bash
pip install -r requirements.txt
```

## Running the extractor

```python
extract = MetadataExtractor("path/to/file")
metadata = extract.get_metadata()
print(metadata) 
pprint(metadata) # Pretty Print likewise 
```