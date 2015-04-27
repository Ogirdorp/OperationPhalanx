import base

class acr_base(base.Base):
	class NoWrite: pass
	headgear = 'rhsusf_mich_helmet_marpatd_alt'

	class Primary:
		optic = 'rhsusf_acc_ACOG'
		rail = 'rhsusf_acc_anpeq15'
	
	class Uniform:
		type = 'rhs_uniform_FROG01_d'
		items = base.Base.Uniform.items + [
		]
	class Vest:
		type = 'rhsusf_iotv_ocp'
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

class acr_rifleman(acr_base):
	class Primary(acr_base.Primary):
		weapon = 'rhs_weap_m4'
		mags = [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_No_Tracer', 30],
		]
	class Vest(acr_base.Vest):
		items = acr_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_No_Tracer', 2],
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 2],
		]
	class Backpack(acr_base.Backpack):
		items = acr_base.Backpack.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_No_Tracer', 2],
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 2],
		]

class acr_tl(acr_rifleman):
	binoc = 'Binocular'
	items = acr_rifleman.items + ['tf_rf7800str']
	class Primary(acr_base.Primary):
		weapon = 'rhs_weap_m4a1_m320'
		mags = [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_No_Tracer', 30],
			['rhs_mag_M433_HEDP', 1],
		]
	class Uniform(acr_base.Uniform):
		items = acr_base.Uniform.items + [
			['cw_item_9liner_medivac', 1],
			['cw_item_9liner_cas', 1],
			['cw_item_5liner_gcff', 1],
		]
	class Vest(acr_base.Vest):
		items = acr_base.Vest.items + [
			['rhs_mag_M433_HEDP', 3],
			['rhs_mag_M714_white', 3],
		]

	class Backpack(acr_rifleman.Backpack):
		items = acr_rifleman.Backpack.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 5],
			['rhs_mag_M433_HEDP', 8],
			['rhs_mag_M714_white', 6],
			['rhs_mag_M713_red', 2],
			['rhs_mag_M585_white', 2],
		]

class acr_sl(acr_tl):
	binoc = 'Binocular'
	class Backpack(acr_tl.Backpack):
		items = acr_tl.Backpack.items + [
			['tf_anprc152', 1],
		]
	class Primary(acr_tl.Primary):
		weapon = 'rhs_weap_m4a1_carryhandle_grip'
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(acr_base.Uniform):
		items = acr_base.Uniform.items + [['RH_15Rnd_9x19_M9', 2]]

class acr_ar(acr_base):
	class Primary(acr_base.Primary):
		weapon = 'rhs_weap_m249_pip'
		mags = [
			['rhsusf_100Rnd_556x45_soft_pouch', 100],
		]

	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(acr_base.Uniform):
		items = acr_base.Uniform.items + [['RH_15Rnd_9x19_M9', 2]]

	class Vest(acr_base.Vest):
		items = acr_base.Vest.items + [
			['rhsusf_100Rnd_556x45_soft_pouch', 2],
		]
	class Backpack(acr_base.Backpack):
		items = acr_base.Backpack.items + [
			['rhsusf_100Rnd_556x45_soft_pouch', 3],
		]

class acr_aar(acr_rifleman):
	binoc = 'Binocular'
	class Vest(acr_base.Vest):
		items = acr_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 5],
		]
	class Backpack(acr_rifleman.Backpack):
		items = acr_rifleman.Backpack.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 3],
			['rhsusf_200Rnd_556x45_soft_pouch', 2],
		]

class acr_mg(acr_base):
	class Primary(acr_base):
		weapon = 'rhs_weap_m240B'
		optic = 'rhsusf_acc_ELCAN'
		mags = [['rhsusf_100Rnd_762x51', 100]]
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(acr_base.Uniform):
		items = acr_base.Uniform.items + [['RH_15Rnd_9x19_M9', 2]]

	class Vest(acr_base.Vest):
		items = acr_base.Vest.items + [
			['rhsusf_100Rnd_762x51', 2],
		]

	class Backpack(acr_base.Backpack):
		items = acr_base.Backpack.items + [
			['rhsusf_100Rnd_762x51', 2],
		]

class acr_amg(acr_rifleman):
	items = acr_rifleman.items + ['tf_rf7800str']
	binoc = 'Binocular'
	class Vest(acr_base.Vest):
		items = acr_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 6],
		]
	class Backpack(acr_rifleman.Backpack):
		items = acr_rifleman.Backpack.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 2],
			['rhsusf_100Rnd_762x51', 3],
		]

class acr_at(acr_rifleman):
	class Secondary:
		weapon = 'rhs_weap_fgm148'
		mags = [
			['rhs_fgm148_magazine_AT', 1],
		]

	class Backpack(acr_rifleman.Backpack):
		items = acr_rifleman.Backpack.items + [
			['rhs_fgm148_magazine_AT', 1],
		]

class acr_aat(acr_rifleman):
	items = acr_rifleman.items + ['tf_rf7800str']
	binoc = 'Rangefinder'
	class Backpack(acr_rifleman.Backpack):
		items = acr_rifleman.Backpack.items + [
			['rhs_fgm148_magazine_AT', 2],
		]

class acr_pl(acr_rifleman):
	items = acr_rifleman.items + ['tf_rf7800str']
	binoc = 'lerca_1200_black'

	class Primary(acr_tl.Primary):
		weapon = 'rhs_weap_m4a1'
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(acr_base.Uniform):
		items = acr_base.Uniform.items + [
			['RH_15Rnd_9x19_M9', 2],
			['cw_item_9liner_medivac', 1],
			['cw_item_9liner_cas', 1],
			['cw_item_5liner_gcff', 1],
		]

	class Backpack(acr_rifleman.Backpack):
		items = acr_rifleman.Backpack.items + [
			['tf_anprc152', 2],
			['alive_tablet', 1],
		]
	
class acr_rto(acr_rifleman):
	items = acr_rifleman.items + ['tf_rf7800str']
	binoc = 'Binocular'
	class Backpack(acr_rifleman.Backpack):
		type = "tf_rt1523g_big"
		items = acr_rifleman.Backpack.items + [
			['alive_tablet', 1],
			['tf_anprc152', 2],
		]

class acr_corpsman(acr_rifleman):
	items = acr_rifleman.items + ['tf_rf7800str']
	class Backpack(acr_base.Backpack):
		items = acr_base.Backpack.items + base.MedicSupplies + [
			['tf_anprc152', 1],
		]

class acr_crewman(acr_rifleman):
	items = acr_rifleman.items + ['tf_rf7800str']
	headgear = 'rhsusf_cvc_ess'

class acr_commander(acr_rifleman):
	items = acr_rifleman.items + ['tf_rf7800str']
	headgear = 'rhsusf_cvc_ess'
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(acr_base.Uniform):
		items = acr_rifleman.Uniform.items + [['RH_15Rnd_9x19_M9', 2]]

	class Backpack:		
		items = acr_crewman.Backpack.items + [
			['tf_anprc152', 2],
		]