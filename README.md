# RationalMathLibrary

A Python library for performing arithmetic operations on rational numbers, including simplification, addition, subtraction, multiplication, and division. This repository also contains methods for finding the highest common factor (HCF) and least common multiple (LCM) of two integers, which are utilized for fraction operations.

## Features

- **HCF and LCM Calculation**: Easily compute the highest common factor and least common multiple of two integers.
- **Fraction Operations**:
  - Simplify fractions to their lowest terms.
  - Add, subtract, multiply, and divide rational numbers.
- **Reciprocal**: Obtain the reciprocal of a given fraction.

## Structure

- `class math`: Contains methods for HCF and LCM calculations.
- `class rational`: Provides a blueprint for rational numbers, with methods to perform arithmetic operations and simplify fractions.

## Usage

### Initial Setup
Clone the repository and include the `math` and `rational` classes in your project to start using the rational number operations.

### Examples

#### HCF and LCM Calculation

```python
print(math.hcf(12, 64))   # Output: 4
print(math.lcm(12, 64))   # Output: 192
