GLASS PACKING AUTOMATION SYSTEM
This code written in python simulates a factory automation system for packaging glasses into boxes. It represents a simple industrial process where 
glasses are moved on one conveyor belt, boxes on another, and a robotic arm picks upglasses and places them in specific positions within eachbox.

How the System Works:
The system consists of three main components:
● A conveyor belt for glasses
● A conveyor belt for boxes
● A robotic arm that picks and places glasses

The program runs through a cycle where:
1. Both conveyor belts move to bring glasses and boxesinto position
2. The system checks if both a glass and a box are properly positioned
3. The robotic arm picks up a glass and places it in a specific position in the box
4. This repeats until 6 glasses are placed in each box (following a predefined pattern)
5. After filling a box, the system checks if another box is available and repeats the process

Key Features
● Preset Placement Pattern: The robot follows a specific pattern when placing glasses in a box: "front left", "front right", "second right", "second left", "third left", "third right".
● User Interaction: The system requires confirmation that glasses and boxes are properly positioned before proceeding.
● Error Handling: If a glass or box is not in position, the process stops.
● Cyclical Operation: After filling one box with 6 glasses, the system can continue with another box.

The program has a slight delay (1 second) between operations to simulate the actual movement time of physical machinery in a real factory.

Practical Application
This simulation represents how industrial automation systems work in packaging facilities. In a real implementation, sensors would replace the manual confirmation inputs, 
and the system would be connected toactual robotic hardware rather than just printing status messages.
