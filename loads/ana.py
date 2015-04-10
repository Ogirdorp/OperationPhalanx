import base

class ana_base(base.Base):
	headgear = 'LOP_H_PASGTHelmet_OLV'
	items = [
		'ItemWatch',
		'ItemMap',
		'ItemCompass',
	]	
	class HandGun:
		weapon = 'RH_mak'
		mags = [['RH_8Rnd_9x18_Mak', 8]]

	class Uniform:
		type = 'LOP_U_AA_Fatigue_01_slv'
		items = base.Base.Uniform.items + [
			['RH_8Rnd_9x18_Mak', 2],
		]
	class Vest:
		type = 'LOP_V_CarrierRig_WDL'
		items = [
			['rhs_mag_an_m8hc', 2],
			['Chemlight_blue', 1],
			['Chemlight_red', 1],
		]
	class Backpack:
		type = 'B_Kitbag_rgr'
		items = [
			['rhs_mag_rgd5', 2],
		]
################  Rifleman

class ana_rifleman(cdf_base):
	class Primary:
		weapon = 'rhs_weap_m16a4_carryhandle'
		mags = [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 30],
		]
	class Vest(cdf_base.Vest):
		items = cdf_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_Mk318_Stanag', 5],
		]
	class Backpack(cdf_base.Backpack):
		items = cdf_base.Backpack.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 5],
		]

class ana_rifleman_light(cdf_base):
	class Primary:
		weapon = 'rhs_weap_m4'
		mags = [
			['rhs_mag_30Rnd_556x45_Mk318_Stanag', 30],
		]
	class Vest(cdf_base.Vest):
	        items = cdf_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_Mk318_Stanag', 5],
		]
	class Backpack(cdf_base.Backpack):
		items = cdf_base.Backpack.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 2],
		]

		
################  Grenadier 

class ana_grenadier(cdf_rifleman_light):
	class Primary:
		weapon = 'rhs_m4_m320'
		mags = [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 30],
			['1Rnd_HE_Grenade_shell', 1],
		]

	class Secondary:
		weapon = 'rhs_weap_rpg26'
		mags = [
			['rhs_rpg26_mag', 1],
		]
	class Vest(cdf_rifleman_light.Vest):
		type = 'LOP_V_CarrierRig_WDL'
		items = cdf_rifleman_light.Vest.items + [
			['1Rnd_HE_Grenade_shell', 5],
		]

	class Backpack(cdf_rifleman_light.Backpack):
		items = cdf_rifleman_light.Backpack.items + [
			['1Rnd_HE_Grenade_shell', 5],
			['rhs_mag_M585_white', 4],
			['rhs_mag_m714_White', 4],
		]

################  Squad Leader

class ana_tl(cdf_rifleman):
	headgear = 'LOP_H_PASGTHelmet_cover_AA'
	items = cdf_rifleman.items + ['tf_anprc154']
	binoc = 'Binocular'

	class Primary:
		weapon = 'rhs_m4_m320'
		mags = [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 30],
			['1Rnd_HE_Grenade_shell', 1],
		]
	class Vest(cdf_rifleman.Vest):
		type = 'LOP_V_CarrierRig_WDL'
		items = cdf_rifleman.Vest.items + [
			['1Rnd_HE_Grenade_shell', 5],
		]

	class Uniform(cdf_rifleman.Uniform):
		type = 'LOP_U_AA_Fatigue_01'
		items = cdf_rifleman.Uniform.items + [
			['cw_item_9liner_medivac', 1],
			['cw_item_9liner_cas', 1],
			['cw_item_5liner_gcff', 1],
		]
	class Backpack(cdf_rifleman.Backpack):
		items = cdf_rifleman.Backpack.items + [
			['rhsusf_ANPVS_14', 1],
			['1Rnd_HE_Grenade_shell', 5],
			['rhs_mag_M585_white', 10],
			['rhs_mag_m714_White', 5],
		]
		
class ana_sl(cdf_tl):
	headgear = 'LOP_H_PASGTHelmet_cover_AA'
	class Backpack(cdf_rifleman.Backpack):
		items = cdf_rifleman.Backpack.items + [
			['tf_fadak', 1],
		]
################  Vehicle Crew Driver/Gunner

class cdf_crew(cdf_rifleman):
	headgear = 'LOP_H_PASGTHelmet_TAN'
	items = cdf_base.items + ['tf_anprc154']

	class Primary:
		weapon = 'rhs_weap_m16a4_carryhandle'
		mags = [
			['rhs_mag_30Rnd_556x45_Mk318_Stanag', 30],
		]
	class Backpack(cdf_rifleman_light.Backpack):
		items = cdf_rifleman_light.Backpack.items + [
			['rhsusf_ANPVS_14', 1],
		]
class cdf_asl_gunner(cdf_crew):
	class Backpack(cdf_crew.Backpack):
		items = cdf_crew.Backpack.items + [
			['rhsusf_ANPVS_14', 1],
			['tf_anprc152_1', 1],
		]



################  Medium Machine Gunner
class ana_mg(cdf_base):
	binoc = 'Binocular'
	class Primary:
		weapon = 'rhs_weap_m249_pip'
		mags = [
			['rhsusf_100Rnd_556x45_soft_pouch', 100],
		]
	class Vest(cdf_base.Vest):
		type = 'LOP_V_CarrierRig_WDL'
		items = cdf_base.Vest.items + [
			['rhsusf_100Rnd_556x45_soft_pouch', 1],
		]
	class Backpack(cdf_base.Backpack):
		items = cdf_base.Backpack.items + [
			['rhsusf_100Rnd_556x45_soft_pouch', 2],
		]

################  Medic
class cdf_medic(cdf_rifleman_light):
	items = cdf_crew.items + [
		'tf_anprc154',
	]
	class Vest(cdf_rifleman_light.Vest):
		items = cdf_rifleman_light.Vest.items + [
			['cw_item_9liner_medivac', 1],
			['rhs_mag_rdg2_white', 2],
		]
	class Backpack(cdf_rifleman_light.Backpack):
		items = cdf_base.Backpack.items + base.MedicSupplies + [
			['rhs_mag_rdg2_white', 2],
		]


################  Platoon Leader

class ana_pl(cdf_rifleman):
	items = cdf_rifleman.items + ['tf_anprc154']
	binoc = 'Binocular'
	headgear = 'LOP_H_Pakol'
	class Primary:
		weapon = 'rhs_weap_m16a4_carryhandle'
		mags = [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 30],
		]
	class HandGun:
		weapon = 'RH_mak'
		mags = [
			['RH_8Rnd_9x18_Mak', 1],
		]
	class Uniform(cdf_rifleman.Uniform):
		type = 'LOP_U_AA_Fatigue_01'
		items = cdf_rifleman.Uniform.items + [
			['cw_item_9liner_medivac', 1],
			['cw_item_9liner_cas', 1],
			['cw_item_5liner_gcff', 1],
		]
	class Vest(cdf_rifleman.Vest):
		type = 'LOP_V_CarrierRig_WDL'
		items = cdf_base.Vest.items + [
			['tf_anprc152', 1],
			['rhs_mag_30Rnd_556x45_Mk318_Stanag', 5],
		]
	class Backpack(cdf_base.Backpack):
		items = cdf_base.Backpack.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 2],
			['rhs_mag_an_m8hc', 2],
			['rhsusf_ANPVS_14', 1],
		]

################  Platoon RTO

class ana_rto(cdf_rifleman_light):
	binoc = 'Binocular'
	items = cdf_rifleman_light.items + ['tf_anprc154']
	class Backpack:
		type = 'tf_anprc155'
		items = cdf_rifleman_light.Backpack.items + [
			['tf_fadak', 1],
		]