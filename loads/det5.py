import base


#add fuccking lasers for rails
#snipers to box
#add chemlights for pubs

class det5_base(base.Base):
	class NoWrite: pass
	headgear = 'rhsusf_opscore_03_ocp'
	binoc = 'Rangefinder'
	items = base.Base.items + [
		'ItemGPS',
		'tf_microdagr',
		'tf_anprc152_1',
	]

	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 12]]
		suppressor = 'RH_m9qd'

	class Uniform:
		type = 'rhs_uniform_cu_ocp_patchless'
		items = base.Base.Uniform.items + [
			['cw_item_9liner_medivac', 1],
			['cw_item_9liner_cas', 1],
			['cw_item_5liner_gcff', 1],
			['cse_morphine', 2],
			['cse_epinephrine', 2],
			['RH_15Rnd_9x19_M9', 1],
		]
	class Vest:
		type = 'V_PlateCarrier2_rgr'
		items = [
			['rhs_mag_m67', 2],
		]
	class Backpack:
		type = 'rhsusf_assault_eagleaiii_ocp'
		items = [
			['tf_anprc148jem', 2],
			['rhsusf_ANPVS_14', 1],
			['alive_tablet', 1],
			['rhs_googles_clear', 2],
		]
	

class rifleman_det5(det5_base):
	class Primary:
		weapon = 'rhs_weap_m4a1_blockII_grip2'
		optic = 'SMA_eotech552_kf'
		suppressor = 'rhsusf_acc_rotex5_grey'
		rail = 'SMA_ANPEQ15_BLK'
		mags = [
			['rhs_mag_30Rnd_556x45_Mk318_Stanag', 30],
		]
	class Vest(det5_base.Vest):
		items = det5_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_Mk318_Stanag', 2],
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 2],
		]

	class Backpack(det5_base.Backpack):
		items = det5_base.Backpack.items + [
			['ACRE_PRC152', 1],
			['rhs_mag_30Rnd_556x45_Mk318_Stanag', 2],
		]
		
class officer_det5(det5_base):
	class Primary:
		weapon = 'SMA_HK416vfg'
		optic = 'SMA_eotech552_kf'
		suppressor = 'SMA_supp1b_556'
		rail = 'rhsusf_acc_anpeq15'
		mags = [
			['SMA_30Rnd_556x45_M855A1', 30],
		]
	class Vest(det5_base.Vest):
		type = 'V_PlateCarrierSpec_rgr'
		items = det5_base.Vest.items + [
			['SMA_30Rnd_556x45_M855A1', 2],
			['SMA_30Rnd_556x45_M855A1_Tracer', 2],
		]
	class Backpack(det5_base.Backpack):
		items = det5_base.Backpack.items + [
			['SMA_30Rnd_556x45_M855A1', 2],
			['rhs_mag_m67', 1],
			['SmokeShell', 2],
		]

class sniper_det5(det5_base):
	headgear = ''
	class Primary:
		weapon = 'SMA_Mk17'
		optic = 'SMA_eotech552_3XDOWN_des'
		suppressor = 'SMA_spSCARtan_762'
		rail = 'rhsusf_acc_anpeq15'
		mags = [
			['SMA_20Rnd_762x51mm_M80A1_EPR', 30],
		]
	class Vest(det5_base.Vest):
		type = 'V_PlateCarrier2_rgr'
		items = det5_base.Vest.items + [
			['SMA_20Rnd_762x51mm_M80A1_EPR', 5],
		]
	class Backpack(det5_base.Backpack):
		type = 'rhsusf_assault_eagleaiii_ocp'
		items = det5_base.Backpack.items + [
			['SMA_20Rnd_762x51mm_M80A1_EPR', 2],
			['SMA_20Rnd_762x51mm_M80A1_EPR_Tracer', 2],
			['ClaymoreDirectionalMine_Remote_Mag', 1],
		]
		
class gunner_det5(det5_base):
	headgear = 'rhsusf_opscore_03_ocp'
	class Primary:
		weapon = 'rhs_weap_m249_pip'
		optic = 'SMA_eotech552_kf'
		mags = [
			['rhsusf_100Rnd_556x45_soft_pouch', 100],
		]
	class Vest(det5_base.Vest):
		type = 'V_PlateCarrier2_rgr'
		items = det5_base.Vest.items + [
			['rhsusf_100Rnd_556x45_soft_pouch', 1],
			['30Rnd_556x45_Stanag_Tracer_Red', 1],
		]
	class Backpack(det5_base.Backpack):
		items = det5_base.Backpack.items + [
			['rhsusf_100Rnd_556x45_soft_pouch', 1],
			['30Rnd_556x45_Stanag_Tracer_Red', 1],
		]

class medic_det5(det5_base):
	class Primary:
		weapon = 'rhs_weap_m4a1_blockII_grip2'
		optic = 'SMA_eotech552_kf'
		suppressor = 'rhsusf_acc_rotex5_grey'
		mags = [
			['rhs_mag_30Rnd_556x45_Mk318_Stanag', 30],
		]
	class Vest(det5_base.Vest):
		type = 'V_KORA_K_CHICOM'
		items = det5_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 2],
			['rhs_mag_30Rnd_556x45_Mk318_Stanag', 4],
		]
	class Backpack(det5_base.Backpack):
		items = det5_base.Backpack.items + base.MedicSupplies

class medic_det5_1tk(medic_det5):
	headgear = 'rhsusf_opscore_03_ocp'
	class Uniform(medic_det5.Uniform):
		type = 'V_PlateCarrierSpec_rgr'
	class Primary(medic_det5.Primary):
		weapon = 'rhs_weap_m4a1_blockII_grip2'

class commo_det5(det5_base):
	headgear = 'rhsusf_opscore_03_ocp'
	class Primary:
		weapon = 'rhs_weap_m4a1_blockII_grip2'
		optic = 'SMA_eotech552_kf'
		suppressor = 'rhsusf_acc_rotex5_grey'
		mags = [
			['rhs_mag_30Rnd_556x45_Mk318_Stanag', 30],
		]
	class Vest(det5_base.Vest):
		type = 'V_PlateCarrierSpec_rgr'
		items = det5_base.Vest.items + [
			['tf_anprc148jem', 2],
			['rhs_mag_30Rnd_556x45_Mk318_Stanag', 4],
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 2],
		]
	class Backpack:
		type = 'rhsusf_assault_eagleaiii_ocp'
