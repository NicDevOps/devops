
# Lib for electronic basics


class component:
    def __init__(self, amperes, component, foward_voltage, power_source, resistance):
        self.amperes = amperes
        self.component = component
        self.foward_voltage = foward_voltage
        self.power_source = power_source
        self.resistance = resistance
        
    def frame(self):
        x = """
        *************************************************************
            Component: {:s}                   
            Power source: {:1.3f} Volts | foward voltage: {:1.3f} Volts
            Amperes : {:1.3f} Amps
        *************************************************************
            Resistance needed: {:1.3f} Ohms

        """.format(self.component, self.power_source, self.foward_voltage, self.amperes, self.resistance)
        print(x)
