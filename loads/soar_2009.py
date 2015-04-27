from p4a.loadout import Crate
from base import Base

class soar_pilot(Base):
	headgear = 'rhsusf_hgu56p_mask'
	items = Base.items + [
		'ItemGPS',
	]

	class Primary:
		weapon = 'rhs_weap_m4'
		mags = [['rhs_mag_30Rnd_556x45_Mk318_Stanag', 30],]

	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 8]]

	class Uniform:
		type = 'U_B_HeliPilotCoveralls'
		items = Base.Uniform.items + [
			['cw_item_9liner_medivac', 1],
			['cw_item_9liner_cas', 1],
			['cw_item_5liner_gcff', 1],
			['cw_item_cas_check_in_breef', 1],
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 2],
			['RH_15Rnd_9x19_M9', 2],
		]
	class Vest:
		type = 'V_TacVest_oli'
		items = [
			['rhs_mag_m18_green', 2],
		]
	class Backpack:
		type = 'tf_anprc155'
		items = [
			['rhsusf_ANPVS_15', 1],
			['ToolKit', 1],
		]

class soar_crew(soar_pilot):
	pass

