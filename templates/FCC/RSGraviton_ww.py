import ROOT
import collections

### variable list
variables = {
	'Jet1_tau21':{'name':'Jet1_trk02_tau21','title':'Jet1 #tau_{2,1}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet1_tau32':{'name':'Jet1_trk02_tau32','title':'Jet1 #tau_{3,2}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet1_tau31':{'name':'Jet1_trk02_tau31','title':'Jet1 #tau_{3,1}','bin':50,'xmin':0.0,'xmax':1.0},

        'Jet1_SD_Cor_pt':{'name':'Jet1_trk02_SD_Corr_pt','title':'Jet1 p_{T} (SD cor) [TeV]','bin':65,'xmin':2,'xmax':15, 'divide':1000},
        'Jet1_SD_Cor_eta':{'name':'Jet1_trk02_SD_Corr_eta','title':'Jet1 #eta (SD cor)','bin':50,'xmin':-5.0,'xmax':5.0},
        'Jet1_trk02_SD_Cor_m':{'name':'Jet1_trk02_SD_Corr_m','title':'Jet1 trk02 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},
        'Jet1_trk04_SD_Cor_m':{'name':'Jet1_trk04_SD_Corr_m','title':'Jet1 trk04 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},
        'Jet1_trk08_SD_Cor_m':{'name':'Jet1_trk08_SD_Corr_m','title':'Jet1 trk08 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},

	'Jet2_tau21':{'name':'Jet2_trk02_tau21','title':'Jet2 #tau_{2,1}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet2_tau32':{'name':'Jet2_trk02_tau32','title':'Jet2 #tau_{3,2}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet2_tau31':{'name':'Jet2_trk02_tau31','title':'Jet2 #tau_{3,1}','bin':50,'xmin':0.0,'xmax':1.0},

        'Jet2_SD_Cor_pt':{'name':'Jet2_trk02_SD_Corr_pt','title':'Jet2 p_{T} (SD cor) [TeV]','bin':65,'xmin':2,'xmax':15, 'divide':1000},
        'Jet2_SD_Cor_eta':{'name':'Jet2_trk02_SD_Corr_eta','title':'Jet2 #eta (SD cor)','bin':50,'xmin':-5.0,'xmax':5.0},
        'Jet2_trk02_SD_Cor_m':{'name':'Jet2_trk02_SD_Corr_m','title':'Jet2 trk02 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},
        'Jet2_trk04_SD_Cor_m':{'name':'Jet2_trk04_SD_Corr_m','title':'Jet2 trk04 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},
        'Jet2_trk08_SD_Cor_m':{'name':'Jet2_trk08_SD_Corr_m','title':'Jet2 trk08 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},

        'rapiditySeparation':{'name':'rapiditySeparation_trk02','title':'Rapidity Separation','bin':50,'xmin':0.0,'xmax':10.0},
        'transverseMomentumAsymmetry':{'name':'transverseMomentumAsymmetry_trk02','title':'Transverse Momentum Asymmetry','bin':50,'xmin':0.0,'xmax':1.0},

#        'Mj1j2_trk02' :{'name':'Mj1j2_trk02','title':'m_{Z\'} [TeV] (trk02)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},
#        'Mj1j2_trk02_Corr' :{'name':'Mj1j2_trk02_Corr','title':'m_{Z\'} [TeV] (trk02 cor)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},

#        'Mj1j2_pf02' :{'name':'Mj1j2_pf02','title':'m_{Z\'} [TeV] (pf02)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},

#        'Mj1j2_pf04' :{'name':'Mj1j2_pf04','title':'m_{Z\'} [TeV] (pf04)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},

        'Mj1j2_pf08' :{'name':'Mj1j2_pf08','title':'m_{Z\'} [TeV] (pf08)','bin':225,'xmin':5.0,'xmax':50.0, 'divide':1000},

        'Jet1_Flow15':{'name':'Jet1_Flow15','title':'Flow_{1,5} Jet_1','bin':200,'xmin':0.0,'xmax':1.0},
        'Jet2_Flow15':{'name':'Jet2_Flow15','title':'Flow_{1,5} Jet_2','bin':200,'xmin':0.0,'xmax':1.0},
        'Jet1_Flow25':{'name':'Jet1_Flow25','title':'Flow_{2,5} Jet_1','bin':200,'xmin':0.0,'xmax':1.0},
        'Jet2_Flow25':{'name':'Jet2_Flow25','title':'Flow_{2,5} Jet_2','bin':200,'xmin':0.0,'xmax':1.0},
        'Jet1_Flow35':{'name':'Jet1_Flow35','title':'Flow_{3,5} Jet_1','bin':200,'xmin':0.0,'xmax':1.0},
        'Jet2_Flow35':{'name':'Jet2_Flow35','title':'Flow_{3,5} Jet_2','bin':200,'xmin':0.0,'xmax':1.0},
        'Jet1_Flow45':{'name':'Jet1_Flow45','title':'Flow_{4,5} Jet_1','bin':200,'xmin':0.0,'xmax':1.0},
        'Jet2_Flow45':{'name':'Jet2_Flow45','title':'Flow_{4,5} Jet_2','bin':200,'xmin':0.0,'xmax':1.0},
        'Jet1_Flow55':{'name':'Jet1_Flow55','title':'Flow_{5,5} Jet_1','bin':200,'xmin':0.0,'xmax':1.0},
        'Jet2_Flow55':{'name':'Jet2_Flow55','title':'Flow_{5,5} Jet_2','bin':200,'xmin':0.0,'xmax':1.0},
#        'BDTvariable_qcd' :{'name':'BDTvariable_qcd','title':'QCD BDT score','bin':100,'xmin':-0.5,'xmax':0.5},
        'Jet1_Whad_vs_QCD_tagger' :{'name':'Jet1_Whad_vs_QCD_tagger','title':'Jet1 W had. vs QCD tagger','bin':100,'xmin':-1.,'xmax':1.},
        'Jet2_Whad_vs_QCD_tagger' :{'name':'Jet2_Whad_vs_QCD_tagger','title':'Jet2 W had. vs QCD tagger','bin':100,'xmin':-1.,'xmax':1.},
}

variables2D = {}


colors = {}
colors['m_{RSG} = 10 TeV'] = ROOT.kRed
colors['m_{RSG} = 15 TeV'] = ROOT.kRed
colors['m_{RSG} = 20 TeV'] = ROOT.kRed
colors['m_{RSG} = 25 TeV'] = ROOT.kRed
colors['m_{RSG} = 30 TeV'] = ROOT.kRed
colors['m_{RSG} = 35 TeV'] = ROOT.kRed
colors['QCD'] = ROOT.kBlue+1
colors['tt'] = ROOT.kOrange-2
colors['vv'] = ROOT.kGreen+2
colors['vj'] = ROOT.kMagenta+2

signal_groups = collections.OrderedDict()
signal_groups['m_{RSG} = 10 TeV'] = ['pp_RSGraviton_10TeV_ww']
signal_groups['m_{RSG} = 15 TeV'] = ['pp_RSGraviton_15TeV_ww']
signal_groups['m_{RSG} = 20 TeV'] = ['pp_RSGraviton_20TeV_ww']
signal_groups['m_{RSG} = 25 TeV'] = ['pp_RSGraviton_25TeV_ww']
signal_groups['m_{RSG} = 30 TeV'] = ['pp_RSGraviton_30TeV_ww']
signal_groups['m_{RSG} = 35 TeV'] = ['pp_RSGraviton_35TeV_ww']



background_groups = collections.OrderedDict()

background_groups['vv']  = ['pp_vv_lo'] 
background_groups['vj'] = ['pp_vj_4f_M_5000_inf']
background_groups['tt']  = ['pp_tt_lo']
background_groups['QCD'] = ['pp_jj_lo']



# global parameters
intLumi = 3.0e+07
delphesVersion = '3.4.2'

uncertainties = []
uncertainties.append([0., 0.])
uncertainties.append([0.02, 0.0])
uncertainties.append([0.02, 0.02])
uncertainties.append([0.02, 0.10])

# the first time needs to be set to True
runFull = True

#####################
# base pre-selections
#####################
selbase = 'Jet1_trk02_SD_Corr_pt > 3000. && Jet2_trk02_SD_Corr_pt > 3000. && abs(Jet1_trk02_SD_Corr_eta) < 3.&& abs(Jet1_trk02_SD_Corr_eta) < 3.'
# clean cuts
selbase += ' && Jet1_trk02_tau21>0 && Jet1_trk02_tau31>0 && Jet1_trk02_tau32>0 && Jet2_trk02_tau21>0 && Jet2_trk02_tau31>0 && Jet2_trk02_tau32>0'

#####################
# CUT base selection
#####################
#sel1 = selbase + '&& Jet1_trk02_SD_Corr_m > 50.&& Jet1_trk02_SD_Corr_m < 100. && Jet2_trk02_SD_Corr_m > 50.&& Jet2_trk02_SD_Corr_m < 100. && Jet1_trk02_tau21 <0.6 && Jet2_trk02_tau21 <0.6'
#sel2 = sel1 +    '&& Jet1_Flow15 > 0.85 && Jet2_Flow15 > 0.85 && Jet1_Flow25 < 0.05 && Jet2_Flow25 < 0.05'

#####################
# MVA selection
#####################
#sel2 = selbase + ' && BDTvariable_qcd > 0.27'

#####################
# anti-QCD jet tagger selection
#####################
sel1 = selbase + ' && Jet1_Whad_vs_QCD_tagger>0.15 && Jet2_Whad_vs_QCD_tagger>0.15'
## + extra cuts
sel2 = sel1    + ' && Jet1_trk02_SD_Corr_m>40. && Jet2_trk02_SD_Corr_m>40.'

selections = collections.OrderedDict()
selections['m_{RSG} = 10 TeV'] = []
selections['m_{RSG} = 10 TeV'].append(selbase)
selections['m_{RSG} = 10 TeV'].append(sel1)
selections['m_{RSG} = 10 TeV'].append(sel2)

selections['m_{RSG} = 15 TeV'] = []
selections['m_{RSG} = 15 TeV'].append(selbase)
#selections['m_{RSG} = 15 TeV'].append(sel1)
selections['m_{RSG} = 15 TeV'].append(sel2)

selections['m_{RSG} = 20 TeV'] = []
selections['m_{RSG} = 20 TeV'].append(selbase)
#selections['m_{RSG} = 20 TeV'].append(sel1)
selections['m_{RSG} = 20 TeV'].append(sel2)

selections['m_{RSG} = 25 TeV'] = []
selections['m_{RSG} = 25 TeV'].append(selbase)
#selections['m_{RSG} = 25 TeV'].append(sel1)
selections['m_{RSG} = 25 TeV'].append(sel2)

selections['m_{RSG} = 30 TeV'] = []
selections['m_{RSG} = 30 TeV'].append(selbase)
#selections['m_{RSG} = 30 TeV'].append(sel1)
selections['m_{RSG} = 30 TeV'].append(sel2)

selections['m_{RSG} = 35 TeV'] = []
selections['m_{RSG} = 35 TeV'].append(selbase)
#selections['m_{RSG} = 35 TeV'].append(sel1)
selections['m_{RSG} = 35 TeV'].append(sel2)

