import time

class ConveyorBelt:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} Conveyor Belt: Moving...")

class RoboticArm:
    def __init__(self):
        self.gripper_status = "open"

    def pick_glass(self, glass_type):
        self.gripper_status = "closed"
        print(f"Robotic Arm: Picked up the glass of type {glass_type}")

    def place_glass(self, box_position, box_type, place_position):
        self.gripper_status = "open"
        print(f"Robotic Arm: Placed the glass in the box of type {box_type} at position {box_position} in place {place_position}")

def main(glass_type, box_type):
    glass_conveyor = ConveyorBelt("Glass")
    box_conveyor = ConveyorBelt("Box")
    robotic_arm = RoboticArm()

    # Define the placement pattern for box A
    place_pattern = ["front left", "front right", "second right", "second left", "third left", "third right"]
    current_place_index = 0

    while True:
        for _ in range(6):  # Place 6 glasses for each box
            # Move the conveyors
            glass_conveyor.move()
            box_conveyor.move()

            # Input for glass and box positions
            glass_in_position = input("Is the glass in position? (yes/no): ")
            if glass_in_position.lower() != "yes":
                print("Error: Glass is not in position")
                return

            box_in_position = input("Is the box in position? (yes/no): ")
            if box_in_position.lower() != "yes":
                print("Error: Box is not in position")
                return

            # Pick and place the glass
            robotic_arm.pick_glass(glass_type)
            place_position = place_pattern[current_place_index]
            robotic_arm.place_glass(current_place_index + 1, box_type, place_position)

            # Move to the next place in the pattern
            current_place_index = (current_place_index + 1) % len(place_pattern)

            # Simulate some delay
            time.sleep(1)

        # After every 6 glasses, move the conveyors and detect another box
        print("6 glasses placed. Moving conveyors for the next box...")
        glass_conveyor.move()
        box_conveyor.move()

        another_box = input("Is there another box in position? (yes/no): ")
        if another_box.lower() != "yes":
            print("Process completed.")
            return

if __name__ == "__main__":
    glass_type = "A"  # Change glass type here
    box_type = "A"    # Change box type here
    main(glass_type, box_type)