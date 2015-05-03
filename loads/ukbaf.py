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
		weapon = 'UK3CB_BAF_L85A2'
		optic = 'UK3CB_BAF_SpecterLDS_Dot'
		suppressor = 'UK3CB_BAF_sffh'
		rail = 'UK3CB_BAF_LLM_Flashlight'
		mags = [
			['UK3CB_BAF_30Rnd', 30],
		]
	class Vest(ukbaf_base.Vest):
		items = ukbaf_base.Vest.items + [
			['UK3CB_BAF_30Rnd_T', 2],
		]
	class Backpack(ukbaf_base.Backpack):
		items = ukbaf_base.Backpack.items + [
			['UK3CB_BAF_30Rnd', 2],
			['UK3CB_BAF_30Rnd_T', 2],
		]

class ukbaf_sl(ukbaf_leadscout):
	class Backpack(ukbaf_leadscout.Backpack):
		items = ukbaf_leadscout.Backpack.items + [
			['tf_anprc148jem', 1],
		]

class ukbaf_gunner(ukbaf_leadscout):
	class Primary:
		weapon = 'UK3CB_BAF_L110A1'
		rail = 'rhsusf_acc_ELCAN'
		mags = [
			['UK3CB_BAF_100Rnd', 100],
		]
	class Vest:
		type = 'STKR_Osprey_MG'
		items = ukbaf_leadscout.Vest.items + [
			['UK3CB_BAF_100Rnd', 1],
		]

	class Backpack(ukbaf_base.Backpack):
		items = ukbaf_base.Backpack.items + [
			['UK3CB_BAF_100Rnd', 1],
			['UK3CB_BAF_100Rnd_T', 2],
		]

class ukbaf_combatmedic(ukbaf_leadscout):

	class Vest(ukbaf_leadscout.Vest):
		items = ukbaf_leadscout.Vest.items + [
			['rhs_mag_m18_green', 2],
		]
	class Backpack(ukbaf_base.Backpack):
		items = ukbaf_base.Backpack.items + base.MedicSupplies + [
			['UK3CB_BAF_L85A2', 3],
			['ACE_personal_aid_kit', 3],
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
		optic = 'UK3CB_BAF_L86A3'
		mags = [
			['UK3CB_BAF_30Rnd', 20],
		]
	class Vest(ukbaf_base.Vest):
		items = ukbaf_base.Vest.items + [
			['UK3CB_BAF_30Rnd', 2],
		]
	class Backpack(ukbaf_base.Backpack):
		items = ukbaf_base.Backpack.items + [
			['UK3CB_BAF_30Rnd', 4],
		]
