from bmtk.builder.networks import NetworkBuilder
import synapses

synapses.load()

net1 = NetworkBuilder('hco_net')
net1.add_nodes(N=1, 
              cell_name='HCOCell1',
              model_type='biophysical',
              model_template='hoc:HCOcell',
              morphology='blank.swc'
            )
            
net1.add_nodes(N=1, 
              cell_name='HCOCell2',
              model_type='biophysical',
              model_template='hoc:HCOcell',
              morphology='blank.swc'
            )
            

                        
conn = net1.add_edges(source={'cell_name': 'HCOCell1'}, target={'cell_name':'HCOCell2'},
              connection_rule=1,
              syn_weight=40.0e-02,
              dynamics_params='my_inhsyn.json',
              model_template='inhsyn',
              delay=0.0,
              target_sections=["soma"],
              distance_range=[0,999])
conn.add_properties(['sec_id','sec_x'],rule=(0, 0.5), dtypes=[np.int32,np.float])
              
conn = net1.add_edges(source={'cell_name': 'HCOCell2'}, target={'cell_name':'HCOCell1'},
              connection_rule=1,
              syn_weight=40.0e-02,
              dynamics_params='my_inhsyn.json',
              model_template='inhsyn',
              delay=0.0,
              target_sections=["soma"],
              distance_range=[0,999])
conn.add_properties(['sec_id','sec_x'],rule=(0, 0.5), dtypes=[np.int32,np.float])

net1.build()
net1.save_nodes(output_dir='network')             
              
net1.build()
net1.save_edges(output_dir='network')


#from bmtk.analyzer import node_types_table
#node_types_table(node_types_file='network/mcortex_node_types.csv', population='mcortex')
