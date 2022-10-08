# Automatic-abstract-model-computation-from-Verilog-design-descriptions

## What is abstraction?
it is process of hiding implementation details and 
only showing the functionality to the user. 
Abstraction focus on what the object does instead of how it does. 
It is achieved by using Abstract class and Interface. 
abstract methods (methods without body, cannot be static and final), 
interface must implemented and abstract classes must be extended 
by regular classes in order to achieve abstraction 

## Why is Abstraction necessary?
Due to the complexity of life, abstraction is necessary. Complex systems must be simplified for people to understand and use them. 
To understand this in simple form. Let us take an example of 8-Bit Counter.
8-Bit Counter will count from 0 to 255. Let us assume that this design is a bit complicated. To make this design simpler we have to do abstraction. This can be done by introducing new states in between the counter or reducing the bit width. The new design/Abstract model will count from 0 to 127, and then 127 to 255. This can be easily visualized in the following diagram:

![image](https://user-images.githubusercontent.com/56917291/166094629-89ee67c6-6225-4e2c-bcb6-28c3c3822051.png)

## How to automate the abstraction of verilog models
#### Reducing the Bit width 
#### Removing the same registers
#### Abstraction of verilog variables
#### Abstraction of verilog constants

## Resources
#### https://link.springer.com/chapter/10.1007/0-306-47658-4_3?noAccess=true
#### https://opencores.org/
#### https://github.com/DARClab-UTD/S2CBench

