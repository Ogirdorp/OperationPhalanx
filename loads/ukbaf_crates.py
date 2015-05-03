from p4a.loadout import Crate
 
class ukbaf_launchers(Crate):
	title = 'UKBAF CSW and Explosives'
 	base = 'Box_FIA_Wps_F'
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
 	base = 'Box_FIA_Wps_F'

	weapons = [
		['UK3CB_BAF_L7A2', 8],
		['UK3CB_BAF_L85A2_UGL', 10],
		['UK3CB_BAF_L86A2', 10],
		['UK3CB_BAF_L129A1_AFG', 10],
		['UK3CB_BAF_L115A3_Desert_Ghillie', 2],		
	]
	
	magazines = [
		['UK3CB_BAF_75Rnd', 200],
		['UK3CB_BAF_75Rnd_T', 200],
		['UK3CB_BAF_200Rnd', 300],
		['UK3CB_BAF_200Rnd_T', 300],
		['UK3CB_BAF_30Rnd', 600],
		['UK3CB_BAF_30Rnd_T', 600],
		['UK3CB_BAF_L115A3_Mag', 200],
		['UK3CB_BAF_20Rnd', 300],
		['UK3CB_BAF_20Rnd_T', 300],
		['UK3CB_BAF_100Rnd', 300],
		['UK3CB_BAF_100Rnd_T', 300],
	]
	
	items = [
		['UK3CB_BAF_TA31F', 2],
		['UK3CB_BAF_SUSAT', 10],
		['UK3CB_BAF_SpecterLDS_Dot', 10],
		['UK3CB_BAF_SpecterLDS', 10],
		['UK3CB_BAF_LLM_IR', 10],
		['UK3CB_BAF_L85_Silencer', 20],
	]
	
class ukbaf_launchers(Crate):
	title = 'UKBAF Launchers and Warheads'
	base = 'Box_FIA_Wps_F'
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
 	base = 'Box_FIA_Wps_F'
	items = [
		['tf_anprc148jem', 50],
	]
	backpacks = [
		['tf_rt1523g_big_rhs', 10],
	]
