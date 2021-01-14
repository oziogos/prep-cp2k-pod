
# block expressions for cp2k:qs dft simulations

blocks={
    
    'POISSON_MT':
    'PERIODIC none\n'
        'POISSON_SOLVER mt\n'
        '&MT\n'
        ' ALPHA 7.0\n'
        ' REL_CUTOFF 2.0\n'
        '&END MT',
    
    'QS_GGA':
    '&QS\n'
    ' EPS_DEFAULT 1.0e-10\n'
    ' EXTRAPOLATION ps\n'
    ' EXTRAPOLATION_ORDER 3\n'
    ' MAP_CONSISTENT .true.\n'
    '&END QS',
    
    'QS_HFX':
    '&QS\n'
    ' EPS_DEFAULT 1.0e-10\n'
    ' EPS_PGF_ORB 1.0e-32\n'
    ' EPS_FILTER_MATRIX 1.0e-32\n'
    ' EXTRAPOLATION ps\n'
    ' EXTRAPOLATION_ORDER 3\n'
    ' MAP_CONSISTENT .true.\n'
    '&END QS',
    
    'SCF_OT_CG':
    'EPS_SCF 1.0e-6\n'
    '&OT on\n'
    ' MINIMIZER cg\n'
    ' PRECONDITIONER full_all\n'
    ' ENERGY_GAP 0.01\n'
    '&END OT\n'
    '&PRINT\n'
    ' &RESTART on\n'
    ' &END\n'
    '&END',
    
    'SCF_OT_CG_OUTER':
    'EPS_SCF 1.0e-6\n'
    '&OT on\n'
    ' MINIMIZER cg\n'
    ' PRECONDITIONER full_all\n'
    ' ENERGY_GAP 0.01\n'
    '&END OT\n'
    '&OUTER_SCF\n'
    ' EPS_SCF 1.0e-6\n'
    ' MAX_SCF 20\n'
    '&END OUTER_SCF\n'
    '&PRINT\n'
    ' &RESTART on\n'
    ' &END\n'
    '&END',
    
    'XC_PBE':
    '&XC\n'
    ' &XC_FUNCTIONAL pbe\n'
    ' &END XC_FUNCTIONAL\n'
    '&END XC',
    
    'XC_PBE0':
    '&XC\n'
    ' &XC_FUNCTIONAL\n'
    '  &PBE\n'
    '   PARAMETRIZATION orig\n'
    '   SCALE_X 0.75\n'
    '  &END PBE\n'
    ' &END XC_FUNCTIONAL\n'
    ' &HF\n'
    '  FRACTION 0.25\n'
    '  &SCREENING\n'
    '   EPS_SCHWARZ 1.0E-10\n'
    '   SCREEN_ON_INITIAL_P .false.\n'
    '  &END\n'
    '  &INTERACTION_POTENTIAL\n'
    '   POTENTIAL_TYPE coulomb\n'
    '  &END INTERACTION_POTENTIAL\n'
    ' &END HF\n'
    '&END XC',
    
    'XC_HSE06':
    '&XC\n'
    ' &XC_FUNCTIONAL\n'
    '  &LIBXC\n'
    '   FUNCTIONAL HYB_GGA_XC_HSE06\n'
    '  &END LIBXC\n'
    ' &END XC_FUNCTIONAL\n'
    ' &HF\n'
    '  FRACTION 0.25\n'
    '  &SCREENING\n'
    '   EPS_SCHWARZ 1.0E-10\n'
    '   SCREEN_ON_INITIAL_P .false.\n'
    '  &END\n'
    '  &INTERACTION_POTENTIAL\n'
    '   POTENTIAL_TYPE shortrange\n'
    '   OMEGA 0.11\n'
    '  &END INTERACTION_POTENTIAL\n'
    ' &END HF\n'
    '&END XC\n',
    
    'XC_LRC-wPBEh':
    '&XC\n'
    ' &XC_FUNCTIONAL\n'
    '  &LIBXC\n'
    '   FUNCTIONAL HYB_GGA_XC_LRC_WPBEH\n'
    '  &END LIBXC\n'
    ' &END XC_FUNCTIONAL\n'
    ' &HF\n'
    '  &SCREENING\n'
    '   EPS_SCHWARZ 1.0E-10\n'
    '   SCREEN_ON_INITIAL_P .false.\n'
    '  &END\n'
    '  &INTERACTION_POTENTIAL\n'
    '   POTENTIAL_TYPE mix_cl\n'
    '   OMEGA 0.2\n'
    '   SCALE_COULOMB 0.2\n'
    '   SCALE_LONGRANGE 0.8\n'
    '  &END INTERACTION_POTENTIAL\n'
    ' &END HF\n'
    '&END XC\n',
    
    'XC_wB97x':
    '&XC\n'
    ' &XC_FUNCTIONAL\n'
    '  &LIBXC\n'
    '   FUNCTIONAL HYB_GGA_XC_WB97X\n'
    '  &END LIBXC\n'
    ' &END XC_FUNCTIONAL\n'
    ' &HF\n'
    '  &SCREENING\n'
    '   EPS_SCHWARZ 1.0E-10\n'
    '   SCREEN_ON_INITIAL_P .false.\n'
    '  &END\n'
    '  &INTERACTION_POTENTIAL\n'
    '   POTENTIAL_TYPE mix_cl\n'
    '   OMEGA 0.3\n'
    '   SCALE_COULOMB 0.157706\n'
    '   SCALE_LONGRANGE 0.842294\n'
    '  &END INTERACTION_POTENTIAL\n'
    ' &END HF\n'
    '&END XC\n',
    
    'XC_B3LYP':
    '&XC\n'
    ' &XC_FUNCTIONAL b3lyp\n'
    ' &END XC_FUNCTIONAL\n'
    '&END XC\n',
    
    'XC_BLYP':
    '&XC\n'
    ' &XC_FUNCTIONAL blyp\n'
    ' &END XC_FUNCTIONAL\n'
    '&END XC\n',
    
}
