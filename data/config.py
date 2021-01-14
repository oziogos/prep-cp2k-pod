
from data.blocks import *
from src.utils import *

#--------------------------------------------------------------------

# coordinates dictionaries: keys correspond to xyz file paths;
# values hold descriptive comments

pyrene={
    'data/dimers/pyrene_cofacial_3.5A.xyz':'cofacial_3.5A',
    'data/dimers/pyrene_coplanar.xyz':'coplanar',
}

pyrene_Ac2={
    'data/dimers/pyrene_Ac2_cofacial_3.5A.xyz':'cofacial_3.5A',
    'data/dimers/pyrene_Ac2_coplanar.xyz':'coplanar',
}

pyrene_db={
    'data/dimers/pyrene_dumbbell_000deg.xyz':'rotated_0deg',
    'data/dimers/pyrene_dumbbell_005deg.xyz':'rotated_5deg',
    'data/dimers/pyrene_dumbbell_010deg.xyz':'rotated_10deg',
    'data/dimers/pyrene_dumbbell_015deg.xyz':'rotated_15deg',
    'data/dimers/pyrene_dumbbell_020deg.xyz':'rotated_20deg',
    'data/dimers/pyrene_dumbbell_025deg.xyz':'rotated_25deg',
    'data/dimers/pyrene_dumbbell_030deg.xyz':'rotated_30deg',
    'data/dimers/pyrene_dumbbell_035deg.xyz':'rotated_35deg',
    'data/dimers/pyrene_dumbbell_040deg.xyz':'rotated_40deg',
    'data/dimers/pyrene_dumbbell_045deg.xyz':'rotated_45deg',
    'data/dimers/pyrene_dumbbell_090deg.xyz':'rotated_90deg',
}

anthracene={
    'data/dimers/3cene_3.5A.xyz':'cofacial_3.5A',
    'data/dimers/3cene_4.0A.xyz':'cofacial_4.0A',
    'data/dimers/3cene_4.5A.xyz':'cofacial_4.5A',
    'data/dimers/3cene_5.0A.xyz':'cofacial_5.0A',
    'data/dimers/1.xyz':'random_1',
    'data/dimers/2.xyz':'random_2',
    'data/dimers/3.xyz':'random_3',
    'data/dimers/4.xyz':'random_4',
    'data/dimers/5.xyz':'random_5',
}
tetracene={
    'data/dimers/4cene_3.5A.xyz':'cofacial_3.5A',
    'data/dimers/4cene_4.0A.xyz':'cofacial_4.0A',
    'data/dimers/4cene_4.5A.xyz':'cofacial_4.5A',
    'data/dimers/4cene_5.0A.xyz':'cofacial_5.0A',
}
pentacene={
    'data/dimers/5cene_3.5A.xyz':'cofacial_3.5A',
    'data/dimers/5cene_4.0A.xyz':'cofacial_4.0A',
    'data/dimers/5cene_4.5A.xyz':'cofacial_4.5A',
    'data/dimers/5cene_5.0A.xyz':'cofacial_5.0A',
}
perylene={
    'data/dimers/perylene_3.5A.xyz':'cofacial_3.5A',
    'data/dimers/perylene_4.0A.xyz':'cofacial_4.0A',
    'data/dimers/perylene_4.5A.xyz':'cofacial_4.5A',
    'data/dimers/perylene_5.0A.xyz':'cofacial_5.0A',
}
anthraceneF={
    'data/dimers/anthraceneF_3.5A.xyz':'cofacial_3.5A',
    'data/dimers/anthraceneF_4.0A.xyz':'cofacial_4.0A',
    'data/dimers/anthraceneF_4.5A.xyz':'cofacial_4.5A',
    'data/dimers/anthraceneF_5.0A.xyz':'cofacial_5.0A',
}
perylene_diimide={
    'data/dimers/perylene_diimide_3.5A.xyz':'cofacial_3.5A',
    'data/dimers/perylene_diimide_4.0A.xyz':'cofacial_4.0A',
    'data/dimers/perylene_diimide_4.5A.xyz':'cofacial_4.5A',
    'data/dimers/perylene_diimide_5.0A.xyz':'cofacial_5.0A',
}
porphyrin={
    'data/dimers/porph_3.5A.xyz':'cofacial_3.5A',
    'data/dimers/porph_4.0A.xyz':'cofacial_4.0A',
    'data/dimers/porph_4.5A.xyz':'cofacial_4.5A',
    'data/dimers/porph_5.0A.xyz':'cofacial_5.0A',
}

#--------------------------------------------------------------------

# dataset dictionaries

pyrene_dataset={
    'pyrene_neutral':{
        'src':pyrene,
        'atoms':[26,26],
        'electrons':[74,74],
    },
    'pyrene_Ac2_neutral':{
        'src':pyrene_Ac2,
        'atoms':[34,34],
        'electrons':[106,106],
    },
    'pyrene_db_neutral':{
        'src':pyrene_db,
        'atoms':[33,33],
        'electrons':[105,105],
    },
}

HAB7minus={
    'anthracene_charged':{
        'src':anthracene,
        'atoms':[24,24],
        'electrons':[66,66],
        '__FORCE_EVAL__DFT__CHARGE__':-1,
        '__FORCE_EVAL__DFT__SPIN_POLARIZED__':'.true.',
        '__FORCE_EVAL__DFT__MULTIPLICITY__':2,
    },
    'anthracene_neutral':{
        'src':anthracene,
        'atoms':[24,24],
        'electrons':[66,66],
        '__FORCE_EVAL__DFT__CHARGE__':0,
        '__FORCE_EVAL__DFT__SPIN_POLARIZED__':'.true.',
        '__FORCE_EVAL__DFT__MULTIPLICITY__':1,
    },
    'tetracene_neutral':{
        'src':tetracene,
        'atoms':[30,30],
        'electrons':[84,84],
    },
    'pentacene_neutral':{
        'src':pentacene,
        'atoms':[36,36],
        'electrons':[102,102],
    },
    'perylene_neutral':{
        'src':perylene,
        'atoms':[32,32],
        'electrons':[92,92],
    },
    'anthraceneF_neutral':{
        'src':anthraceneF,
        'atoms':[24,24],
        'electrons':[126,126],
    },
    'perylene_diimide_neutral':{
        'src':perylene_diimide,
        'atoms':[40,40],
        'electrons':[140,140],
    },
    'porphyrin_neutral':{
        'src':porphyrin,
        'atoms':[38,38],
        'electrons':[114,114],
    },
}

#--------------------------------------------------------------------

# theory dictionary

driver={
    'PBE-GTH':{
        
        'template':'templates/dft_spin_pod.txt',
        
        '__FORCE_EVAL__DFT__BASIS_SET_FILE_NAME__':'GTH_BASIS_SETS',
        '__FORCE_EVAL__DFT__POTENTIAL_FILE_NAME__':'POTENTIAL',
        '__FORCE_EVAL__DFT__MGRID__CUTOFF__':450.0,
        '__FORCE_EVAL__DFT__MGRID__REL_CUTOFF__':75.0,
        '__FORCE_EVAL__DFT__SCF__MAX_SCF__':1000,
        '__FORCE_EVAL__DFT__SCF__SCF_GUESS__':'atomic',
        '__FORCE_EVAL__DFT__POISSON__':blocks['POISSON_MT'],
        '__FORCE_EVAL__DFT__QS__':blocks['QS_GGA'],
        '__FORCE_EVAL__DFT__SCF__':blocks['SCF_OT_CG'],
        '__FORCE_EVAL__DFT__XC__':blocks['XC_PBE'],
        
    },
    
    'PBE0-GTH':{
        
        'template':'templates/dft_spin_pod.txt',
        
        '__FORCE_EVAL__DFT__BASIS_SET_FILE_NAME__':'GTH_BASIS_SETS',
        '__FORCE_EVAL__DFT__POTENTIAL_FILE_NAME__':'POTENTIAL',
        '__FORCE_EVAL__DFT__MGRID__CUTOFF__':450.0,
        '__FORCE_EVAL__DFT__MGRID__REL_CUTOFF__':75.0,
        '__FORCE_EVAL__DFT__SCF__MAX_SCF__':1000,
        '__FORCE_EVAL__DFT__SCF__SCF_GUESS__':'restart',
        '__FORCE_EVAL__DFT__POISSON__':blocks['POISSON_MT'],
        '__FORCE_EVAL__DFT__QS__':blocks['QS_HFX'],
        '__FORCE_EVAL__DFT__SCF__':blocks['SCF_OT_CG'],
        '__FORCE_EVAL__DFT__XC__':blocks['XC_PBE0'],
        
    },
    
    'HSE06-GTH':{
        
        'template':'templates/dft_spin_pod.txt',
        
        '__FORCE_EVAL__DFT__BASIS_SET_FILE_NAME__':'GTH_BASIS_SETS',
        '__FORCE_EVAL__DFT__POTENTIAL_FILE_NAME__':'POTENTIAL',
        '__FORCE_EVAL__DFT__MGRID__CUTOFF__':450.0,
        '__FORCE_EVAL__DFT__MGRID__REL_CUTOFF__':75.0,
        '__FORCE_EVAL__DFT__SCF__MAX_SCF__':1000,
        '__FORCE_EVAL__DFT__SCF__SCF_GUESS__':'restart',
        '__FORCE_EVAL__DFT__POISSON__':blocks['POISSON_MT'],
        '__FORCE_EVAL__DFT__QS__':blocks['QS_HFX'],
        '__FORCE_EVAL__DFT__SCF__':blocks['SCF_OT_CG'],
        '__FORCE_EVAL__DFT__XC__':blocks['XC_HSE06'],
        
    },
    
    'LRC-wPBEh-GTH':{
        
        'template':'templates/dft_spin_pod.txt',
        
        '__FORCE_EVAL__DFT__BASIS_SET_FILE_NAME__':'GTH_BASIS_SETS',
        '__FORCE_EVAL__DFT__POTENTIAL_FILE_NAME__':'POTENTIAL',
        '__FORCE_EVAL__DFT__MGRID__CUTOFF__':450.0,
        '__FORCE_EVAL__DFT__MGRID__REL_CUTOFF__':75.0,
        '__FORCE_EVAL__DFT__SCF__MAX_SCF__':1000,
        '__FORCE_EVAL__DFT__SCF__SCF_GUESS__':'restart',
        '__FORCE_EVAL__DFT__POISSON__':blocks['POISSON_MT'],
        '__FORCE_EVAL__DFT__QS__':blocks['QS_HFX'],
        '__FORCE_EVAL__DFT__SCF__':blocks['SCF_OT_CG'],
        '__FORCE_EVAL__DFT__XC__':blocks['XC_LRC-wPBEh'],
        
    },
    
    'BLYP-GTH':{
        
        'template':'templates/dft_spin_pod.txt',
        
        '__FORCE_EVAL__DFT__BASIS_SET_FILE_NAME__':'GTH_BASIS_SETS',
        '__FORCE_EVAL__DFT__POTENTIAL_FILE_NAME__':'POTENTIAL',
        '__FORCE_EVAL__DFT__MGRID__CUTOFF__':450.0,
        '__FORCE_EVAL__DFT__MGRID__REL_CUTOFF__':75.0,
        '__FORCE_EVAL__DFT__SCF__MAX_SCF__':1000,
        '__FORCE_EVAL__DFT__SCF__SCF_GUESS__':'atomic',
        '__FORCE_EVAL__DFT__POISSON__':blocks['POISSON_MT'],
        '__FORCE_EVAL__DFT__QS__':blocks['QS_GGA'],
        '__FORCE_EVAL__DFT__SCF__':blocks['SCF_OT_CG'],
        '__FORCE_EVAL__DFT__XC__':blocks['XC_BLYP'],
        
    },
    
    'B3LYP-GTH':{
        
        'template':'templates/dft_spin_pod.txt',
        
        '__FORCE_EVAL__DFT__BASIS_SET_FILE_NAME__':'GTH_BASIS_SETS',
        '__FORCE_EVAL__DFT__POTENTIAL_FILE_NAME__':'POTENTIAL',
        '__FORCE_EVAL__DFT__MGRID__CUTOFF__':450.0,
        '__FORCE_EVAL__DFT__MGRID__REL_CUTOFF__':75.0,
        '__FORCE_EVAL__DFT__SCF__MAX_SCF__':1000,
        '__FORCE_EVAL__DFT__SCF__SCF_GUESS__':'restart',
        '__FORCE_EVAL__DFT__POISSON__':blocks['POISSON_MT'],
        '__FORCE_EVAL__DFT__QS__':blocks['QS_HFX'],
        '__FORCE_EVAL__DFT__SCF__':blocks['SCF_OT_CG'],
        '__FORCE_EVAL__DFT__XC__':blocks['XC_B3LYP'],
        
    },
    
    'wB97x-GTH':{
        
        'template':'templates/dft_spin_pod.txt',
        
        '__FORCE_EVAL__DFT__BASIS_SET_FILE_NAME__':'GTH_BASIS_SETS',
        '__FORCE_EVAL__DFT__POTENTIAL_FILE_NAME__':'POTENTIAL',
        '__FORCE_EVAL__DFT__MGRID__CUTOFF__':450.0,
        '__FORCE_EVAL__DFT__MGRID__REL_CUTOFF__':75.0,
        '__FORCE_EVAL__DFT__SCF__MAX_SCF__':1000,
        '__FORCE_EVAL__DFT__SCF__SCF_GUESS__':'restart',
        '__FORCE_EVAL__DFT__POISSON__':blocks['POISSON_MT'],
        '__FORCE_EVAL__DFT__QS__':blocks['QS_HFX'],
        '__FORCE_EVAL__DFT__SCF__':blocks['SCF_OT_CG'],
        '__FORCE_EVAL__DFT__XC__':blocks['XC_wB97x'],
        
    },
    
    'HSE06-GTH_OUTER_SCF':{
        
        'template':'templates/dft_spin_pod.txt',
        
        '__FORCE_EVAL__DFT__BASIS_SET_FILE_NAME__':'GTH_BASIS_SETS',
        '__FORCE_EVAL__DFT__POTENTIAL_FILE_NAME__':'POTENTIAL',
        '__FORCE_EVAL__DFT__MGRID__CUTOFF__':450.0,
        '__FORCE_EVAL__DFT__MGRID__REL_CUTOFF__':75.0,
        '__FORCE_EVAL__DFT__SCF__MAX_SCF__':100,
        '__FORCE_EVAL__DFT__SCF__SCF_GUESS__':'restart',
        '__FORCE_EVAL__DFT__POISSON__':blocks['POISSON_MT'],
        '__FORCE_EVAL__DFT__QS__':blocks['QS_HFX'],
        '__FORCE_EVAL__DFT__SCF__':blocks['SCF_OT_CG_OUTER'],
        '__FORCE_EVAL__DFT__XC__':blocks['XC_HSE06'],
        
    },
}

#--------------------------------------------------------------------

