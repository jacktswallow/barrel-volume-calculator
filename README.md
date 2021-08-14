# Barrel volume calculator
Python application for calculating the volume of liquid in a barrel.

## Usage
Add new barrels by adding a new row to the included barrels.csv file.
Existing barrels may be edited by editing the existing rows in the barrels.csv file.
Do not alter or delete the first row of the barrels.csv file.
Do not rename the .csv file.

Variable formatting is as follows:
- Height: Must be a numerical value.
- End radius: Must be a numerical value.
- Middle radius: Must be a numerical value.
- Thickness: Must be a numerical value or a dash '-'. 
  - A dash means that thickness has not been supplied.
  - When thickness is given, it will automatically be subtracted from height. 
    For example, a height of '94' and a thickness of '2' will result in a height of 92 being used in the calculation.
  - When thickness is not given (denoted by '-'), height will not be altered.
    For example, a height of '94' and a thickness of '-' will result in a height of 94 being used in the calculation.

Formula formatting is as follows:
- Accepted variables are as follows:
  - 'H' (Height) (cm)
  - 'r' (End radius) (cm)
  - 'R' (Middle radius) (cm)
  - 'd' (Dip measurement) (cm)
- Order of operations applies
- Formulas may contain spaces or not ('2 + 4' and '2+4' are both acceptable)
- Multiplication: '*' (eg: '3*R')
- Division: '/' (eg: 'H/15')
- Addition: '+' (eg: 'r+8')
- Subtraction: '-' (eg: '2-1')
- Power of: '**' (eg: 'r**2' is r squared, '3**r' is 3 to the power of r)
- Brackets: '(' and ')' (eg: '(r**2)/15)'
- Pi/π: 'pi' (eg: 'pi*2') (any other variantion including 'Pi', or 'π' will not work)
- Many other operators likely work, but have not been tested

## Written by Jack Swallow
