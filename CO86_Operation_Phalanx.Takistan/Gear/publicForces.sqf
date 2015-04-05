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
* 1: Public Forces PL
* 2: Public Forces 2IC
* 3: Public Forces Soldado
* 4: Public Forces MG1
* 5: Public Forces EMT
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
	//Public Forces PL
	case 1: 
	{
		//HINT "Public Forces PL"; 
		//MAIN CONTAINERS
		_unit forceAddUniform "ffaa_brilat_CombatUniform_item_b";
			for "_i" from 1 to 2 do {_unit addItemToUniform "16Rnd_9x21_Mag";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_tourniquet";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_bandageElastic";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_morphine";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_chestseal";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_quikclot";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_Keycuffs";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_earplugs_electronic";};
		_unit addHeadgear "ffaa_brilat_casco_b";
		
		//VEST
		_unit addVest "ffaa_brilat_chaleco_01_bs";
			for "_i" from 1 to 5 do {_unit addItemToVest "ffaa_556x45_g36";};
			for "_i" from 1 to 2 do {_unit addItemToVest "rhs_mag_m67";};
			for "_i" from 1 to 2 do {_unit addItemToVest "cse_canteen";};
			for "_i" from 1 to 1 do {_unit addItemToVest "cse_personal_aid_kit";};
			for "_i" from 1 to 1 do {_unit addItemToVest "cse_MRE_MeatballsPasta";};
			for "_i" from 1 to 1 do {_unit addItemToVest "Binocular";};
			for "_i" from 1 to 2 do {_unit addItemToVest "SmokeShell";};


		//BACKPACK
		_unit addBackpack "tf_rt1523g_big_bwmod";
			for "_i" from 1 to 1 do {_unit addItemToBackpack "rhs_googles_clear";};
		_unit addItemToBackpack "ffaa_nvgoggles";

		//WEAPONS
		_unit addWeapon "ffaa_armas_hkg36k";
		_unit addPrimaryWeaponItem "ffaa_optic_g36_holo";
		_unit addWeapon "ffaa_armas_usp";

		//ITEMS
		_unit linkItem "tf_anprc152_1";
		_unit linkItem "ItemGPS";

	};
	//Public Forces 2IC
	case 2: 
	{
		//HINT "Public Forces 2IC"; 
		//MAIN CONTAINERS
		_unit forceAddUniform "ffaa_brilat_CombatUniform_item_b";
			for "_i" from 1 to 2 do {_unit addItemToUniform "16Rnd_9x21_Mag";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_tourniquet";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_bandageElastic";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_morphine";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_chestseal";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_quikclot";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_Keycuffs";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_earplugs_electronic";};
		_unit addHeadgear "ffaa_brilat_casco_b";
		
		//VEST
		_unit addVest "tf_rt1523g_big_bwmod";
			for "_i" from 1 to 5 do {_unit addItemToVest "ffaa_556x45_g36";};
			for "_i" from 1 to 2 do {_unit addItemToVest "rhs_mag_m67";};
			for "_i" from 1 to 2 do {_unit addItemToVest "cse_canteen";};
			for "_i" from 1 to 1 do {_unit addItemToVest "cse_personal_aid_kit";};
			for "_i" from 1 to 1 do {_unit addItemToVest "cse_MRE_MeatballsPasta";};
			for "_i" from 1 to 1 do {_unit addItemToVest "Binocular";};
			for "_i" from 1 to 2 do {_unit addItemToVest "SmokeShell";};


		//BACKPACK
		_unit addBackpack "ffaa_brilat_mochila_boscoso";
			for "_i" from 1 to 1 do {_unit addItemToBackpack "rhs_googles_clear";};
		_unit addItemToBackpack "ffaa_nvgoggles";

		//WEAPONS
		_unit addWeapon "ffaa_armas_hkag36k";
		_unit addPrimaryWeaponItem "ffaa_optic_g36_holo";
		_unit addWeapon "ffaa_armas_usp";

		//ITEMS
		_unit linkItem "tf_anprc152_1";
		_unit linkItem "ItemGPS";

	};
	//Public Forces Soldado
	case 3: 
	{
		//HINT "Public Forces Soldado"; 
		//MAIN CONTAINERS
		_unit forceAddUniform "ffaa_brilat_CombatUniform_item_b";
			for "_i" from 1 to 2 do {_unit addItemToUniform "16Rnd_9x21_Mag";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_tourniquet";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_bandageElastic";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_morphine";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_chestseal";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_quikclot";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_earplugs_electronic";};
		_unit addHeadgear "ffaa_brilat_casco_b";
		
		//VEST
		_unit addVest "ffaa_brilat_chaleco_02_bs";
			for "_i" from 1 to 5 do {_unit addItemToVest "ffaa_556x45_g36";};
			for "_i" from 1 to 2 do {_unit addItemToVest "rhs_mag_m67";};
			for "_i" from 1 to 2 do {_unit addItemToVest "cse_canteen";};
			for "_i" from 1 to 1 do {_unit addItemToVest "cse_personal_aid_kit";};
			for "_i" from 1 to 1 do {_unit addItemToVest "cse_MRE_MeatballsPasta";};
			for "_i" from 1 to 2 do {_unit addItemToVest "SmokeShell";};


		//BACKPACK
		_unit addBackpack "ffaa_brilat_mochila_boscoso";
			for "_i" from 1 to 1 do {_unit addItemToBackpack "rhs_googles_clear";};
		_unit addItemToBackpack "ffaa_nvgoggles";

		//WEAPONS
		_unit addWeapon "ffaa_armas_hkg36e";
		_unit addPrimaryWeaponItem "ffaa_optic_g36_holo";
		_unit addWeapon "ffaa_armas_usp";

		//ITEMS
		_unit linkItem "tf_anprc152_1";
		_unit linkItem "ItemGPS";

	};
	//Public Forces MG1
	case 4: 
	{
		//HINT "Public Forces Ameli"; 
		//MAIN CONTAINERS
		_unit forceAddUniform "ffaa_brilat_CombatUniform_item_b";
			for "_i" from 1 to 2 do {_unit addItemToUniform "16Rnd_9x21_Mag";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_tourniquet";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_bandageElastic";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_morphine";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_chestseal";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_quikclot";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_earplugs_electronic";};
		_unit addHeadgear "ffaa_brilat_casco_b";
		
		//VEST
		_unit addVest "ffaa_brilat_chaleco_01_bs";
			for "_i" from 1 to 2 do {_unit addItemToVest "ffaa_556x45_ameli";};
			for "_i" from 1 to 2 do {_unit addItemToVest "rhs_mag_m67";};
			for "_i" from 1 to 2 do {_unit addItemToVest "cse_canteen";};
			for "_i" from 1 to 1 do {_unit addItemToVest "cse_personal_aid_kit";};
			for "_i" from 1 to 1 do {_unit addItemToVest "cse_MRE_MeatballsPasta";};
			for "_i" from 1 to 2 do {_unit addItemToVest "SmokeShell";};


		//BACKPACK
		_unit addBackpack "ffaa_brilat_mochila_boscoso";
			for "_i" from 1 to 1 do {_unit addItemToBackpack "rhs_googles_clear";};
			for "_i" from 1 to 2 do {_unit addItemToBackpack "ffaa_556x45_ameli";};
		_unit addItemToBackpack "ffaa_nvgoggles";

		//WEAPONS
		_unit addWeapon "ffaa_armas_ameli";
		_unit addWeapon "ffaa_armas_usp";

		//ITEMS
		_unit linkItem "tf_anprc152_1";
		_unit linkItem "ItemGPS";

	};
	//Public Forces EMT
	case 5: 
	{
		//HINT "Public Forces EMT"; 
		//MAIN CONTAINERS
		_unit forceAddUniform "ffaa_brilat_CombatUniform_item_b";
			for "_i" from 1 to 2 do {_unit addItemToUniform "16Rnd_9x21_Mag";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_tourniquet";};
			for "_i" from 1 to 4 do {_unit addItemToUniform "cse_bandageElastic";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_morphine";};
			for "_i" from 1 to 2 do {_unit addItemToUniform "cse_chestseal";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_quikclot";};
			for "_i" from 1 to 1 do {_unit addItemToUniform "cse_earplugs_electronic";};
		_unit addHeadgear "ffaa_brilat_casco_b";
		
		//VEST
		_unit addVest "ffaa_brilat_chaleco_03_bs";
			for "_i" from 1 to 4 do {_unit addItemToVest "ffaa_556x45_g36";};
			for "_i" from 1 to 2 do {_unit addItemToVest "rhs_mag_m67";};
			for "_i" from 1 to 2 do {_unit addItemToVest "cse_canteen";};
			for "_i" from 1 to 1 do {_unit addItemToVest "cse_personal_aid_kit";};
			for "_i" from 1 to 1 do {_unit addItemToVest "cse_MRE_MeatballsPasta";};
			for "_i" from 1 to 2 do {_unit addItemToVest "SmokeShell";};

		//BACKPACK
		_unit addBackpack "ffaa_brilat_mochila_viaje_boscoso";
			for "_i" from 1 to 1 do {_unit addItemToBackpack "rhs_googles_clear";};
			for "_i" from 1 to 2 do {_unit addItemToBackpack "ffaa_556x45_g36";};
			for "_i" from 1 to 4 do {_unit addItemToBackpack "cse_epinephrine";};
		_unit addItemToBackpack "ffaa_nvgoggles";

		//WEAPONS
		_unit addWeapon "ffaa_armas_hkg36k";
		_unit addWeapon "ffaa_armas_usp";

		//ITEMS
		_unit linkItem "tf_anprc152_1";
		_unit linkItem "ItemGPS";

	};
	default {hint "Script Error, Variable does not exist"}; 
};