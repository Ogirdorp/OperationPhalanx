import base

class ukbaf_base(base.Base):
	class NoWrite: pass
	binoc = 'Binocular'
	headgear = 'STKR_MK7'
	items = base.Base.items + ['tf_pnr1000a']

	class HandGun:
		weapon = 'RH_usp'
		mags = [['RH_12Rnd_45cal_usp', 8]]

	class Uniform:
		type = 'STKR_UBACS'
		items = base.Base.Uniform.items + [
			['RH_12Rnd_45cal_usp', 2],
		]
	class Vest:
		type = 'STKR_Osprey_R'
		items = [
			['rhs_mag_m67', 2],
		]
	class Backpack:
		type = 'STKR_Predator'
		items = [
			['rhsusf_ANPVS_14', 1],
			['tf_anprc148jem', 1],
			['alive_tablet', 1],
			['rhs_googles_clear', 1],
		]

class ukbaf_leadscout(ukbaf_base):
	class Primary:
		weapon = 'SMA_Mk17'
		optic = 'SMA_ELCAN_SPECTER_TAN'
		rail = 'SMA_ANPEQ15_TOP_TAN_SCAR'
		mags = [
			['SMA_20Rnd_762x51mm_M80A1_EPR', 30],
		]
	class Vest(ukbaf_base.Vest):
		items = ukbaf_base.Vest.items + [
			['SMA_20Rnd_762x51mm_M80A1_EPR', 2],
		]
	class Backpack(ukbaf_base.Backpack):
		items = ukbaf_base.Backpack.items + [
			['SMA_20Rnd_762x51mm_M80A1_EPR', 2],
			['SMA_20Rnd_762x51mm_M80A1_EPR_Tracer', 2],
		]

class ukbaf_sl(ukbaf_leadscout):
	class Backpack(ukbaf_leadscout.Backpack):
		items = ukbaf_leadscout.Backpack.items + [
			['tf_anprc148jem', 1],
		]

class ukbaf_gunner(ukbaf_leadscout):
	class Primary:
		weapon = 'rhs_weap_m240B'
		mags = [
			['rhsusf_100Rnd_762x51', 100],
		]
	class Vest:
		type = 'STKR_Osprey_MG'
		items = ukbaf_leadscout.Vest.items + [
			['rhsusf_100Rnd_762x51', 1],
		]

	class Backpack(ukbaf_base.Backpack):
		items = ukbaf_base.Backpack.items + [
			['rhsusf_100Rnd_762x51', 1],
			['rhsusf_100Rnd_762x51_m993', 2],
		]

class ukbaf_combatmedic(ukbaf_leadscout):

	class Vest(ukbaf_leadscout.Vest):
		items = ukbaf_leadscout.Vest.items + [
			['rhs_mag_m18_green', 2],
		]
	class Backpack(ukbaf_base.Backpack):
		items = ukbaf_base.Backpack.items + base.MedicSupplies + [
			['SMA_20Rnd_762x51mm_M80A1_EPR', 3],
			['cse_personal_aid_kit', 3],
		]

class ukbaf_tl(ukbaf_leadscout):
	class Vest(ukbaf_leadscout):
		items = ukbaf_leadscout.Vest.items + [
			['tf_anprc148jem', 1],
		]

class ukbaf_signaller(ukbaf_leadscout):
	class Vest(ukbaf_leadscout.Vest):
		items = ukbaf_leadscout.Vest.items + [
			['tf_anprc148jem', 1],
		]
	class Backpack:
		type = 'STKR_PredatorBow'
		
		
class ukbaf_longrange(ukbaf_base):
	class Primary:
		weapon = 'rhs_weap_sr25'
		optic = 'rhsusf_acc_LEUPOLDMK4_2'
		mags = [
			['rhsusf_20Rnd_762x51_m118_special_Mag', 20],
		]
	class Vest(ukbaf_base.Vest):
		items = ukbaf_base.Vest.items + [
			['rhsusf_20Rnd_762x51_m118_special_Mag', 2],
		]
	class Backpack(ukbaf_base.Backpack):
		items = ukbaf_base.Backpack.items + [
			['rhsusf_20Rnd_762x51_m118_special_Mag', 4],
		]
