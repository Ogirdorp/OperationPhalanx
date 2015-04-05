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
* 1: MCRU CO
* 2: MCRU 2IC
* 3: MCRU RL
* 4: MCRU MG
* 5: MCRU EMT
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
	//MCRU CO
	case 1: 
	{
		//HINT "MCRU CO"; 
		//MAIN CONTAINERS
		_unit forceAddUniform "rhs_uniform_FROG01_wd";
			for "_i" from 1 to 2 do {_unit addItemToUniform "rhs_mag_9x19_17";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_tourniquet";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_bandageElastic";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_morphine";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_chestseal";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_quikclot";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_Keycuffs";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_earplugs_electronic";};
		_unit addHeadgear "rhsusf_mich_helmet_marpatwd_headset";
		
		//VEST
		_unit addVest "rhsusf_iotv_ocp_Squadleader";
			for "_i" from 1 to 5 do {_unit addItemToVest "rhs_mag_30Rnd_556x45_Mk318_Stanag";};
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
		_unit addWeapon "rhs_weap_m4";
		_unit addPrimaryWeaponItem "rhsusf_acc_ACOG";
		_unit addPrimaryWeaponItem "rhsusf_acc_anpeq15";
		_unit addWeapon "rhs_weap_pya";
		_unit addWeapon "lerca_1200_black";

		//ITEMS
		_unit linkItem "tf_anprc152_1";
		_unit linkItem "ItemGPS";

	};
	//MCRU 2IC
	case 2: 
	{
		//HINT "MCRU 2IC"; 
		//MAIN CONTAINERS
		_unit forceAddUniform "rhs_uniform_FROG01_wd";
			for "_i" from 1 to 2 do {_unit addItemToUniform "rhs_mag_9x19_17";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_tourniquet";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_bandageElastic";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_morphine";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_chestseal";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_quikclot";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_Keycuffs";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_earplugs_electronic";};
		_unit addHeadgear "rhsusf_mich_helmet_marpatwd_headset";
		
		//VEST
		_unit addVest "rhsusf_iotv_ocp_teamleader";
			for "_i" from 1 to 5 do {_unit addItemToVest "rhs_mag_30Rnd_556x45_Mk318_Stanag";};
			for "_i" from 1 to 2 do {_unit addItemToVest "rhs_mag_m67";};
			for "_i" from 1 to 2 do {_unit addItemToVest "cse_canteen";};
			for "_i" from 1 to 6 do {_unit addItemToVest "rhs_mag_M441_HE";};
			for "_i" from 1 to 1 do {_unit addItemToVest "cse_MRE_CreamTomatoSoup";};
			for "_i" from 1 to 1 do {_unit addItemToVest "Binocular";};
			for "_i" from 1 to 2 do {_unit addItemToVest "SmokeShell";};


		//BACKPACK
		_unit addBackpack "tf_rt1523g_big_bwmod";
			for "_i" from 1 to 1 do {_unit addItemToBackpack "rhs_googles_clear";};
		_unit addItemToBackpack "rhsusf_ANPVS_14";

		//WEAPONS
		_unit addWeapon "rhs_m4_m320";
		_unit addPrimaryWeaponItem "rhsusf_acc_ACOG";
		_unit addPrimaryWeaponItem "rhsusf_acc_anpeq15";
		_unit addWeapon "rhs_weap_pya";
		_unit addWeapon "lerca_1200_black";

		//ITEMS
		_unit linkItem "tf_anprc152_1";
		_unit linkItem "ItemGPS";

	};
	//MCRU RL
	case 3: 
	{
		//HINT "MCRU RL"; 
		//MAIN CONTAINERS
		_unit forceAddUniform "rhs_uniform_FROG01_wd";
			for "_i" from 1 to 2 do {_unit addItemToUniform "rhs_mag_9x19_17";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_tourniquet";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_bandageElastic";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_morphine";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_chestseal";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_quikclot";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_earplugs_electronic";};
		_unit addHeadgear "rhsusf_mich_helmet_marpatwd_headset";
		
		//VEST
		_unit addVest "rhsusf_iotv_ocp_rifleman";
			for "_i" from 1 to 5 do {_unit addItemToVest "rhs_mag_30Rnd_556x45_Mk318_Stanag";};
			for "_i" from 1 to 2 do {_unit addItemToVest "rhs_mag_m67";};
			for "_i" from 1 to 2 do {_unit addItemToVest "cse_canteen";};
			for "_i" from 1 to 1 do {_unit addItemToVest "cse_MRE_CreamTomatoSoup";};
			for "_i" from 1 to 1 do {_unit addItemToVest "Binocular";};
			for "_i" from 1 to 2 do {_unit addItemToVest "SmokeShell";};
		_unit addItemToVest "rhsusf_ANPVS_14";
		_unit addItemToVest "rhs_googles_clear";

		//BACKPACK

		//WEAPONS
		_unit addWeapon "rhs_weap_m16a4";
		_unit addPrimaryWeaponItem "rhsusf_acc_ACOG";
		_unit addPrimaryWeaponItem "rhsusf_acc_anpeq15";
		_unit addWeapon "rhs_weap_pya";

		//ITEMS
		_unit linkItem "tf_anprc152_1";
		_unit linkItem "ItemGPS";

	};
	//MCRU MG
	case 4: 
	{
		//HINT "MCRU MG"; 
		//MAIN CONTAINERS
		_unit forceAddUniform "rhs_uniform_FROG01_wd";
			for "_i" from 1 to 2 do {_unit addItemToUniform "rhs_mag_9x19_17";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_tourniquet";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_bandageElastic";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_morphine";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_chestseal";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_quikclot";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_earplugs_electronic";};
		_unit addHeadgear "rhsusf_mich_helmet_marpatwd_headset";
		
		//VEST
		_unit addVest "rhsusf_iotv_ocp_SAW";
			for "_i" from 1 to 2 do {_unit addItemToVest "rhs_mag_m67";};
			for "_i" from 1 to 2 do {_unit addItemToVest "cse_canteen";};
			for "_i" from 1 to 1 do {_unit addItemToVest "cse_MRE_CreamTomatoSoup";};
			for "_i" from 1 to 2 do {_unit addItemToVest "SmokeShell";};
		_unit addItemToVest "rhsusf_ANPVS_14";
		_unit addItemToVest "rhs_googles_clear";

		//BACKPACK
		_unit addBackpack "rhsusf_assault_eagleaiii_ocp";
			for "_i" from 1 to 3 do {_unit addItemToBackpack "rhsusf_100Rnd_556x45_soft_pouch";};

		//WEAPONS
		_unit addWeapon "rhs_weap_m249_pip";
		_unit addWeapon "rhs_weap_pya";

		//ITEMS
		_unit linkItem "tf_anprc152_1";
		_unit linkItem "ItemGPS";

	};
	//MCRU EMT
	case 5: 
	{
		//HINT "MCRU EMT"; 
		//MAIN CONTAINERS
		_unit forceAddUniform "rhs_uniform_FROG01_wd";
			for "_i" from 1 to 2 do {_unit addItemToUniform "rhs_mag_9x19_17";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_tourniquet";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_bandageElastic";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_morphine";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_chestseal";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_quikclot";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_earplugs_electronic";};
		_unit addHeadgear "rhsusf_mich_helmet_marpatwd_headset";
		
		//VEST
		_unit addVest "rhsusf_iotv_ocp_rifleman";
			for "_i" from 1 to 5 do {_unit addItemToVest "rhs_mag_30Rnd_556x45_Mk318_Stanag";};
			for "_i" from 1 to 2 do {_unit addItemToVest "rhs_mag_m67";};
			for "_i" from 1 to 2 do {_unit addItemToVest "cse_canteen";};
			for "_i" from 1 to 1 do {_unit addItemToVest "cse_MRE_CreamTomatoSoup";};
			for "_i" from 1 to 1 do {_unit addItemToVest "Binocular";};
			for "_i" from 1 to 2 do {_unit addItemToVest "SmokeShell";};
		_unit addItemToVest "rhsusf_ANPVS_14";
		_unit addItemToVest "rhs_googles_clear";

		//BACKPACK
		_unit addBackpack "rhsusf_assault_eagleaiii_ocp";
			for "_i" from 1 to 4 do {_unit addItemToBackpack "cse_epinephrine";};

		//WEAPONS
		_unit addWeapon "rhs_weap_m16a4";
		_unit addPrimaryWeaponItem "rhsusf_acc_ACOG";
		_unit addPrimaryWeaponItem "rhsusf_acc_anpeq15";
		_unit addWeapon "rhs_weap_pya";

		//ITEMS
		_unit linkItem "tf_anprc152_1";
		_unit linkItem "ItemGPS";

	};
	default {hint "Script Error, Variable does not exist"}; 
};