from p4a.loadout import Crate
 
class ukbaf_launchers(Crate):
	title = 'UKBAF CSW and Explosives'
 	base = 'CUP_RUSpecialWeaponsBox'
	weapons = [
		['rhs_mag_m67', 200],
		['rhs_mag_an_m8hc', 100],
		['rhs_mag_m18_purple', 100],
		['rhs_mag_m18_green', 100],
		['rhs_mag_m18_red', 100],
		['rhs_mag_m18_yellow', 100],
		['rhs_mine_M19_mag', 100],
		['SatchelCharge_Remote_Mag', 100],
		['DemoCharge_Remote_Mag', 100],

		['rhs_mag_M433_HEDP', 300],
		['rhs_mag_M585_white', 200],
		['rhs_mag_M661_green', 500],
		['rhs_mag_M662_red', 500],
		['rhs_mag_M713_red', 500],
		['rhs_mag_M714_white', 500],
		['rhs_mag_M715_green', 300],
		['rhs_mag_M716_yellow', 300],
	]
	backpacks = [
		['RHS_M2_MiniTripod_Bag', 10],
		['RHS_M2_Gun_Bag', 10],
		['RHS_Mk19_Tripod_Bag', 10],
		['RHS_Mk19_Gun_Bag', 10],
	]
	
class ukbaf_weapons(Crate):
	title = 'UKBAF Rifles and Ammo'
 	base = 'CUP_RUSpecialWeaponsBox'

	weapons = [
		['SMA_Mk17_EGLM', 5],
		['kio_l85a2_ris', 10],
		['kio_l85a2_ugl', 10],
		['STKR_L129A1_Bipod', 10],
		['rhs_weap_XM2010_wd', 2],		
	]
	
	magazines = [
		['rhsusf_5Rnd_300winmag_xm2010', 200],
		['SMA_20Rnd_762x51mm_M80A1_EPR', 800],
		['SMA_20Rnd_762x51mm_M80A1_EPR_Tracer', 500],
		['STKR_762x51_Mag', 500],
		['30rnd_556_magazine', 800],
		['rhsusf_20Rnd_762x51_m118_special_Mag', 500],
		['rhsusf_100Rnd_762x51', 500],
		['RH_12Rnd_45cal_usp', 100],
	]
	
	items = [
		['rhsusf_acc_LEUPOLDMK4_2', 2],
		['SMA_ELCAN_SPECTER_TAN', 10],
		['SMA_ELCAN_SPECTER', 10],
		['SMA_eotech552', 5],
		['rhsusf_acc_ACOG_USMC', 10],
	]
	
class ukbaf_launchers(Crate):
	title = 'UKBAF Launchers and Warheads'
	base = 'CUP_USBasicWeaponsBox'
	weapons = [
		['rhs_weap_fgm148', 20],
		['rhs_weap_M136', 400],
		['rhs_weap_M136_hedp', 400],
		['rhs_weap_M136_hp', 400],
	]
	magazines = [		
		['rhs_m136_mag', 400],
		['rhs_m136_hedp_mag', 400],
		['rhs_m136_hp_mag', 400],
		['rhs_fgm148_magazine_AT', 400],
	]

class ukbaf_radios(Crate):
	title = 'UKBAF Radios'
 	base = 'CUP_RUBasicAmmunitionBox'
	items = [
		['tf_anprc148jem', 50],
	]
	backpacks = [
		['tf_rt1523g_big_rhs', 10],
	]
