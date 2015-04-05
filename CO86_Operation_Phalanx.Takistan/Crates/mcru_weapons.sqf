/////////   MP Ammo Box script
/////////   By: Riouken
/////////   For Arma 3

if (! isServer) exitWith {};


_crate = _this select 0;




while {alive _crate} do
{


clearMagazineCargo _crate;
clearWeaponCargo _crate;
clearItemCargoGlobal _crate;
///NATO Weapons///


_crate addWeaponCargoGlobal ["rhs_weap_m240B", 15];
_crate addWeaponCargoGlobal ["rhs_m4_m320", 15];
_crate addWeaponCargoGlobal ["rhs_weap_m4_bipod", 15];
_crate addWeaponCargoGlobal ["rhs_weap_m16a4_grip", 20];
_crate addWeaponCargoGlobal ["rhs_weap_m16a4", 20];
_crate addWeaponCargoGlobal ["rhs_weap_m14ebrri", 5];
_crate addWeaponCargoGlobal ["rhs_weap_XM2010_wd", 2];
_crate addWeaponCargoGlobal ["rhs_weap_M590_5RD", 10];


///AMMO///


_crate addMagazineCargoGlobal ["rhsusf_100Rnd_762x51", 200];
_crate addMagazineCargoGlobal ["rhs_mag_30Rnd_556x45_Mk262_Stanag", 200];
_crate addMagazineCargoGlobal ["rhs_mag_30Rnd_556x45_M855A1_Stanag", 200];
_crate addMagazineCargoGlobal ["rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red", 200];
_crate addMagazineCargoGlobal ["rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Green", 200];
_crate addMagazineCargoGlobal ["rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Yellow", 200];
_crate addMagazineCargoGlobal ["rhsusf_20Rnd_762x51_m118_special_Mag", 100];
_crate addMagazineCargoGlobal ["rhsusf_5Rnd_300winmag_xm2010", 75];
_crate addMagazineCargoGlobal ["rhsusf_5Rnd_00Buck", 200];


/////Grenades////


_crate addMagazineCargoGlobal ["1Rnd_HE_Grenade_shell", 100];
_crate addMagazineCargoGlobal ["1Rnd_Smoke_Grenade_shell", 50];
_crate addMagazineCargoGlobal ["1Rnd_SmokeGreen_Grenade_shell", 50];
_crate addMagazineCargoGlobal ["1Rnd_SmokeYellow_Grenade_shell", 50];
_crate addMagazineCargoGlobal ["1Rnd_SmokePurple_Grenade_shell", 50];
_crate addMagazineCargoGlobal ["1Rnd_SmokeBlue_Grenade_shell", 50];
_crate addMagazineCargoGlobal ["1Rnd_SmokeOrange_Grenade_shell", 50];
_crate addMagazineCargoGlobal ["SmokeShellRed", 50];
_crate addMagazineCargoGlobal ["SmokeShell", 50];
_crate addMagazineCargoGlobal ["SmokeShellGreen", 50];
_crate addMagazineCargoGlobal ["SmokeShellYellow", 50];
_crate addMagazineCargoGlobal ["SmokeShellPurple", 50];
_crate addMagazineCargoGlobal ["SmokeShellBlue", 50];
_crate addMagazineCargoGlobal ["SmokeShellOrange", 50];


///Attachments///


//_crate addItemCargoGlobal ["Zasleh2",50]; 


////Items////


/////Items////


//_crate addItemCargoGlobal ["FirstAidKit", 50];



//sleep 500;
};