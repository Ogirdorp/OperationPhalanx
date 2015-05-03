from p4a.loadout import LoadOut

class Base(LoadOut):
	class NoWrite: pass
	def __init__(self):
		super(Base, self).__init__()
		self.remove('all')
		self.clear('all')

	items = [
		'ItemMap',
		'ItemCompass',
	]
	
	class Uniform:
		items = [
			['ACE_fieldDressing', 5],
			['ACE_elasticBandage', 3],
			['ACE_packingBandage', 3],
			['ACE_quikclot', 3],
			['ACE_tourniquet', 4],
			['ACE_EarPlugs', 1],
		]

MedicSupplies = [
	['ACE_fieldDressing', 16],
	['ACE_packingBandage', 16],
	['ACE_tourniquet', 8],
	['ACE_morphine', 4],
	['ACE_epinephrine', 4],
	['ACE_atropine', 4],
	['ACE_salineIV_250', 4],
	['ACE_quikclot', 16],
	['ACE_surgicalKit', 1],
	['ACE_personalAidKit', 1],
]