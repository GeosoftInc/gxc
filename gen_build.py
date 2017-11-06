import glob
import os
from ninja_syntax import Writer

gxc_dirs = glob.glob('./examples/**/', recursive=True)

with open("build.ninja", "w") as buildfile:
    n = Writer(buildfile)
    
    n.rule("grc", command="cmd /c cd ${cwd} && grc ${in_name}", description="grc ${in_name}")
    n.rule("gxc", command="cmd /c cd ${cwd} && gxc ${in_name}", description="gxc ${in_name}")
    
    for dir in gxc_dirs:
        gxc_files = glob.glob(dir + '*.gxc')
        if gxc_files:
            grc_files = glob.glob(dir + '*.grc')
            gxc_implicit_inputs = []
            for grc_file in grc_files:
                #def build(self, outputs, rule, inputs=None, implicit=None, order_only=None,
                #variables=None, implicit_outputs=None):
                grc_file_name_part = os.path.split(grc_file)[1].split('.')[0]
                gr_file = os.path.join(dir, grc_file_name_part + '.gr')
                grh_file = os.path.join(dir, grc_file_name_part + '.grh')
                gxc_implicit_inputs.append(gr_file)
                gxc_implicit_inputs.append(grh_file)
                n.build(gr_file, 'grc', inputs=grc_file, implicit_outputs=grh_file, 
                        variables={'in_name': grc_file_name_part, 'cwd': dir})
            
            #TODO: Currently GXC uses the same temporary filename for preprocessed output which does not allow parallel builds with same working dir. 
            #      We make GXCs in same directory dependent on each other so they build serially 
            gxc_dep_files = [os.path.join(dir, os.path.split(f)[1].split('.')[0] + '.gx') for f in gxc_files]
            for gxc_file in gxc_files:
                gxc_file_name_part = os.path.split(gxc_file)[1].split('.')[0]
                gx_file = os.path.join('./build', gxc_file_name_part + '.gx')
                gxc_dep_files.remove(gx_file)
                inputs = [gxc_file]
                inputs.extend(gxc_dep_files)
                n.build(gx_file, 'gxc', inputs=inputs, implicit=gxc_implicit_inputs, 
                        variables={'in_name': gxc_file_name_part, 'cwd': dir})

