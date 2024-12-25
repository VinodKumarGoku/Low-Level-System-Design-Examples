class Lift:
	def __init__(self, lift_id, name):
		self.lift_id = lift_id
		self.name = name



class LiftContollerSingleton(object):
	__lifts: dict = dict()
	__lift_controller_instance = None


	def __new__(cls):
		if cls.__lift_controller_instance is None:
			print("Creating new instance")
			cls.__lift_controller_instance = super(LiftContollerSingleton, cls).__new__(cls)
			return cls.__lift_controller_instance
		else:
			print("Already created instance")
			return cls.__lift_controller_instance



	@classmethod
	def add_lift(cls, lift):
		cls.__lifts[lift.lift_id] = lift


	@classmethod
	def get_lift(cls, lift_id):
		return cls.__lifts[lift_id]
	


lift1 = Lift(1, "Ram")
lift2 = Lift(2, "Sita")

lift_controller1 = LiftContollerSingleton()
lift_controller2 = LiftContollerSingleton()

lift_controller1.add_lift(lift1)
lift_controller2.add_lift(lift2)


for i in range(10):
	val = LiftContollerSingleton()

