from bmtk.builder.networks import NetworkBuilder

net1 = NetworkBuilder('hco_net')
net1.add_nodes(N=1, 
              pop_name='hco1',
              cell_name='HCOCell1',
              model_type='biophysical',
              model_template='hoc:HCOcell',
              morphology='blank.swc'
            )
            
net1.add_nodes(N=1, 
              pop_name='hco2',
              cell_name='HCOCell2',
              model_type='biophysical',
              model_template='hoc:HCOcell',
              morphology='blank.swc'
            )
            
net1.build()
net1.save_nodes(output_dir='network')
                        
net1.add_edges(source={'pop_name': 'hco1'}, target={'pop_name':'hco2'},
              connection_rule=1,
              syn_weight=40.0e-03,
              dynamics_params='GABA_InhToInh.json',
              model_template='Exp2Syn',
              delay=0.0,
              target_sections=["soma"],
              distance_range=99999999)
              
net1.add_edges(source={'pop_name': 'hco2'}, target={'pop_name':'hco1'},
              connection_rule=1,
              syn_weight=40.0e-03,
              dynamics_params='GABA_InhToInh.json',
              model_template='Exp2Syn',
              delay=0.0,
              target_sections=["soma"],
              distance_range=99999999)
                           
              
net1.build()
net1.save_edges(output_dir='network')

#from bmtk.analyzer import node_types_table
#node_types_table(node_types_file='network/mcortex_node_types.csv', population='mcortex')
