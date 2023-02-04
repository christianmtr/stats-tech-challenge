# DataCapture

DataCapture is a class that implements a system to capture and process data. It allows adding new values, building statistics, and providing information about the distribution of the values.

## Features

- Add new values to the data set.
- Build the statistics for the data set.
- Get the number of values less than a given value.
- Get the number of values greater than a given value.
- Get the number of values between a given range.

## Requirements

- Values must be integers between 1 and 1000.
- Statistics must be built before making any query.

## Usage

To use DataCapture, simply create an instance of the class and start adding values. When all values are added, call the build_stats method to process the data. After that, you can use the less, greater and between methods to get information about the distribution of the values.

```
capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)

stats = capture.build_stats()
print(stats.less(4)) # 2
print(stats.greater(4)) # 2
print(stats.between(3, 6)) # 4
```

## Exceptions

DataCapture raises exceptions in the following situations:

- Statistics not built yet: raised by less, greater, and between methods if statistics have not been built yet. To fix, call `build_stats()` first.
- Invalid input: raised by add method if the value is not an integer between 1 and 1000.

## Testing

The test file tests the functionality and exceptions of the DataCapture class. To run the tests, simply execute the test file.

```
python test_stats.py
```
