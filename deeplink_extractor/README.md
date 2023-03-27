# Deeplink Extractor

This tool is designed to extract all deeplinks from an AndroidManifest.xml file with just one click.

## Installation

1. Clone this repository.
2. Install the required dependencies by running `pip install -r requirements`.

## Usage

1. Navigate to the root directory of this project.
2. Run `python deeplink_extractor.py path/to/AndroidManifest.xml`.
3. The tool will output all deeplinks found in the specified AndroidManifest.xml file.

## Example

```
python deeplink_extractor.py app/src/main/AndroidManifest.xml
```

This will output all deeplinks found in the `AndroidManifest.xml` file located in the `app/src/main` directory.