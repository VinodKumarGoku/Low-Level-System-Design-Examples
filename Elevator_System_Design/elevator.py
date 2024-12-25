from abc import ABC, abstractmethod
from typing import List

from pdb import set_trace

import time

import uuid

"""
Entities
Lift
Floor
Elevator Controller
Button
Direction


Design pattern
1. Lift controller - singleton pattern, Facade
2. Button - Prototype 
3. Door, Additional Services for lift - Decorator
4. Repository design pattern
5. Lift status - state design pattern
"""

class ButtonType:
	FLOORBUTTON = 1
	EMERGENCYBUTTON = 2
	DIRECTIONBUTTON = 3


class LiftDirection:
	UP = 1
	DOWN = 2



class Button(ABC):
	def __init__(self, button_type: ButtonType, button_id: str):
		self.button_type = button_type
		self.button_id = button_id


	@abstractmethod
	def action(self):
		pass


	#@abstractmethod
	#def clone(self):
	#	return None


class FloorButton(Button):
	def __init__(self, button_type: ButtonType, button_id: str):
		super().__init__(button_type, button_id)


	def action(self):
		print(f"Button Pressed {self.button_id}")


class EmergencyButton(Button):
	def __init__(self, button_type: ButtonType, button_id: str):
		super().__init__(button_type, button_id)


	def action(self):
		print(f"Button Pressed {self.button_id}")


class DirectionButton(Button):
	def __init__(self, button_type: ButtonType, button_id: str):
		super().__init__(button_type, button_id)


	def action(self):
		print(f"Button Pressed {self.button_id}")


class DoorStatus:
	OPEN = 1
	CLOSED = 2


class LiftDoor:
	def __init__(self):
		self.status = DoorStatus.OPEN


class LiftStatus:
	MOVING = 1
	HALT = 2
	REPAIR = 3




class Lift:
	def __init__(self, lift_id, buttons: List[Button], doors: LiftDoor):
		self.lift_id = lift_id
		self.buttons = buttons
		self.doors = doors

		self.floor_number = 0
		self.lift_status = LiftStatus.HALT


	def move_lift(self, dest_floor):

		self.lift_status = LiftStatus.MOVING

		if dest_floor > self.floor_number:
			while self.floor_number < dest_floor:
				print(f"Lift {self.lift_id} in floor {self.floor_number}")
				time.sleep(0.5)
				self.floor_number += 1
		else:
			while self.floor_number > dest_floor:
				print(f"Lift {self.lift_id} in position {self.floor_number}")
				time.sleep(0.5)
				self.floor_number -= 1

		self.floor_number = dest_floor
		self.lift_status = LiftStatus.HALT



	def get_lift_status(self):
		return self.lift_status


	def stop_lift(self):
		self.lift_status = LiftStatus.HALT


class LiftContoller:
	def __init__(self):
		self.lifts = dict()


	def add_lift(self, lift: Lift):
		self.lifts[lift.lift_id] = lift


	def get_lift(self, src_floor, dst_floor) -> Lift:
		minval = float("inf")
		nearest_lift = None

		for lift_id, lift in self.lifts.items():
			nearest_floor = abs(lift.floor_number - dst_floor)
			if nearest_floor < minval:
				nearest_lift = lift
				minval = nearest_floor
		
		return nearest_lift


	def move_lift(self, src_floor, floor_number):
		nearest_lift = self.get_lift(src_floor, floor_number)

		nearest_lift.move_lift(floor_number)







