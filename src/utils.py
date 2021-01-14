import os
def read_xyz(filename):
    fp=open(filename,mode='r')
    xyz=fp.readlines()
    fp.close()
    atoms=int(xyz[0].strip())
    species=[]
    x=[]
    y=[]
    z=[]
    for i in range(atoms):
        line=xyz[i+2].strip().split()
        species.append(line[0])
        x.append(float(line[1]))
        y.append(float(line[2]))
        z.append(float(line[3]))
    return atoms,species,x,y,z
def replace_patterns(source,target,text):
    indentation=0
    block=False
    if(text.find('\n')!=-1):
        block=True
    for counter,i in enumerate(source):
        for j in i.split():
            if j.find(target)==0:
                indentation=i.index(target)
                if block==False:
                    source[counter]=source[counter].replace(target,text)
                else:
                    source[counter]=source[counter].replace(target,text.replace('\n','\n'+''.join([' ' for i in range(indentation)])))
    return indentation
def create_input(system_dict,system,driver_dict,driver,basis,potential,vacuum=8.0,occ_offset=3,virt_offset=4,hpc=None,restart=None):
    
    apply_defaults(system_dict,basis,potential)
    
    # store template to memory
    fp=open(f'{driver_dict[driver]["template"]}',mode='r')
    template=fp.readlines()
    fp.close()
    # replace all keywords from driver
    for key,value in driver_dict[driver].items():
        if key.find('__')==0:
            replace_patterns(template,key,str(value))
    # replace all keywords from system
    for key,value in system_dict[system].items():
        if key.find('__')==0:
            replace_patterns(template,key,str(value))
    # replace keywords in pod section
    for j,i in enumerate(template):
        if i.find('__M1_start__')!=-1:
            template[j]=i.replace('__M1_start__',str(1))
    for j,i in enumerate(template):
        if i.find('__M1_stop__')!=-1:
            template[j]=i.replace('__M1_stop__',str(system_dict[system]['atoms'][0]))
    for j,i in enumerate(template):
        if i.find('__M2_start__')!=-1:
            template[j]=i.replace('__M2_start__',str(system_dict[system]['atoms'][0]+1))
    for j,i in enumerate(template):
        if i.find('__M2_stop__')!=-1:
            template[j]=i.replace('__M2_stop__',str(system_dict[system]['atoms'][0]+system_dict[system]['atoms'][1]))
    for j,i in enumerate(template):
        if i.find('__M1_NELECTRON__')!=-1:
            template[j]=i.replace('__M1_NELECTRON__',str(system_dict[system]['electrons'][0]))
        if i.find('__M2_NELECTRON__')!=-1:
            template[j]=i.replace('__M2_NELECTRON__',str(system_dict[system]['electrons'][1]))
    # replace kinds
    kinds=[]
    for key,value in system_dict[system]['kinds'].items():
        kinds.append(f'&KIND {key}\n')
        for i,j in value.items():
            kinds.append(f' {i} {j}\n')
        kinds.append('&END KIND\n')
    kinds[-1]=kinds[-1].replace('\n',' ')
    kinds=''.join(kinds)
    replace_patterns(template,'__FORCE_EVAL__SUBSYS__KIND__',kinds)
    # prep cube preview
    for j,i in enumerate(template):
        if i.find('__M1MO_start__')!=-1:
            template[j]=template[j].replace('__M1MO_start__',str(int(system_dict[system]['electrons'][0]/2-occ_offset)))
            template[j]=template[j].replace('__M1MO_stop__',str(int(system_dict[system]['electrons'][0]/2+virt_offset)))
    for j,i in enumerate(template):
        if i.find('__M2MO_start__')!=-1:
            template[j]=template[j].replace('__M2MO_start__',str(int(system_dict[system]['electrons'][1]/2-occ_offset)))
            template[j]=template[j].replace('__M2MO_stop__',str(int(system_dict[system]['electrons'][1]/2+virt_offset)))
    
    # treat closed shell
    if system_dict[system]['__FORCE_EVAL__DFT__SPIN_POLARIZED__']=='.false.':
        for j,i in enumerate(template):
            if i.find('__FORCE_EVAL__DFT__MULTIPLICITY__')!=-1:
                template[j]=''
    
    # backup current template state
    template0=[i for i in template]
    # prep wfn restart dict
    wfn_restart_dict={}
    # read xyz files
    for xyz,info in system_dict[system]['src'].items():
        
        # resolve simulation name
        name=f'{system}_{info}_{basis}_{driver}'
        # replace name
        replace_patterns(template,'__GLOBAL__PROJECT_NAME__',name)
        
        # store wfn dict values
        wfn_restart_dict[(xyz,info)]=f'{name}-RESTART.wfn '
        
        # apply restart keyword
        if driver_dict[driver]['__FORCE_EVAL__DFT__SCF__SCF_GUESS__']=='restart':
            for line,i in enumerate(template):
                if i.find('POTENTIAL_FILE_NAME')!=-1:
                    offset=i.index('POTENTIAL_FILE_NAME')
                    break
            template.insert(line+1,''.join([' ' for i in range(offset)])+f'WFN_RESTART_FILE_NAME {restart[(xyz,info)]}'+'\n')
        
        atoms,species,x,y,z=read_xyz(xyz)
        # center molecule
        X,Y,Z=[sum(i)/atoms for i in [x,y,z]]
        lx,ly,lz=[max(x)-min(x)+vacuum,max(y)-min(y)+vacuum,max(z)-min(z)+vacuum]
        x,y,z=[[i-X+lx/2 for i in x],[i-Y+ly/2 for i in y],[i-Z+lz/2 for i in z]]
        # preview
    #     with open('preview.dat',mode='w') as fp:
    #         print(atoms+8,file=fp)
    #         print(file=fp)
    #         for i in range(atoms):
    #             print(f'{species[i]} {x[i]} {y[i]} {z[i]}',file=fp)
    #         print(f'Xx {0} {0} {0}',file=fp)
    #         print(f'Xx {lx} {0} {0}',file=fp)
    #         print(f'Xx {lx} {ly} {0}',file=fp)
    #         print(f'Xx {0} {ly} {0}',file=fp)
    #         print(f'Xx {0} {0} {lz}',file=fp)
    #         print(f'Xx {lx} {0} {lz}',file=fp)
    #         print(f'Xx {lx} {ly} {lz}',file=fp)
    #         print(f'Xx {0} {ly} {lz}',file=fp)
        # replace cell
        for j,i in enumerate(template):
            if i.find('__FORCE_EVAL__SUBSYS__CELL__A__')!=-1:
                template[j]=template[j].replace('__FORCE_EVAL__SUBSYS__CELL__A__',str(lx))
                template[j]=template[j].replace('__FORCE_EVAL__SUBSYS__CELL__B__',str(ly))
                template[j]=template[j].replace('__FORCE_EVAL__SUBSYS__CELL__C__',str(lz))
        # replace coords
        coords=[]
        for i in range(atoms):
            coords.append(f'{species[i]} {x[i]} {y[i]} {z[i]}\n')
        coords[-1]=coords[-1].replace('\n','')
        coords=''.join(coords)
        replace_patterns(template,'__FORCE_EVAL__SUBSYS__COORD__',coords)
        # write to file
        if os.path.exists('output')==False:
            os.mkdir('output')
        if os.path.exists(f'output/{system}_{basis}_{driver}')==False:
            os.mkdir(f'output/{system}_{basis}_{driver}')
        outfile=f'output/{system}_{basis}_{driver}/{name}.inp'
        with open(outfile,mode='w') as fp:
            for i in template:
                print(i,end='',file=fp)
        # reset
        template=[i for i in template0]
        # create hpc output
        if hpc is not None:
            if hpc["arch"]=='aprun':
                print(f'{hpc["arch"]} -n {hpc["cores"]} cp2k.popt -i {name}.inp > {name}.out')
                
    return wfn_restart_dict

def apply_defaults(input_dict,basis,potential):
    for key,value in input_dict.items():
        #if 'kinds' not in value:
        fp=open(list(value['src'])[0],mode='r')
        xyz=fp.readlines()
        fp.close()
        #species=list(set([i.strip().split()[0] for i in xyz][2:int(xyz[0])+2]))
        species=list(set([i.split()[0] for i in xyz[2::]]))
        value['kinds']={i:{'BASIS_SET':basis,'POTENTIAL':potential} for i in species}
        if '__FORCE_EVAL__DFT__CHARGE__' not in value:
            value['__FORCE_EVAL__DFT__CHARGE__']=0
        if '__FORCE_EVAL__DFT__SPIN_POLARIZED__' not in value:
            value['__FORCE_EVAL__DFT__SPIN_POLARIZED__']='.true.'
        if '__FORCE_EVAL__DFT__MULTIPLICITY__' not in value:
            value['__FORCE_EVAL__DFT__MULTIPLICITY__']=1