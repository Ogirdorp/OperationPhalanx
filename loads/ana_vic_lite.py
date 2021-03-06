from p4a.loadout import Crate

class cdf_vic_lite(Crate):
	vehicle = True
	def __init__(self):
		super(cdf_vic_lite, self).__init__()
		self.remove('all')	
	weapons = [
		['ACE_HandFlare_White', 2],
		['ACE_HandFlare_Red', 2],
	]
	magazines = [
		['ACE_HandFlare_White', 2],
		['ACE_HandFlare_Red', 2],
		['rhs_mag_30Rnd_556x45_Mk318_Stanag', 5],
		['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 5],
		['rhsusf_100Rnd_556x45_soft_pouch', 2],
		['rhs_mag_an_m8hc', 2],
		['rhs_mag_m18_red', 2],
		['rhs_mag_m67', 4],
	]
	items = [
		['ACE_bandage_basic', 10],
		['ACE_bandageElastic', 5],
		['ACE_morphine', 2],
		['ACE_epinephrine', 2],
		['ACE_saline_iv', 1],
		['ACE_saline_iv_500', 2],
		['ACE_saline_iv_250', 2],
		['ACE_tourniquet', 2],	
	]