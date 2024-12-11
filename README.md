# PyBandiger

PyBandiger is a Python library for preprocessing data, including cleaning, encoding, scaling, and transforming date columns. It is designed to simplify the data wrangling process for machine learning tasks.

## Installation

You can install PyBandiger using pip:

```sh
pip install pybandiger
```

## Usage

### Importing the Library

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

**Parameters:**

- `data` (pd.DataFrame): The input DataFrame to be cleaned.

### Encoding and Scaling Data

The `EncodeAndScale_fit` method encodes categorical columns using `LabelEncoder` and scales numerical columns using `StandardScaler`.

```python
encoded_scaled_data = pb.EncodeAndScale_fit(cleaned_data)
```

**Parameters:**

- `data` (pd.DataFrame): The input DataFrame to be encoded and scaled.

The `EncodeAndScale_transform` method transforms new data using the previously fitted encoders and scaler.

```python
new_encoded_scaled_data = pb.EncodeAndScale_transform(new_data)
```

**Parameters:**

- `data` (pd.DataFrame): The new DataFrame to be transformed using the fitted encoders and scaler.

### Transforming Date Columns

The `time_transform` method extracts year, month, day, and day of the week from a date column and drops the original date column.

```python
transformed_data = pb.time_transform(data, date_col='date')
```

**Parameters:**

- `data` (pd.DataFrame): The input DataFrame containing the date column.
- `date_col` (str): The name of the date column to be transformed. Default is 'date'.
- `prefix` (str): The prefix to add to the new date-related columns. Default is ''.

### Example

```python
import pandas as pd
from pybandiger import PyBandiger

# Sample data
data = pd.DataFrame({
    'category': ['A', 'B', 'A', None],
    'value': [1.0, 2.5, None, 4.0],
    'date': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01']
})

# Create an instance of PyBandiger
pb = PyBandiger()

# Clean the data
cleaned_data = pb.clean(data)

# Encode and scale the data
encoded_scaled_data = pb.EncodeAndScale_fit(cleaned_data)

# Transform date columns
transformed_data = pb.time_transform(cleaned_data)

print(encoded_scaled_data)
print(transformed_data)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Author

Lansari Fedi - lansarifedi7@gmail.com
