# Procedural Shading Notes

## Colors

### values are nodes in grey

### Colors are nodes in yellow

### Vectors are nodes in Purple

### Shaders are nodes in Green

### _Values are_

0 = Black

1 = White

- The color can go below to below 1 but and above 1
- When the color is converted to a value, the three color channels have to be reduced to 1
- The calculated value is the **luminosity Value**
- The Luminosity is a method to the percieved brightness nad is caluclated as a whited avarage of RGB
- If you have to choose a color for a value, choose the same value for all RGB channels
- Use **COMBINE RGB NODE**

**set color management Look to NONE**

**set filmic to none to have a better understanding just for a little**

### _Vectors are_

**containers of multiples separate values**

- it has 3 dimensions (x,y,z)
- it always interpreted as a _position_ or _Direction_
- use **Combine XYZ NODE**
- The values are not clamped from 0 and 1
- NO CONVERSION IS NEEDED
  
![title](Images/Vector1.png)







