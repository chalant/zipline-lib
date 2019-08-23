from contrib.control import clockengine

def create_clock(calendar, start_dt, end_dt=None, emission_rate='daily', type_='simulation'):
    if type_ == 'simulation':
        return clockengine.SimulationClock(calendar, emission_rate, start_dt, end_dt)