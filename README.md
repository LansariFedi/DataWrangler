# PyBandiger

PyBandiger is a Python library for preprocessing data, including cleaning, encoding, and scaling. It is designed to simplify the data wrangling process for machine learning tasks.

## Installation

You can install PyBandiger using pip:

```sh
pip install pybandiger
```

## Usage

Importing the Library

```python
from pybandiger import PyBandiger
```

### Creating an Instance

```python
pb = PyBandiger()
```

### Cleaning Data

The `clean` method fills missing values in categorical columns with 'Missing' and in numerical columns with the mean of the column.

```python
cleaned_data = pb.clean(data)
```

### Encoding and Scaling Data

The `EncodeAndScale_fit` method encodes categorical columns using `LabelEncoder` and scales numerical columns using `StandardScaler`.

```python
encoded_scaled_data = pb.EncodeAndScale_fit(cleaned_data)
```

The `EncodeAndScale_transform` method transforms new data using the previously fitted encoders and scaler.

```python
new_encoded_scaled_data = pb.EncodeAndScale_transform(new_data)
```

### Example

```python
import pandas as pd
from pybandiger import PyBandiger

# Sample data
data = pd.DataFrame({
    'category': ['A', 'B', 'A', None],
    'value': [1.0, 2.5, None, 4.0]
})

# Create an instance of PyBandiger
pb = PyBandiger()

# Clean the data
cleaned_data = pb.clean(data)

# Encode and scale the data
encoded_scaled_data = pb.EncodeAndScale_fit(cleaned_data)

print(encoded_scaled_data)
```

## License

This project is licensed under the MIT License - see the <a href="https://opensource.org/license/mit" target="_blank">LICENSE</a>
file for details.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Author

Lansari Fedi - lansarifedi7@gmail.com
