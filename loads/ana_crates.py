from p4a.loadout import Crate

class ana_explosives(Crate):
	title = 'ANA Explosives and CSW'
 	base = 'Box_NATO_Wps_F'
	weapons = [
		['ACE_HandFlare_White', 500],
		['ACE_HandFlare_Red', 200],
		['ACE_HandFlare_Green', 200],
	]
	magazines = [
		['ACE_HandFlare_White', 500],
		['ACE_HandFlare_Red', 200],
		['ACE_HandFlare_Green', 200],
		
		['rhs_mag_m67', 500],
		['rhs_mag_an_m8hc', 500],

		['rhs_mag_m18_red', 100],
		['rhs_mag_m18_yellow', 100],
		['rhs_mag_m18_green', 100],
		['rhs_mag_m18_purple', 100],

		['1Rnd_HE_Grenade_shell', 200],
		['rhs_mag_M433_HEDP', 200],
		['rhs_mag_M585_white', 100],
		['rhs_mag_m661_green', 100],
		['rhs_mag_m662_red', 100],
		
		['rhs_mag_m714_White', 100],
		['rhs_mag_m715_Green', 100],
		['rhs_mag_m713_Red', 100],

	]

	backpacks = [
		['RHS_NSV_Gun_Bag', 10],
		['RHS_NSV_Tripod_Bag', 10],
		
		['RDS_DShkM_Gun_Bag', 10],
		['RDS_DShkM_TripodLow_Bag', 10],

		['RDS_AGS30_Gun_Bag', 10],
		['RDS_AGS30_Tripod_Bag', 10],

		['RDS_Metis_Gun_Bag', 10],
		['RDS_Metis_Tripod_Bag', 10],

		['RDS_SPG9_Gun_Bag', 10],
		['RDS_SPG9_Tripod_Bag', 10],
	]

class ana_launchers(Crate):
	title = 'ANA Launchers and Warheads'
 	base = 'Box_NATO_Wps_F'
	weapons = [
		['rhs_weap_rpg7', 50],
		['rhs_weap_rpg26', 500],
		['rhs_weap_rshg2', 100],
	]
	magazines = [
		['rhs_rpg7_PG7VL_mag', 400],
		['rhs_rpg7_PG7VR_mag', 200],
		['rhs_rpg26_mag', 500],
		['rhs_rshg2_mag', 100],
	]

class ana_weapons(Crate):
	title = 'ANA Rifles and Ammo'
 	base = 'Box_NATO_Wps_F'
	magazines = [
		['rhs_mag_30Rnd_556x45_Mk318_Stanag', 800],
		['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 300],
		['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Green', 300],
		['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Yellow', 300],
		
		['rhsusf_100Rnd_556x45_soft_pouch', 500],
		['hlc_50rnd_556x45_EPR', 500],

		['rhsusf_100Rnd_762x51', 500],
		['rhsusf_100Rnd_762x51_m993', 500],
		['rhsusf_100Rnd_762x51_m80a1epr', 500],
	]

