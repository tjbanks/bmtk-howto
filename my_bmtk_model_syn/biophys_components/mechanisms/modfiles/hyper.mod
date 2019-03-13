: Hyperpolarization-activated channel (also known as funny current)

NEURON {
	SUFFIX hyper
	USEION h READ eh WRITE ih VALENCE 1
	RANGE gbar, g
	RANGE hminf, hmtau
	RANGE ih
}

UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)
}

PARAMETER {
	gbar (siemens/cm2)
}

ASSIGNED {
	v (mV)
	eh (mV)
	ih (mA/cm2)
	hminf
	hmtau (ms)
	g (siemens/cm2)
}

STATE {
	hm
}

BREAKPOINT {
	SOLVE states METHOD cnexp
	g = gbar*hm
	ih = g*(v-eh)
}

INITIAL {
	rate(v)
	hm = hminf
}

DERIVATIVE states {
	rate(v)
	hm' = (hminf-hm)/hmtau
}	

PROCEDURE rate(v (mV)) {
	UNITSOFF
	hminf = 1/(1+(exp ((v+75)/(5.5))))      
	hmtau = 2.0/( (exp ((v+169.7)/(-11.6))) + (exp ((v-26.7)/14.3)))   
	UNITSON	
}
