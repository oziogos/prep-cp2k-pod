
from data.blocks import *
from src.utils import *

#--------------------------------------------------------------------

# coordinates dictionaries: keys correspond to xyz file paths;
# values hold descriptive comments

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

# basis set and pseudopotentials

#basis='DZVP-GTH'
basis='TZVP-GTH'

potential='GTH-PBE'

#--------------------------------------------------------------------

# dataset dictionaries

HAB7minus={
    'anthracene_charged':{
        'src':anthracene,
        'atoms':[24,24],
        'electrons':[66,66],
        'kinds':{
            'C':{'BASIS_SET':basis,'POTENTIAL':potential},
            'H':{'BASIS_SET':basis,'POTENTIAL':potential},
        },
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
}

#--------------------------------------------------------------------

# store basis and potential to driver dict
driver['basis']=basis
driver['potential']=potential

