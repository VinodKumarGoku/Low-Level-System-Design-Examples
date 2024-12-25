from abc import abstractmethod


class LiftType:
	NORMAL = 1
	SPECIAL = 2
	VIP = 3
	UNKNOWN = 100000


class Lift:
	def __init__(self, lift_id, lift_type):
		self.lift_id = lift_id
		self.lift_type = lift_type
	
	def get_lift(self):
		return self.lift_id


class NormalLift(Lift):
	def __init__(self, lift_id, lift_type):
		super().__init__(lift_id, lift_type)


class SpecialLift(Lift):
	def __init__(self, lift_id, lift_type):
		super().__init__(lift_id, lift_type)


class VipLift(Lift):
	def __init__(self, lift_id, lift_type):
		super().__init__(lift_id, lift_type)



class LiftFactory:
	__lift_ids = dict()


	def get_lift(self, lift_type: LiftType):
		current_id = 1
		if lift_type in LiftFactory.__lift_ids.keys():
			current_id += LiftFactory.__lift_ids[lift_type]
		LiftFactory.__lift_ids[lift_type] = current_id

		if lift_type == LiftType.NORMAL:
			return NormalLift(current_id, lift_type)
		elif lift_type == LiftType.SPECIAL:
			return SpecialLift(current_id, LiftType.SPECIAL)
		elif lift_type == LiftType.VIP:
			return VipLift(current_id, LiftType.VIP)
		else:
			return Lift(current_id, LiftType.UNKNOWN)



if __name__ == "__main__":

	lift_factory = LiftFactory()

	normal_lift = lift_factory.get_lift(LiftType.NORMAL)
	special_lift = lift_factory.get_lift(LiftType.SPECIAL)
	vip_lift = lift_factory.get_lift(LiftType.VIP)

	print([normal_lift.get_lift(), special_lift.get_lift(), vip_lift.get_lift()])

	normal_lift1 = lift_factory.get_lift(LiftType.NORMAL)
	special_lift1 = lift_factory.get_lift(LiftType.SPECIAL)
	vip_lift1 = lift_factory.get_lift(LiftType.VIP)

	print([normal_lift1.get_lift(), special_lift1.get_lift(), vip_lift1.get_lift()])
