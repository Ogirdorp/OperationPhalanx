/*
*
* Arsenal Restriction Script
* Place this in your init
* 
*
* Put in box init: null = [this] execVM "folder\nameyourscript.sqf"
*/

//INIT
_crate = _this select 0;
["AmmoboxInit",[_crate,false,{true}]] spawn BIS_fnc_arsenal;


//LIST OF ITEMS TO INCLUDE
_availableWeapons = [
	"ffaa_armas_hkg36e_base",
	"ffaa_armas_hkg36k",
	"ffaa_armas_hkag36e",
	"ffaa_armas_hkag36k",
	"ffaa_armas_hkg36e_tir",
	"ffaa_armas_hkg36k_tir",
	"ffaa_armas_mg4_poin",
	"ffaa_armas_mg3",
	"ffaa_armas_ameli",
	"ffaa_armas_usp"
];

_availableMagazines = [
	"ffaa_556x45_g36",
	"rhs_mag_m67",
	"ffaa_556x45_ameli"
];

_availableWeaponItems = [
	"rhsusf_acc_ACOG",
	"ffaa_optic_g36_holo"
];


[_crate,((weaponCargo _crate) + _availableWeapons)] call BIS_fnc_addVirtualWeaponCargo;
//[_crate,((itemCargo _crate) + _availableWeaponItems)] call BIS_fnc_addVirtualItemCargo;
[_crate,((magazineCargo _crate) + _availableMagazines)] call BIS_fnc_addVirtualMagazineCargo;
//Populate with predefined items and whatever is already in the crate
//[_crate,((backpackCargo _crate) + _availableBackpacks)] call BIS_fnc_addVirtualBackpackCargo;
//[_crate,(magazineCargo _crate)] call BIS_fnc_addVirtualMagazineCargo;
//[_crate,((weaponCargo _crate) + _availableWeapons)] call BIS_fnc_addVirtualWeaponCargo;

// <--- This means comment. If you wish to use the other fnc just delete the forward slashes