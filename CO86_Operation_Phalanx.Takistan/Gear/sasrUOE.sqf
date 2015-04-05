/*
* For loading custom loadouts | Modified by Ogirdor
* You may change/edit all settings
*
*
* in the unit init line put
* null = [this,"role"] execVM "scriptname.sqf"; 
* For RESPAWN add this;
* this addeventhandler ["respawn","[_this select 0,CASE NUMBER] execVM 'scriptname.sqf'"];
* Switch out role with a number depending on what role you want, remove ""
*
* 
* 1: SASR CO
* 2: SASR 2IC
* 3: SASR RL
* 4: SASR MG
* 5: SASR EMT
*/

//Defines Variables
waitUntil {!isNull player};  //Prevent MP / JIP issues

_unit = _this select 0;
_role = _this select 1;


//Pre-Removal and Additions
removeallweapons _unit;
removeAllAssignedItems _unit;
removeBackpack _unit;
removeVest _unit;
removeUniform _unit;
removeHeadGear _unit;
_unit addWeapon "ItemMap";
_unit addWeapon "ItemCompass";
//_unit addItem "NVGoggles";


//Switch hands out weapons and equipment based on role
switch (_role) do 
{ 
	//SASR CO
	case 1: 
	{
		//HINT "SASR CO"; 
		//MAIN CONTAINERS
		_unit forceAddUniform "rhs_uniform_FROG01_m81";
			for "_i" from 1 to 2 do {_unit addItemToUniform "16Rnd_9x21_Mag";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_tourniquet";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_bandageElastic";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_morphine";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_chestseal";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_quikclot";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_Keycuffs";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_earplugs_electronic";};
		_unit addHeadgear "ffaa_moe_casco_02_1_b";
		_unit addGoggles "G_Balaclava_blk";
		
		//VEST
		_unit addVest "ffaa_et_moe_peco_02_b";
			for "_i" from 1 to 5 do {_unit addItemToVest "hlc_30Rnd_9x19_B_MP5";};
			for "_i" from 1 to 2 do {_unit addItemToVest "rhs_mag_m67";};
			for "_i" from 1 to 2 do {_unit addItemToVest "cse_canteen";};
			for "_i" from 1 to 1 do {_unit addItemToVest "cse_personal_aid_kit";};
			for "_i" from 1 to 1 do {_unit addItemToVest "cse_MRE_CreamTomatoSoup";};
			for "_i" from 1 to 1 do {_unit addItemToVest "Binocular";};
			for "_i" from 1 to 2 do {_unit addItemToVest "SmokeShell";};


		//BACKPACK
		_unit addBackpack "tf_rt1523g_big_bwmod";
			for "_i" from 1 to 1 do {_unit addItemToBackpack "rhs_googles_clear";};
		_unit addItemToBackpack "rhsusf_ANPVS_14";

		//WEAPONS
		_unit addWeapon "hlc_smg_mp5n";
		_unit addPrimaryWeaponItem "hlc_muzzle_Tundra";
		_unit addPrimaryWeaponItem "SMA_ANPEQ15_BLK";
		_unit addPrimaryWeaponItem "SMA_AIMPOINT";
		_unit addWeapon "ffaa_armas_usp";
		_unit addHandgunItem "muzzle_snds_L";
		_unit addWeapon "lerca_1200_black";

		//ITEMS
		_unit linkItem "tf_anprc152_1";
		_unit linkItem "ItemGPS";
	};
	//SASR 2IC
	case 2: 
	{
		//HINT "SASR 2IC"; 
		//MAIN CONTAINERS
		_unit forceAddUniform "rhs_uniform_FROG01_m81";
			for "_i" from 1 to 2 do {_unit addItemToUniform "16Rnd_9x21_Mag";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_tourniquet";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_bandageElastic";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_morphine";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_chestseal";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_quikclot";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_Keycuffs";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_earplugs_electronic";};
		_unit addHeadgear "ffaa_moe_casco_02_1_b";
		_unit addGoggles "G_Balaclava_blk";
		
		//VEST
		_unit addVest "ffaa_et_moe_peco_02_b";
			for "_i" from 1 to 5 do {_unit addItemToVest "hlc_30Rnd_9x19_B_MP5";};
			for "_i" from 1 to 2 do {_unit addItemToVest "rhs_mag_m67";};
			for "_i" from 1 to 2 do {_unit addItemToVest "cse_canteen";};
			for "_i" from 1 to 6 do {_unit addItemToVest "1Rnd_HE_Grenade_shell";};
			for "_i" from 1 to 1 do {_unit addItemToVest "cse_MRE_CreamTomatoSoup";};
			for "_i" from 1 to 1 do {_unit addItemToVest "Binocular";};
			for "_i" from 1 to 2 do {_unit addItemToVest "SmokeShell";};


		//BACKPACK
		_unit addBackpack "tf_rt1523g_big_bwmod";
			for "_i" from 1 to 1 do {_unit addItemToBackpack "rhs_googles_clear";};
		_unit addItemToBackpack "rhsusf_ANPVS_14";

		//WEAPONS
		_unit addWeapon "hlc_smg_9mmar";
		_unit addPrimaryWeaponItem "hlc_muzzle_Tundra";
		_unit addPrimaryWeaponItem "SMA_ANPEQ15_BLK";
		_unit addPrimaryWeaponItem "SMA_AIMPOINT_GLARE";
		_unit addWeapon "ffaa_armas_usp";
		_unit addHandgunItem "muzzle_snds_L";

		//ITEMS
		_unit linkItem "tf_anprc152_1";
		_unit linkItem "ItemGPS";
	};
	//SASR TROOPER
	case 3: 
	{
		//HINT "SASR TROOPER"; 
		//MAIN CONTAINERS
		_unit forceAddUniform "rhs_uniform_FROG01_m81";
			for "_i" from 1 to 2 do {_unit addItemToUniform "16Rnd_9x21_Mag";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_tourniquet";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_bandageElastic";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_morphine";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_chestseal";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_quikclot";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_Keycuffs";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_earplugs_electronic";};
		_unit addHeadgear "ffaa_moe_casco_02_1_b";
		_unit addGoggles "G_Balaclava_blk";
		
		//VEST
		_unit addVest "ffaa_et_moe_peco_02_b";
			for "_i" from 1 to 5 do {_unit addItemToVest "hlc_20rnd_762x51_b_G3";};
			for "_i" from 1 to 2 do {_unit addItemToVest "rhs_mag_m67";};
			for "_i" from 1 to 2 do {_unit addItemToVest "cse_canteen";};
			for "_i" from 1 to 1 do {_unit addItemToVest "cse_MRE_CreamTomatoSoup";};
			for "_i" from 1 to 1 do {_unit addItemToVest "Binocular";};
			for "_i" from 1 to 2 do {_unit addItemToVest "SmokeShell";};


		//BACKPACK
		_unit addBackpack "rhsusf_assault_eagleaiii_ocp";
			for "_i" from 1 to 1 do {_unit addItemToBackpack "rhs_googles_clear";};
		_unit addItemToBackpack "rhsusf_ANPVS_14";

		//WEAPONS
		_unit addWeapon "hlc_rifle_g3ka4";
		_unit addPrimaryWeaponItem "hlc_muzzle_snds_g3";
		_unit addPrimaryWeaponItem "SMA_ANPEQ15_BLK";
		_unit addPrimaryWeaponItem "SMA_eotech552_kf";
		_unit addWeapon "ffaa_armas_usp";
		_unit addHandgunItem "muzzle_snds_L";

		//ITEMS
		_unit linkItem "tf_anprc152_1";
		_unit linkItem "ItemGPS";
	};
	default {hint "Script Error, Variable does not exist"}; 
};