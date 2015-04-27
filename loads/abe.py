import base

class abe_base(base.Base):
	class NoWrite: pass
	headgear = 'rhsusf_ach_helmet_ESS_ocp'

	class Primary:
		optic = 'rhsusf_acc_compm4'
		rail = 'SMA_ANPEQ15_BLK'
	
	class Uniform:
		type = 'rhs_uniform_cu_ocp_patchless'
		items = base.Base.Uniform.items + [
		]
	class Vest:
		type = 'rhsusf_iotv_ocp_Repair'
		items = [
			['rhs_mag_m67', 2],
			['rhs_mag_an_m8hc', 1],
		]
	class Backpack:
		type = 'rhsusf_assault_eagleaiii_ocp'
		items = [
			['rhsusf_ANPVS_14', 1],
			['rhs_mag_m67', 1],
			['rhs_googles_clear', 1],
		]

class abe_rifleman(abe_base):
	class Primary(abe_base.Primary):
		weapon = 'rhs_weap_m4_grip'
		mags = [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_No_Tracer', 30],
		]
	class Vest(abe_base.Vest):
		items = abe_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_No_Tracer', 2],
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 2],
		]
	class Backpack(abe_base.Backpack):
		items = abe_base.Backpack.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_No_Tracer', 2],
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 2],
		]

class abe_tl(abe_rifleman):
	binoc = 'Binocular'
	items = abe_rifleman.items + ['tf_rf7800str']
	class Primary(abe_base.Primary):
		weapon = 'rhs_weap_m4_m320'
		mags = [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_No_Tracer', 30],
			['rhs_mag_M433_HEDP', 1],
		]
	class Uniform(abe_base.Uniform):
		items = abe_base.Uniform.items + [
			['cw_item_9liner_medivac', 1],
			['cw_item_9liner_cas', 1],
			['cw_item_5liner_gcff', 1],
		]
	class Vest(abe_base.Vest):
		items = abe_base.Vest.items + [
			['rhs_mag_M433_HEDP', 3],
			['rhs_mag_M714_white', 3],
		]

	class Backpack(abe_rifleman.Backpack):
		items = abe_rifleman.Backpack.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 5],
			['rhs_mag_M433_HEDP', 8],
			['rhs_mag_M714_white', 6],
			['rhs_mag_M713_red', 2],
			['rhs_mag_M585_white', 2],
		]

class abe_sl(abe_tl):
	binoc = 'Binocular'
	class Backpack(abe_tl.Backpack):
		items = abe_tl.Backpack.items + [
			['tf_anprc152', 1],
		]
	class Primary(abe_tl.Primary):
		weapon = 'rhs_weap_m4_grip'
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(abe_base.Uniform):
		items = abe_base.Uniform.items + [['RH_15Rnd_9x19_M9', 2]]

class abe_ar(abe_base):
	class Primary(abe_base.Primary):
		weapon = 'rhs_weap_m249_pip'
		rail = 'rhsusf_acc_ELCAN'
		mags = [
			['rhsusf_100Rnd_556x45_soft_pouch', 100],
		]

	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(abe_base.Uniform):
		items = abe_base.Uniform.items + [['RH_15Rnd_9x19_M9', 2]]

	class Vest(abe_base.Vest):
		items = abe_base.Vest.items + [
			['rhsusf_100Rnd_556x45_soft_pouch', 2],
		]
	class Backpack(abe_base.Backpack):
		items = abe_base.Backpack.items + [
			['rhsusf_100Rnd_556x45_soft_pouch', 3],
		]

class abe_aar(abe_rifleman):
	binoc = 'Binocular'
	class Vest(abe_base.Vest):
		items = abe_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 5],
		]
	class Backpack(abe_rifleman.Backpack):
		items = abe_rifleman.Backpack.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 3],
			['rhsusf_200Rnd_556x45_soft_pouch', 2],
		]

class abe_mg(abe_base):
	class Primary(abe_base):
		weapon = 'rhs_weap_m240B'
		optic = 'rhsusf_acc_ELCAN'
		mags = [['rhsusf_100Rnd_762x51', 100]]
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(abe_base.Uniform):
		items = abe_base.Uniform.items + [['RH_15Rnd_9x19_M9', 2]]

	class Vest(abe_base.Vest):
		items = abe_base.Vest.items + [
			['rhsusf_100Rnd_762x51', 2],
		]

	class Backpack(abe_base.Backpack):
		items = abe_base.Backpack.items + [
			['rhsusf_100Rnd_762x51', 2],
		]

class abe_amg(abe_rifleman):
	items = abe_rifleman.items + ['tf_rf7800str']
	binoc = 'Binocular'
	class Vest(abe_base.Vest):
		items = abe_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 6],
		]
	class Backpack(abe_rifleman.Backpack):
		items = abe_rifleman.Backpack.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 2],
			['rhsusf_100Rnd_762x51', 3],
		]

class abe_at(abe_rifleman):
	class Secondary:
		weapon = 'rhs_weap_fgm148'
		mags = [
			['rhs_fgm148_magazine_AT', 1],
		]

	class Backpack(abe_rifleman.Backpack):
		items = abe_rifleman.Backpack.items + [
			['rhs_fgm148_magazine_AT', 1],
		]

class abe_aat(abe_rifleman):
	items = abe_rifleman.items + ['tf_rf7800str']
	binoc = 'Rangefinder'
	class Backpack(abe_rifleman.Backpack):
		items = abe_rifleman.Backpack.items + [
			['rhs_fgm148_magazine_AT', 2],
		]

class abe_pl(abe_rifleman):
	items = abe_rifleman.items + ['tf_rf7800str']
	binoc = 'lerca_1200_black'

	class Primary(abe_tl.Primary):
		weapon = 'rhs_weap_m4_grip'
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(abe_base.Uniform):
		items = abe_base.Uniform.items + [
			['RH_15Rnd_9x19_M9', 2],
			['cw_item_9liner_medivac', 1],
			['cw_item_9liner_cas', 1],
			['cw_item_5liner_gcff', 1],
		]

	class Backpack(abe_rifleman.Backpack):
		items = abe_rifleman.Backpack.items + [
			['tf_anprc152', 2],
			['alive_tablet', 1],
		]
	
class abe_rto(abe_rifleman):
	items = abe_rifleman.items + ['tf_rf7800str']
	binoc = 'Binocular'
	class Backpack(abe_rifleman.Backpack):
		type = "tf_rt1523g_big"
		items = abe_rifleman.Backpack.items + [
			['alive_tablet', 1],
			['tf_anprc152', 2],
		]

class abe_corpsman(abe_rifleman):
	items = abe_rifleman.items + ['tf_rf7800str']
	class Backpack(abe_base.Backpack):
		items = abe_base.Backpack.items + base.MedicSupplies + [
			['tf_anprc152', 1],
		]

class abe_crewman(abe_rifleman):
	items = abe_rifleman.items + ['tf_rf7800str']
	headgear = 'rhsusf_cvc_green_helmet'

class abe_commander(abe_rifleman):
	items = abe_rifleman.items + ['tf_rf7800str']
	headgear = 'rhsusf_cvc_green_ess'
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(abe_base.Uniform):
		items = abe_rifleman.Uniform.items + [['RH_15Rnd_9x19_M9', 2]]

	class Backpack:		
		items = abe_crewman.Backpack.items + [
			['tf_anprc152', 2],
		]