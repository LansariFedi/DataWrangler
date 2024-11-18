# DataWrangler

DataWrangler is a Python library for preprocessing data, including cleaning, encoding, and scaling. It is designed to simplify the data wrangling process for machine learning tasks.

## Installation

You can install DataWrangler using pip:

```sh
pip install datawrangler
```

## Usage

Importing the Library

```python
from datawrangler import DataWrangler
```

### Creating an Instance

```python
dw = DataWrangler()
```

### Cleaning Data

The `clean` method fills missing values in categorical columns with 'Missing' and in numerical columns with the mean of the column.

```python
cleaned_data = dw.clean(data)
```

### Encoding and Scaling Data

The `EncodeAndScale_fit` method encodes categorical columns using `LabelEncoder` and scales numerical columns using `StandardScaler`.

```python
encoded_scaled_data = dw.EncodeAndScale_fit(cleaned_data)
```

The `EncodeAndScale_transform` method transforms new data using the previously fitted encoders and scaler.

```python
new_encoded_scaled_data = dw.EncodeAndScale_transform(new_data)
```

### Example

```python
import pandas as pd
from datawrangler import DataWrangler

# Sample data
data = pd.DataFrame({
    'category': ['A', 'B', 'A', None],
    'value': [1.0, 2.5, None, 4.0]
})

# Create an instance of DataWrangler
dw = DataWrangler()

# Clean the data
cleaned_data = dw.clean(data)

# Encode and scale the data
encoded_scaled_data = dw.EncodeAndScale_fit(cleaned_data)

print(encoded_scaled_data)
```

## License

This project is licensed under the MIT License - see the [LICENSE]([https://github.com/yourusername/yourrepositoryname/blob/main/LICENSE](https://opensource.org/license/mit)) file for details.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Author

Lansari Fedi - lansarifedi7@gmail.com
