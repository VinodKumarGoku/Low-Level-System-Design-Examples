import pytest

from pdb import set_trace

from elevator import *


@pytest.fixture(name="lift_controller")
def fixture_lift_controller(request):
	# 2 lift, 4 floor buttons, 2 emergency buttons, 2 direction buttons

	button11 = FloorButton(ButtonType.FLOORBUTTON, 1)
	button12 = FloorButton(ButtonType.FLOORBUTTON, 2)
	button21 = FloorButton(ButtonType.FLOORBUTTON, 3)
	button22 = FloorButton(ButtonType.FLOORBUTTON, 4)

	alarmbutton11 = EmergencyButton(ButtonType.EMERGENCYBUTTON, 1)
	stopbutton12 = EmergencyButton(ButtonType.EMERGENCYBUTTON, 2)
	alarmbutton21 = EmergencyButton(ButtonType.EMERGENCYBUTTON, 1)
	stopbutton22 = EmergencyButton(ButtonType.EMERGENCYBUTTON, 2)

	updirection1 = DirectionButton(ButtonType.DIRECTIONBUTTON, 1)
	updirection2 = DirectionButton(ButtonType.DIRECTIONBUTTON, 2)
	downdirection1 = DirectionButton(ButtonType.DIRECTIONBUTTON, 1)
	downdirection2 = DirectionButton(ButtonType.DIRECTIONBUTTON, 2)

	door1 = LiftDoor()
	door2 = LiftDoor()

	button1list = [button11, button12]
	button2list = [button21, button22]

	lift_controller = LiftContoller()

	lift1 = Lift(1, button1list, door1)
	lift2 = Lift(2, button2list, door2)

	lift_controller.add_lift(lift1)
	lift_controller.add_lift(lift2)

	yield lift_controller
	






def test_elevator_basic(lift_controller: LiftContoller):
	lift_controller.move_lift(0, 10)

	#lift1 = lift_controller.lifts[1] 

	lift_controller.move_lift(0, 3)

	#set_trace()	

	print("Hello World")
